from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

class SimpleHTTPRequestHanlder(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        self.send_response(200)
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        response = BytesIO()
        response.write(b"POST request: ")
        response.write(b'Response: ')
        response.write(body)
        self.wfile.write(response.getvalue())

httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHanlder)
httpd.serve_forever()