# python-waf-benchmark

Benchmark for Python web application frameworks.

## Date
Jul 14, 2017

## Bench

### bottle
```bash
$ wrk -t1 -c1 http://localhost:6000/
Running 10s test @ http://localhost:6000/
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   366.71us    2.40ms  54.01ms   98.45%
    Req/Sec     7.87k     1.53k    9.27k    90.00%
  78448 requests in 10.04s, 13.17MB read
Requests/sec:   7812.26
Transfer/sec:      1.31MB
```
### flask
```bash
$ wrk -t1 -c1 http://localhost:6000/
Running 10s test @ http://localhost:6000/
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   284.10us  254.37us  10.02ms   97.05%
    Req/Sec     3.71k   468.17     4.17k    84.16%
  37331 requests in 10.10s, 6.27MB read
Requests/sec:   3696.18
Transfer/sec:    635.28KB
```
### wsgi
```bash
$ wrk -t1 -c1 http://localhost:6000/
Running 10s test @ http://localhost:6000/
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    11.47ms   45.46ms 390.30ms   93.89%
    Req/Sec     7.83k     3.12k   13.46k    78.49%
  74051 requests in 10.02s, 11.44MB read
Requests/sec:   7392.02
Transfer/sec:      1.14MB
```

## env

Python version: CPython 3.6.1

Web server: Meinheld 0.6.1

MacBook Pro, 2.7 GHz Intel Core i5, 8 GB 1867 MHz DDR3

## How to run

```
bottle : gunicorn -k meinheld.gmeinheld.MeinheldWorker -b :6000 app:bottle_app
flask  : gunicorn -k meinheld.gmeinheld.MeinheldWorker -b :6000 app:flask_app
wsgi   : gunicorn -k meinheld.gmeinheld.MeinheldWorker -b :6000 app:wsgi
```