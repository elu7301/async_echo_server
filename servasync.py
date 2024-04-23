import asyncio

HOST = '127.0.0.1'
PORT = 12345


async def handle_client(reader, writer):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        writer.write(data)
        await writer.drain()
    writer.close()


async def echo_server():
    server = await asyncio.start_server(handle_client, HOST, PORT)

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(echo_server())
