import asyncio
import websockets
import json

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        # while True:
        # name = input("What's your name? ")

        # if name == "quit":
        #     break

        configuration = {"noise": {"x_stretch": 0.1}}

        data = json.dumps(configuration)

        print(json.loads(data))

        await websocket.send(data)
        print("> {}".format(data))

        greeting = await websocket.recv()
        print("< {}".format(greeting))

        print("Leaving loop")


asyncio.get_event_loop().run_until_complete(hello())