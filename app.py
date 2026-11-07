from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = """
        <html>
        <head><title>Greeter App</title></head>
        <body>
            <h1>Hello, Abdul Hanan!</h1>
            <p>Welcome to my Docker project.</p>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("Server running on port 8000...")
server.serve_forever()
