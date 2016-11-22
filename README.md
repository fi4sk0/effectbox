# effectbox
A python implementation of an effect runner intended (but not limited) to be used on a RPi, Fadecandy, WS2811 Software/Hardware stack. 

This project is based on the magnificent [Fadecandy](https://github.com/scanlime/fadecandy) by the infamous [scanlime](http://scanlime.org) and [openpixelcontrol.org](http://openpixelcontrol.org).

# Problem description
In case you ever tried to create an effect for a LED-pixel based project that actually not only just worked but also looked nice, you probably did something like this
```
Code an algorithm -> run -> tweak -> run -> (tweak -> run)**inf 
```
To be more efficient and getting a live view of what tweaking the parameters actually does, _effectbox_ might be able to help you. 

# Sample
```python
# Create an OPC client
client = opc.Client("rpi3:7890", verbose=False, long_connection=True)

# Configure client to you physical LED layout
# This creates positions for a pyhsical LED strip of 12 LEDs starting at index 0 for the positions x = 0, y=1...12
client.led_strip(0,  12, (0., 1.), (0., 12.))

# Create an effect class:
class SingleColor(object):

    @classmethod
    def get_parameters(cls):

        # Define meta information. Note how parameters are defined here.
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

        # Create an effect relying on the parameters you defined in get_parameters()
        def effect(pos, t):
            return colorsys.hsv_to_rgb(p.hue, 1, p.brightness)

        return effect

my_box = Effectbox(client)
my_box.add_effect(SingleColor(), "single_color")
my_box.start()
```
A webapp included in this repository connects to the effect runner using WebSockets and creates a site representing the parameters of the effect:

![Webapp Photo](https://raw.github.com/fi4sk0/effectbox/master/doc/webapp-screen.png)
