
## Why Decorators?  

Decorators provide an explicit syntax for such tasks, which makes intent clearer, can minimize augmentation code redundancy, and may help ensure correct API usage:

- Decorators have a very *explicit* syntax, which makes them easier to spot them helper function calls that may be arbitrary far-removed from the subject functions or classes.

- Decoratoras are applied *once*, when the subject function or class is defined; it's not necessary to add extra code to every call to the class or function, which may have to be changed in the future.

- Because of both of the prior points, decorators make it less likely that a user of an API will *forget* to augment a function or class according to API requirements. 

In other words, beyond their technical model, decorators offer some advantages in terms of both code maintenance and consistency. Moreover, as structuring tools, decorators naturally foster encapsulation of code, which reduces redundancy and makes future changes easier.

Decorators do have some potential *drawbacks*, too—when they insert wrapper logic, they can alter the types of the decorated objects, and they may incur extra calls when used as call or interface proxies. On the other hand, the same considerations apply to any technique that adds wrapping logic to objects.
