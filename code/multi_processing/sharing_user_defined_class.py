import multiprocessing
from multiprocessing import shared_memory
import os
import pickle

class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"PPID: {os.getppid()}, PID: {os.getpid()}, Value: {self.value}")

def worker(shm_name):
    # Access the shared memory
    existing_shm = shared_memory.SharedMemory(name=shm_name)
    # Deserialize the object
    obj = pickle.loads(existing_shm.buf[:])
    obj.display()
    existing_shm.close()

if __name__ == '__main__':
    # Create an instance of MyClass
    obj = MyClass(42)
    # Serialize the object
    serialized_obj = pickle.dumps(obj)
    
    # Create shared memory
    shm = shared_memory.SharedMemory(create=True, size=len(serialized_obj))
    # Write serialized data into shared memory
    shm.buf[:len(serialized_obj)] = serialized_obj

    # Start a new process
    p = multiprocessing.Process(target=worker, args=(shm.name,))
    p.start()
    p.join()
    
    obj.display()

    # Clean up shared memory
    shm.close()
    shm.unlink()
