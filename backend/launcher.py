import threading
import time
import webbrowser

import uvicorn

from app.main import app


HOST = "127.0.0.1"
PORT = 8000


def abrir_navegador():
    time.sleep(2)

    webbrowser.open(
        f"http://{HOST}:{PORT}"
    )


if __name__ == "__main__":

    threading.Thread(
        target=abrir_navegador,
        daemon=True
    ).start()

    config = uvicorn.Config(
        app,
        host=HOST,
        port=PORT,
        reload=False,
        log_config=None
    )

    server = uvicorn.Server(config)

    server.run()