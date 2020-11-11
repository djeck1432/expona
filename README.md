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


## Tests

# api/all
`1000 requests 100 requests concurrency`

```bash
Concurrency Level:      100
Time taken for tests:   0.670 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Total transferred:      225000 bytes
HTML transferred:       55000 bytes
Requests per second:    1492.72 [#/sec] (mean)
Time per request:       66.992 [ms] (mean)
Time per request:       0.670 [ms] (mean, across all concurrent requests)
Transfer rate:          327.99 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    3   1.3      2       7
Processing:     6   63   6.1     65      74
Waiting:        1   45   9.3     47      66
Total:          6   65   5.8     67      74

Percentage of the requests served within a certain time (ms)
  50%     67
  66%     68
  75%     69
  80%     69
  90%     70
  95%     71
  98%     74
  99%     74
 100%     74 (longest request)

```



