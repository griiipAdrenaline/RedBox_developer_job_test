from consumer.server import Server
from producer.client import Client

import traceback


if __name__ == '__main__':
    try:
        s = Server()
        c = Client()

        s.join()
    except Exception as exc:
        traceback.print_exc()
    finally:
        s.stop()
        c.stop()

