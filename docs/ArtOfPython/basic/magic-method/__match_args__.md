# `__match_args__` 

It is possible to manually specify the ordering of the attributes allowing positional matching, like in this alternative definition:

```py
class Click:
    __match_args__ = ("position", "button")
    def __init__(self, pos, btn):
        self.position = pos
        self.button = btn
        ...
```