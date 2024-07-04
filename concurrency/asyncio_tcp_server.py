import sys
import asyncio

PROMPT = b'?>'


def handle_queries(reader, writer):
    pass


def main():
    loop = asyncio.get_event_loop()
    server_coro = asyncio.start_server(handle_queries, "localhost", "7899")
    server = loop.run_until_complete(server_coro)

    host = server.sockets[0].getsockname()
    print("serving on {}. Hit CTRL-C to stop".format(host))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    print("Server Shutting down")
    server.close()
    loop.run_until_complete(server.wait_closed())


if  __name__ == "__main__":
    main()
