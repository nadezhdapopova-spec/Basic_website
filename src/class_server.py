import urllib
from http.server import BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):
    """Класс, отвечающий за обработку входящих запросов от клиентов"""
    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.read_html()

    def do_POST(self):
        """Метод для обработки POST-запросов"""
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)
        # parsed_data = urllib.parse.parse_qs(post_data.decode("utf-8"))
        print(post_data)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

    def read_html(self):
        try:
            with open("dist/page_contacts.html", "r", encoding="utf-8") as file:
                content = file.read()
            self.wfile.write(bytes(content, "utf-8"))
        except FileNotFoundError:
            self.send_error(404, "File not found")
