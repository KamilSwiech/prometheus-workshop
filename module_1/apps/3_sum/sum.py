import http.server
import time
import random
from prometheus_client import start_http_server
from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import Summary
REQUEST = Counter('hello_worlds_total','Hello Worlds requested.')
EXCEPTIONS = Counter('hello_worlds_exceptions_total','Exceptions serving Hello Worlds.')
INPROGRESS = Gauge('hello_worlds_inprogress','Numer of Hello Worlds in progress.')
LAST = Gauge('hello_world_last_time_seconds','The last time a Hello World was served.')
LATENCY = Summary('hello_world_latency_seconds','Time for a request Hello World.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        INPROGRESS.inc()
        start = time.time()
        REQUEST.inc()
        with EXCEPTIONS.count_exceptions():
            if random.random() < 0.2:
                raise Exception
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")
        LAST.set(time.time())
        LATENCY.observe(time.time()-start)
        INPROGRESS.dec()
        
if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer (('0.0.0.0',8001), MyHandler)
    server.serve_forever()
