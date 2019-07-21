from http.server import HTTPServer, BaseHTTPRequestHandler, ThreadingHTTPServer
from socketserver import ThreadingMixIn
import threading
from urllib.parse import urlparse


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        message = threading.currentThread().getName()
        self.wfile.write(message.encode())
        # self.wfile.write('\n')
        return

    def do_POST(self):
        # Begin the response
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        print(self.data_string)
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' % str(self.client_address).encode())
        print('post---------')
        return


# class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
#     """Handle requests in a separate thread."""


if __name__ == '__main__':
    server = ThreadingHTTPServer(('localhost', 8080), Handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()