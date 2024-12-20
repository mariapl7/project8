import http.server
from urllib.parse import parse_qs


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Обработчик HTTP-запросов, который отвечает на GET и POST запросы.
    """

    def do_GET(self):
        """
        Обрабатывает GET-запросы.
        Возвращает HTML-файл при запросе к /contacts и 404, если путь не найден.
        """
        if self.path == "/contacts":
            self.send_response(200)
            self.send_header("text/html; charset=utf-8")
            self.end_headers()
            with open("html/contacts.html", "r", encoding="utf-8") as file:
                content = file.read()  # Читаем содержимое файла как строку
                self.wfile.write(content.encode("utf-8"))  # Преобразуем строку в байты и отправляем
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        """
        Обрабатывает POST-запросы.
        Получает данные из запроса и возвращает ответ о успешной отправке.
        """
        content_length = int(self.headers['Content-Length'])  # Получаем длину данных
        post_data = self.rfile.read(content_length)  # Читаем данные из POST-запроса
        data = parse_qs(post_data.decode('utf-8'))  # Декодируем байты в строку

        print("Received data:", data)  # Печатаем полученные данные

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Данные успешно отправлены!")  # Отправляем ответ клиенту


def run_server(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """
    Запускает HTTP-сервер.

    :param server_class: Класс сервера, обычно http.server.HTTPServer.
    :param handler_class: Класс обработчика запросов, по умолчанию - SimpleHTTPRequestHandler.
    :param port: Порт, на котором будет запущен сервер (по умолчанию 8000).
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)  # Передаем правильный тип
    print(f"Сервер запущен на порту {port}")
    httpd.serve_forever()  # Запускаем сервер


if __name__ == "__main__":
    run_server()  # Запускаем сервер
