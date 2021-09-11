# libLGTV_serial #
libLGTV_serial is a Python library to control LG TVs (or monitors with serial ports) via their serial (RS232) port. It aims to reduce the legwork needed to use this functionality on your TV - simply enter your TV model number and serial port and you're good to go!

## Requirements ##
- Python 2 or 3
- The pyserial module
    - Windows: http://pypi.python.org/pypi/pyserial
    - Debian/Ubuntu Linux: `sudo apt-get install python-serial`

## Supported Models/Operating Systems ##
- All OSes are supported. If you run into trouble please let me know. 
- A large number of LG TVs and monitors are supported -- a full list can be found on [the wiki](https://github.com/suan/libLGTV_serial/wiki/Supported-TV-Models). If your model isn't listed there, you can...
  - Modify the code and add it yourself. The code is pretty simple and straightforward. Look up the codes from the Owner's Manual on the included CD-ROM or from [LG's Support Website](http://www.lg.com/us/support/index.jsp) (Look for the section titled "EXTERNAL CONTROL THROUGH RS-232C"). If you added your model this way I would really appreciate a pull request! =)
  - OR
  - Create a feature request in [the Issues page](https://github.com/suan/libLGTV_serial/issues) or if you don't want to create a github account you can email me at yeosuanaik@gmail.com

## Usage ##
Currently I'm using the library through the LGTV.py script, which is invoked everytime certain buttons are pressed on my HDTV remote. The script is also a simple example of what the library can do and should be enough for most needs. (However, there's no reason you can't use the library in other ways, such as in a client-server configuration.)

The following assumes you will just be using the LGTV.py script as I am:

1. Download the files through the "ZIP" link near the top left of the page.
2. Change the model to match that of your TV
3. Change the serial port to match what your serial port is named. There is more info on this in the comments in the LGTV.py script.
3. You can then run the available_commands.py script to view all available commands for your TV (make sure to set the correct TV model here too).
4. To send one of those commands to the TV, all you have to do is invoke the script with the command, like this:

```
python LGTV.py --togglepower
```
### Toggles ###
Toggles are commands that flip between 2 states, such as power on/off. LGTV.py contains an example of how you can add toggles you want to use, namely:

```
tv.add_toggle('input', 'inputrgbpc', 'inputdigitalcable')
```
From then on, when you pass in '--toggleinput' to the script, it will switch between the 'inputrgbpc' and 'inputdigitalcable' to send to the TV. The 'togglepower' and 'togglemute' toggles are already included for your convenience.
### Debouncing ###
Sometimes a single remote button press is detected as many. For example, EventGhost generates over 10 events every time the power button on my HDTV remote is pressed. libLGTV_serial takes care of this for you, but you have to specify which commands you're having trouble with. In my case, it looks like

```
tv.debounce('togglepower')
```
This will make sure that all 'togglepower' calls within 0.5 seconds of the first one are ignored. If you want to use a duration other than 0.5 seconds, include it as a 2nd argument, for example:

```
tv.debounce('togglepower', 0.7)
```

### Getting TV Status ###
Every command sent to the `send()` method that ends with 'status' or 'level' will return a 2-digit bytestring represnting the status of the item. For some items, you'll need to refer to your model's manual to know what the status code means. For example, if `send('powerstatus')` returns `b'01'`, that means that the TV is currently on.

### Serial/RS232 Tips ###
Make sure you read your TV model's manual to see whether you need a "crossover/null-modem" or "straight-through" cable or adapter, and buy/use the correct one.

## TODO/Bugs/Contributions ##
I'll add more features as there's demand for them. Some that I forsee are:

- Covering more of the available commands
- Switching to a listening server model to improve performance

Either create a feature request on the issues page or email me if theres stuff you'd like added.

Same goes for any bugs you find, create an issue or email me.

And contributions are very much welcome!

## Credits ##
- [Jon Smith's blog post](http://www.thelazysysadmin.net/2009/05/rs232-control-lg-lcd-tv-mythtv/) which is the core of the library
- [Evan Fosmark](http://www.evanfosmark.com/2009/01/cross-platform-file-locking-support-in-python/) for filelock.py
