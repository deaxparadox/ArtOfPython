# `match` Statements

A `match` statement takes an expression and compares its value to successive patterns as one or more case blocks. 

```python
status = 200

match status:
    case 200:
        print("Successfull")
    case 300:
        print("Redirected")
    case _:
        print("Unknown!")

# output
SuccessFull
```

- You can combine several literals in a single pattern using `|` ("or"):

```python
status = 302

match status:
    case 200:
        print("Successfull")
    case 300 | 301 | 302:
        print("Redirected")
    case _:
        print("Unknown!")
```

## Examples

There are more usefull cases where we can use `match` statement. Let's write a simple program.

In our program user enters text commands to interact with fictional world and recevies text descriptors of what happens. Commands will be simplified forms of natural language like `get sword`, `attack dragon`, `go north`, `enter shop` or `buy cheese`.

Your main loop will need to get input from the user and split it into words, let’s say a list of strings like this:

```py
command = input("What are you doing next? ")
# analyze the result of command.split()
```

The next step is to interpret the words. Most of our commands will have two words: an action and an object. 

```
[action, obj] = command.split()
... # interpret action, obj
```

The match statement evaluates the **“subject”** (the value after the `match` keyword), and checks it against the **pattern** (the code next to `case`). A pattern is able to do two different things:

- Verify that the subject has certain structure. In your case, the `[action, obj]` pattern matches any sequence of exactly two elements. This is called **matching**.
- It will bind some names in the pattern to component elements of your subject. In this case, if the list has two elements, it will bind `action = subject[0]` and `obj = subject[1]`.

### Matching multiple patterns


```py
match command.split():
    case [action]:
        print("interpret single-verb action ")
    case [action, obj]:
        print("interpret action, object")
```

let's run our program:

```sh
$
$ python match.py 
What are you doing next? attack
interpret single-verb action 
$
$ python match.py 
What are you doing next? attack dragon
interpret action, object
```

when we specific action only we get *"interpret single-verb-action"* and when we specify action and object we get *'interpret action, object"*.


### Matching specific values

A pattern like `["get", obj]` will match only 2-element sequences that have a first element equal to "get". It will also bind `obj = subject[1]`.

```py
match command.split():
        case ['quit']:
            print("Goodbye!")
        case ['look']:
            print("Looking at current room.")
        case ['get', obj]:
            print("Get user in current room.")
        case ['get', direction]:
            print("Go in that direction")
```

### Matching multiple values

A player may be able to drop multiple items by using a series of commands `drop key`, `drop sword`, `drop cheese`. This interface might be cumbersome, and you might like to allow dropping multiple items in a single command, like `drop key sword cheese`.`

```py
def multiple_values(): 
    match command.split():
        case ["drop", *objects]:
            print(objects)
```

This will match any sequences having “drop” as its first elements. All remaining elements will be captured in a `list` object which will be bound to the `objects` variable.

The `default` case is the universal case if all `case` fail.

```output
What are you doing next? get west south north
Universal case
```

```output 
What are you doing next? drop west south north
['west', 'south', 'north']
```

### Adding a wildcard

You may want to print an error message saying that the command wasn’t recognized when all the patterns fail.

```py
match command.split():
    case ["quit"]: ... # Code omitted for brevity
    case ["go", direction]: ...
    case ["drop", *objects]: ...
    ... # Other cases
    case _:
        print(f"Sorry, I couldn't understand {command!r}")
```

This special pattern which is written `_` (and called wildcard) always matches but it doesn’t bind any variables.

### Or pattersn

The `|` symbol in patterns combines them as alternatives. You could for example write:

```py
match command.split():
    ... # Other cases
    case ["north"] | ["go", "north"]:
        current_room = current_room.neighbor("north")
    case ["get", obj] | ["pick", "up", obj] | ["pick", obj, "up"]:
        ... # Code for picking up the given object
```

```py
    match command.split():
        case ['north'] | ['go', 'north']:
            print("North direction")
        case ["get", obj] | ["pick", "up", obj] | ["pick", obj, "up"]:
            print("Action {}".format(obj))
        case _:
            print("Unable to proceed")
```

```bash
$ python match.py 
What are you doing next? go north
North direction

$ python match.py 
What are you doing next? north
North direction

$ python match.py 
What are you doing next? get something
Action something

$ python match.py 
What are you doing next? pick up the box
Unable to proceed

$ python match.py 
What are you doing next? pick up box
Action box

$ python match.py 
What are you doing next? pick box up
Action box

$ python match.py 
What are you doing next? get box
Action box
```


### Capturing matched sub-patterns

We can specifies multiple direction using `|` operator after "go":

```py
match command.split():
    case ["go", ("north" | "south" | "east" | "west")]:
        current_room = current_room.neighbor(...)
        # how do I know which direction to go?
```

What if we want to get that direction and want to use in below:

```py
match command.split():
    case ["go", ("north" | "south" | "east" | "west") as direction]:
        current_room = current_room.neighbor(direction)
```

```py
direction: list[str] = ['north', 'south', 'east', 'west']

match command.split():
    # if any of direction is given: 'north' or 'south' or 'east' or 'west'
    # and then we can bind that direction to `i` and use it in flow code.
    case ['go', direction as i] :
        print("we can go in {}".format(i))
    
    # same as above, if either action is given run following code
    case ['get', ('down'| 'up')]:
        print("Action specified")

    # if all direction are given: 'go south north west east'
    case ['go', *direction]:
        print("We can go in any direction.")

    # fail safe: if all cases fail
    case _:
        print("Unable to procceed.")
```

```bash
$ python match.py 
What are you doing next? go south
we can go in south

$ python match.py 
What are you doing next? go north
we can go in north

$ python match.py 
What are you doing next? go east
we can go in east

$ python match.py 
What are you doing next? go north south east west
We can go in any direction.
```


### Adding condition to patterns

Let’s say that you would actually like to allow a “go” command only in a restricted set of directions based on the possible exits from the current_room.

```py
match command.split():
    case ["go", direction] if direction in current_room.exits:
        current_room = current_room.neighbor(direction)
    case ["go", _]:
        print("Sorry, you can't go that way")
```


### Adding a UI: Matching objects

Your adventure is becoming a success and you have been asked to implement a graphical interface. Your UI toolkit of choice allows you to write an event loop where you can get a new event object by calling `event.get()`. The resulting object can have different type and attributes according to the user action, for example:

- A `KeyPress` object is generated when the user presses a key. It has a `key_name` attribute with the name of the key pressed, and some other attributes regarding modifiers.
- A `Click` object is generated when the user clicks the mouse. It has an attribute `position` with the coordinates of the pointer.
- A `Quit` object is generated when the user clicks on the close button for the game window.

Rather than writing multiple `isinstance()` checks, you can use patterns to recognize different kinds of objects, and also apply patterns to its attributes:


```py
match event.get():
    case Click(position=(x, y)):
        handle_click_at(x, y)
    case KeyPress(key_name="Q") | Quit():
        game.quit()
    case KeyPress(key_name="up arrow"):
        game.go_north()
    ...
    case KeyPress():
        pass # Ignore other keystrokes
    case other_event:
        raise ValueError(f"Unrecognized event: {other_event}")
```

A pattern like `Click(position=(x, y))` only matches if the type of the event is a subclass of the `Click` class. It will also require that the event has a `position` attribute that matches the `(x, y)` pattern. If there’s a match, the locals `x` and `y` will get the expected values.


A pattern like `KeyPress()`, with no arguments will match any object which is an instance of the `KeyPress` class. Only the attributes you specify in the pattern are matched, and any other attributes are ignored.


### Matching positional attributes

