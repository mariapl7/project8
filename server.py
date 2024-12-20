import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/contacts":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("html/contacts.html", "r", encoding="utf-8") as file:
                self.wfile.write(file.read().encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode('utf-8'))

        print("Received data:", data)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Данные успешно отправлены!")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Сервер запущен на порту {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
