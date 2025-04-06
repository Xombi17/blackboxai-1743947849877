from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="supermarket-checkout-app/public", **kwargs)

if __name__ == '__main__':
    port = 8000
    server = HTTPServer(('', port), Handler)
    print(f'Server running on port {port}')
    server.serve_forever()