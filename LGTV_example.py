# Sample Windows script which uses the libLGTV_serial library
# Can be called, for example by doing "python LGTV.py --poweroff"
#

import sys
import configparser

from libLGTV_serial import LGTV


# Read settings
config = configparser.ConfigParser()
config.read('config.ini')
settings = config['settings']

model = settings['Model']
serial_port = settings['SerialPort']

# Verify passed command
if len(sys.argv) != 2: 
    print('Usage: {0} <command>'.format(sys.argv[0]))
    print('Example: {0} --togglepower'.format(sys.argv[0]))
    sys.exit(1)

tv = LGTV(model, serial_port)

# Example of adding a custom toggle command. Passing in '--toggleinput'
# will toggle between 'inputrgbpc' and 'inputdigitalcable'
tv.add_toggle('input', 'inputrgbpc', 'inputdigitalcable')

# Sometimes a single remote button press is detected as many. By debouncing a
# command, we make sure its only called once per button press.
tv.debounce('togglepower')

# Finally, send the command
# .send() Returns nothing on failure, 2-digit bytecode for status commands,
# and True for other commands
print(tv.send(sys.argv[1].lstrip("--")))
