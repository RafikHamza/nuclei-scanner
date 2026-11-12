"""Run a real Nuclei scan against an ephemeral localhost-only practice server."""

import os
import shutil
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

import app as scanner


class LabHandler(BaseHTTPRequestHandler):
    secure_headers = False

    def do_GET(self):
        self.send_response(200)
        if LabHandler.secure_headers:
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'none'")
            self.send_header("X-Frame-Options", "DENY")
            self.send_header("Referrer-Policy", "no-referrer")
        self.end_headers()
        self.wfile.write(b"Local lab website")

    def log_message(self, *args):
        pass


def main():
    if not shutil.which(os.environ.get("NUCLEI_BIN", "nuclei")):
        raise RuntimeError("Install the official Nuclei CLI before running this check.")

    server = ThreadingHTTPServer(("127.0.0.1", 0), LabHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    target = "http://127.0.0.1:" + str(server.server_port)

    try:
        with tempfile.TemporaryDirectory() as directory:
            with patch.dict(os.environ, {"ALLOWED_ORIGINS": target}), patch.object(
                scanner, "RESULTS", Path(directory)
            ):
                client = scanner.app.test_client()

                response = client.post("/scan", data={"target": target})
                page = response.get_data(as_text=True)
                assert response.status_code == 200, (response.status_code, page)
                assert "x-frame-options" in page, "Expected missing-header finding"
                assert "<table>" in page, "Expected a findings table"
                print("PASS: real Nuclei detected missing headers")

                LabHandler.secure_headers = True
                response = client.post("/scan", data={"target": target})
                page = response.get_data(as_text=True)
                assert response.status_code == 200, (response.status_code, page)
                assert "No matches from the limited header template" in page, page
                print("PASS: correct no-findings result")

                response = client.post(
                    "/scan", data={"target": "https://example.com/"}
                )
                assert response.status_code == 400
                print("PASS: external target was blocked")
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
