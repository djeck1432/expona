# Expona assignment


- Download this repo with terminal:
```bash
git clone https://github.com/djeck1432/expona.git
```

- Open the repo in terminal:
```bash
cd expona
```

## Run server on the local machine:

- Install requirements:
```bash
pip install -r app/requirements.txt
```
- Start server:
```bash
python3 app/src/server.py
```


## Build and Run a Docker container

- Build container
```bash
docker build -t expona .
```

- Run container with `port:8080`
```bash
docker run -p 8080:8080 expona
```

## API endpoint

`params` - timeout in `milliseconds`

`api/all` - return 3 success responses if timeout not ended, else error

`api/first` - return the first success response if timeout not ended, else error

`api/within-timeout` - If a timeout is reached before any of the 3 requests finish, the server should return an empty array instead of an error.  


Example: 
```url
https://example.com/api/all?timeout=400
```



