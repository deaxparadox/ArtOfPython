# Multiprocessing Library


`multiprocessing` is a package that supports spawning processes using an API similar to the `threading` module. 

The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. 

Due to this, the `multiprocessing` module allows the programmer to fully leverage multiple processors on a given machine. It runs on both POSIX and Windows.


- [Pool Object](101-pool-object.md)