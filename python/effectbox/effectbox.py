import asyncio
import websockets
from websockets import ConnectionClosed
import time
import json
from collections import namedtuple


class Effectbox:

    _client = None
    start_server = None

    def __init__(self, client):
        self._client = client
        self._effects = {}
        self._parameter_prototypes = {}
        self._parameters = {}

    def add_effect(self, effect, uid):

        if not hasattr(effect, "name"):
            effect.name = str(effect.__class__)

        self._effects[uid] = effect
        self._parameter_prototypes[uid] = effect.get_parameters()

        self._parameters[uid] = self.create_parameter_from_prototype(uid)

    def create_parameter_from_prototype(self, uid):

        param = self._parameter_prototypes[uid]["parameters"]
        parameter_class = namedtuple(uid, param.keys())

        foo = [value["value"] for key, value in param.items()]
        return parameter_class(*foo)

    def nested_set(self, origin, target):

        for key, value in origin.items():
            if isinstance(value, dict):
                self.nested_set(origin[key], target[key])
            else:
                target[key] = value

    def get_configuration(self):
        return self._parameter_prototypes

    def apply_configuration_dictionary(self, configuration):
        print("---- apply configuration dictionary")
        self.nested_set(configuration, self._parameter_prototypes)
        print(configuration)
        for key, value in configuration.items():
            print(self._parameters[key])
            self._parameters[key] = self.create_parameter_from_prototype(key)
            print(self._parameters[key])

    async def handler(self, web_socket, path):
        print("Connection opened for path {}".format(path))
        try:
            while True:

                command = await web_socket.recv()
                print("< {}".format(command))

                if command == "query":
                    response = json.dumps(self.get_configuration())
                else:
                    try:
                        configuration = json.loads(command)
                        self.apply_configuration_dictionary(configuration)
                        response = None
                    except ValueError:
                        response = "Command is not valid json"

                if response is not None:
                    await web_socket.send(response)

                print("> {}".format(response))
        except ConnectionClosed:
            print("Connection closed")

    async def effect_runner(self):
        t0 = time.time()

        while True:
            await asyncio.sleep(0.05)

            current_parameter = self._parameters["colorful_noise"]
            current_effect = self._effects["colorful_noise"].get_effect(current_parameter)
            self._client.map(current_effect, time.time() - t0)

    def start(self):
        self.start_server = websockets.serve(self.handler, '', 8765)

        asyncio.get_event_loop().run_until_complete(self.start_server)
        asyncio.wait(asyncio.ensure_future(self.effect_runner()))

        asyncio.get_event_loop().run_forever()
