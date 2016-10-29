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

Extra feature: Listen all events
--------------------------------

The event name `all` is a reserved keyword. It makes you able to listen all
emitted events:

```py
from eventdispatcher import EventDispatcher
dispatcher = EventDispatcher()

# Register a listener for all emitted events using the keyword 'all'
dispatcher.listen('all', lambda e: print(e))

# Then, the listener will be called on every trigerring
dispatcher.dispatch('world.hi', 'Hello')
dispatcher.dispatch('world.bye', 'Goodbye')
```

Extra feature: Propagation
--------------------------

If set, dispatching an event 'grandpa.parent.event' also dispatch its parents
'grandpa.parent' and 'grandpa'.

For example:

```py
from eventdispatcher import EventDispatcher

# First, set the propagation
dispatcher = EventDispatcher(propagation=True)

# Register a listener for all the events trigerred by the component 'game'
def game_listener(e):
    print("An event happened!")

dispatcher.listen('game', game_listener)

# Register a second listener for the specific event 'game.jump'
def onJump(e):
    print("Jump on ({},{})!".format(e['x'], e['y']))

dispatcher.listen('game.jump', onJump)

# Dispatch 'game.jump' and both listeners will be called!
dispatcher.dispatch('game.jump', { 'x': 7, 'y': 42 })
```

You can also set or unset propagation for each dispatching:

```py
dispatcher = EventDispatcher()

dispatcher.dispatch('parent.child', 'event', True)
```

Extra feature: Decorator
------------------------

The event dispatcher also provide a decorator for listening events. e.g.:

```py
from eventdispatcher import EventDispatcher
dispatcher = EventDispatcher()

# Register a listener via the decorator
@dispatcher.on('processus.done')
def logger(e):
    print(e)

dispatcher.dispatch('processus.done', 'Hello')
```

Links
-----

The same event dispatcher is written in Javascript:
[zzortell/eventdispatcher.js](https://github.com/zzortell/eventdispatcher.js/).

License
-------

This code is under the MIT License.
For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
