import asyncio

import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = (
            f"1 Сообщение пользователя: {message}\n",
            f"2 Сообщение пользователя: {message}\n",
            f"3 Сообщение пользователя: {message}\n",
            f"4 Сообщение пользователя: {message}\n",
            f"5 Сообщение пользователя: {message}\n"
        )
        await websocket.send(response)


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())
