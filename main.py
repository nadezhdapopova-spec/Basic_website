import os
from http.server import HTTPServer

from dotenv import load_dotenv

from src.class_server import Server

load_dotenv()


def main() -> None:
    """Инициализация, запуск и остановка веб-сервера"""
    host_name = os.getenv("HOST_NAME", "127.0.0.1")
    server_port = int(os.getenv("SERVER_PORT", 8080))
    web_server = HTTPServer((host_name, server_port), Server)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
    web_server.server_close()
    print("Server stopped.")


main()
