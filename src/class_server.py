from http.server import BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):
    """Класс, отвечающий за обработку входящих запросов от клиентов"""
    def do_GET(self) -> None:
        """Метод для обработки входящих GET-запросов"""
        self.send_response(200)

        filename = "/page_contacts.html"

        if self.path[-4:] == '.css':
            self.send_header('Content-type', 'text/css')
            filename = self.path
        else:
            self.send_header("Content-type", "text/html")
        self.end_headers()
        self.read_content(filename)

    def do_POST(self) -> None:
        """Метод для обработки POST-запросов"""
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)
        print(post_data)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

    def read_content(self, file_name: str) -> None:
        """Метод для чтения содержимого файла и отправки его в ответ клиенту"""
        try:
            content_path = "dist" + file_name
            with open(content_path, "r", encoding="utf-8") as file:
                content = file.read()
            self.wfile.write(bytes(content, "utf-8"))
        except FileNotFoundError:
            self.send_error(404, "File not found")
