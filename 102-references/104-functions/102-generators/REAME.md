# Generators

- *Generator functions*: are coded as normal **def** statements, but use **yield** statements to return results one at a time, suspending and resuming their statement between each.
- *Generator expressions*: are smilar to the list comprehensions orf the priors section, but they return an object the produces results on demand intead of building as a result list.

Because neither constructs a result list all at once, they save memory space and allow computation time to be split across result requests.