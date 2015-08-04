EventDispatcher.py
==================

A very simple event dispatcher.

Usage
-----

```py
# Import module
from eventdispatcher import EventDispatcher

# Create a dispatcher
dispatcher = EventDispatcher()

# Add an event listener
def listener(e):
    print(e['msg'])

dispatcher.listen('world.ready', listener)

# Add a second event listener
listener_id = dispatcher.listen(
    'world.ready',                      # The event to listen
    lambda: print("I want to die."),    # The event listener
    -1 # Execute it first, let's put a lower priority than the default one (0)
)

# Well... don't make your visitor sad
dispatcher.detach(listener_id)

# Ok, trigger your event
dispatcher.dispatch('world.ready', { 'msg': 'Hello World!' })

# Enjoy!
```

? Paste this code in the console interpreter and let's play!

Links
-----

The same event dispatcher is written in Javascript:
[zzortell/eventdispatcher.js](https://github.com/zzortell/eventdispatcher.js/).

License
-------

This code is under the MIT License.
For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
