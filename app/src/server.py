import logging
import async_timeout
import asyncio
from aiohttp import web
from contextlib import suppress
from client import send_requests


routes = web.RouteTableDef()
logger = logging.getLogger('expona')


def get_timeout_from_request(request):
    timeout = request.rel_url.query["timeout"]
    if not timeout:
        return 1000
    if not timeout.isdigit():
        logger.error('Invalid timeout in request')
        raise web.HTTPNotFound(text='ServerError: Invalid timeout')
    return int(timeout) / 1000


@routes.get('/api/all')
async def get_all(request):
    timeout = get_timeout_from_request(request)
    responses = []
    async with async_timeout.timeout(timeout) as cm:
        await send_requests(responses)
        if len(responses) == 3:
            return web.json_response(responses)
        logger.warning(
            f'Not all responses were success for /api/all, expected 3 but given {len(responses)}'
            )
        raise web.HTTPNotFound()
    if cm.expired:
        logger.warning('api/all TimeoutError')
        raise web.HTTPNotFound(text='TimeoutError')


@routes.get('/api/first')
async def get_first(request):
    timeout = get_timeout_from_request(request)
    response = []
    async with async_timeout.timeout(timeout) as cm:
        with suppress(asyncio.CancelledError):
            await send_requests(response, first=True)
        if response:
            return web.json_response(response)
        logger.warning('api/first TimeoutError')
    if cm.expired:
        logger.warning('api/first TimeoutError')
        raise web.HTTPNotFound(text='TimeoutError')


@routes.get('/api/within-timeout')
async def get_all_success_within_timeout(request):
    timeout = get_timeout_from_request(request)
    responses = []
    async with async_timeout.timeout(timeout):
        await send_requests(responses)
        return web.json_response(responses)


if __name__ == '__main__':
    logging.basicConfig(
        format=u'%(levelname)-8s %(message)s', level=1)

    app = web.Application()
    app.router.add_routes(routes)
    web.run_app(app)
