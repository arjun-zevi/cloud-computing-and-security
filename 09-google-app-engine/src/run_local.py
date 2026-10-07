"""Serves src/legacy/index.py (a CGI-style script) on http://localhost:8080
- a tiny stand-in for the old Google App Engine Launcher dev server."""
import os, subprocess, sys
from http.server import BaseHTTPRequestHandler, HTTPServer

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "legacy", "index.py")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        out = subprocess.run([sys.executable, SCRIPT], capture_output=True, text=True).stdout
        head, _, body = out.partition("\n\n")
        self.send_response(200)
        self.send_header("Content-Type", head.split(":", 1)[1].strip())
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == "__main__":
    print("Serving on http://localhost:8080  (Ctrl+C to stop)")
    HTTPServer(("127.0.0.1", 8080), Handler).serve_forever()
