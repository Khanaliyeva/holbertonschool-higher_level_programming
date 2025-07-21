#!/usr/bin/env python3
import http.server
import socketserver
import json

PORT = 8000

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Əsas səhifə: /
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # /data endpointi
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # /status endpointi
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # /info endpointi (əlavə, istəyə görə)
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # Tanınmayan endpoin
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error = {"message": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode("utf-8"))

# Serveri işə sal
if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Server started at http://localhost:{PORT}")
        httpd.serve_forever()
