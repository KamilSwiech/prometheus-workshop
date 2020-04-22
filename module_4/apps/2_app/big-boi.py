import http.server
import random
from prometheus_client import start_http_server
from prometheus_client import Counter

REQUEST = Counter('hello_worlds_total','Hello Worlds requested.',labelnames=['path','method','id'])
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUEST.labels(self.path,self.command,random.uniform(0,10000)).inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")
        
if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer (('0.0.0.0',8001), MyHandler)
    server.serve_forever()
