# libLGTV_serial with MQTT support #
Modified version of [libLGTV_serial from suan](https://github.com/suan/libLGTV_serial). Added service for listening for commands via MQTT and added various codes to "LE5300_etc".

For more information take a look at the [README of the original library](https://github.com/suan/libLGTV_serial/blob/master/README.md).

libLGTV_serial is a Python library to control LG TVs (or monitors with serial ports) via their serial (RS232) port. It aims to reduce the legwork needed to use this functionality on your TV - simply enter your TV model number and serial port and you're good to go!


## Requirements ##
- Python 3 *(I've only tested it with Python 3)*
- The [pyserial](https://pypi.org/project/pyserial/) module
- [paho-mqtt](https://pypi.org/project/paho-mqtt/) for MQTT support


## Usage ##

- Move `config_example.ini` to `config.ini` and configure your tv model, serial port and MQTT settings.
- Create a python virtualenv
- Install the required packages (inside your virtualenv) via `pip install -r requirements`
- To use `LGTV_service.py` as a systemd service, copy or move `lgtv_serial.service` to `/etc/systemd/system/` and modify it to your needs.

Now start the systemd service or `LGTV_service.py`.

You can now send commands to the MQTT topic that you've configured in the `config.ini` file. As the payload you use the commands that you can find at the top of `libLGTV_serial.py`.

Examples for the payload:

```
energysaving_off
```

You're also able to send multiple commands inside the payload. They need to be separated with commas and are send to the tv with an interval of 0.5 seconds:

```
r_menu, r_up, r_left, r_ok, r_up, r_up, r_ok, r_exit
```

## Credits ##
- [suans original library](https://github.com/suan/libLGTV_serial)
- [Jon Smith's blog post](http://www.thelazysysadmin.net/2009/05/rs232-control-lg-lcd-tv-mythtv/) which is the core of the library
- [Evan Fosmark](http://www.evanfosmark.com/2009/01/cross-platform-file-locking-support-in-python/) for filelock.py