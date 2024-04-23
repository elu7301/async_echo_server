import asyncio

HOST = '127.0.0.1'
PORT = 12345


async def connect_to_server():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    return reader, writer


async def send_message(reader, writer):
    message = input('Введите сообщение для отправки: ')
    writer.write(message.encode())
    await writer.drain()
    response = await reader.read(1024)
    print('Получено:', response.decode())


async def main():
    reader, writer = await connect_to_server()

    while True:
        await send_message(reader, writer)


if __name__ == "__main__":
    asyncio.run(main())
