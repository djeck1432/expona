import logging
import aiohttp
import asyncio
from anyio import create_task_group


logger = logging.getLogger('expona_server')
URL = 'https://exponea-engineering-assignment.appspot.com/api/work'
AMOUNT_REQUESTS = 3


async def send_request_to_expona(session, responses, url, first):
    async with session.get(url) as resp:
        if resp.status == 200:
            response = await resp.json()
            responses.append(response)
        else:
            logger.error(f'Response from Expona server  status : {resp.status}')
        if first:
            raise asyncio.CancelledError


async def send_requests(
            responses,
            amount_requests=AMOUNT_REQUESTS,
            url=URL,
            first=False
        ):
    # Connector changing limit requests
    connector = aiohttp.TCPConnector(limit=None)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with create_task_group() as expona:
            for item in range(amount_requests):
                await expona.spawn(
                        send_request_to_expona,
                        session,
                        responses,
                        url,
                        first,
                    )
