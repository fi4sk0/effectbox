import opc
import time
import colorsys
from noise import pnoise3
import numpy as np

from effectbox.effectbox import Effectbox

client = opc.Client("rpi3:7890", verbose=False, long_connection=True)

if client.can_connect():
    print("Yay, there is a server")
else:
    print("No server present")

number_of_leds = 64*4
toggle = False
client.set_interpolation(True)

client.led_strip(0,  12, (11., 2.), (11., 24.))
client.led_strip(12, 12, (9., 23.), (9., 1))
client.led_strip(24, 12, (7., 2.), (7., 24))

client.led_strip(64, 12, (5., 23.), (5., 1.))
client.led_strip(76, 12, (3., 2.), (3., 24.))
client.led_strip(88, 12, (1., 23.), (1., 1.))

client.led_strip(128, 12, (-1., 2.), (-1., 24.))
client.led_strip(140, 12, (-3., 23.), (-3., 1.))
client.led_strip(152, 12, (-5., 2.), (-5., 24.))

client.led_strip(192, 12, (-7., 23.), (-7., 1.))
client.led_strip(204, 12, (-9., 2.), (-9., 24.))
client.led_strip(216, 12, (-11., 23.), (-11., 1.))

client.led_strip(228, 6, (0., 26.), (0., 38.))

t0 = time.time()

with open("./layout.json", "w") as f:
    f.write(client.to_dict())


class ColorfulNoise(object):

    @classmethod
    def get_parameters(cls):

        return {"name": "Colorful Noise",
                "description": "A wonderful cloud of color",
                "parameters": {
                    "time_warp": {
                        "min": 1,
                        "max": 10,
                        "value": 5},
                    "y_stretch": {
                        "min": 0,
                        "max": 0.05,
                        "value": 0.03},
                    "x_stretch": {
                        "min": 0,
                        "max": 0.05,
                        "value": 0.03},
                    "brightness": {
                        "min": 0,
                        "max": 1,
                        "value": 1.0}
                    }
                }

    @classmethod
    def get_effect(cls, p):

        def effect(pos, t):

            x = pos[0]
            y = pos[1]

            if np.all(pos == np.zeros((1, 3))):
                return 0, 0, 0.2
            else:
                hue = pnoise3(x*p.x_stretch, y*p.y_stretch, t/p.time_warp, 3) + 2.5
                return colorsys.hsv_to_rgb(hue, 1, p.brightness)

        return effect


class SingleColor(object):

    @classmethod
    def get_parameters(cls):

        return {"name": "Single Color",
                "description": "Just a plain color",
                "parameters": {
                    "hue": {
                        "min": 1.,
                        "max": 2.,
                        "value": 1.},
                    "brightness": {
                        "min": 0,
                        "max": 1,
                        "value": 0.8}
                    }
                }

    @classmethod
    def get_effect(cls, p):

        def effect(pos, t):
            if np.all(pos == np.zeros((1, 3))):
                return 0, 0, 0.2
            else:
                return colorsys.hsv_to_rgb(p.hue, 1, p.brightness)

        return effect

colorful_noise = ColorfulNoise()

my_box = Effectbox(client)

my_box.add_effect(colorful_noise, "colorful_noise")
my_box.add_effect(SingleColor(), "single_color")
my_box.start()
