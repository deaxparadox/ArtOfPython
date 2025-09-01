import cupy as cp
import time

def gpu_worker(duration=30):
    print("[GPU] Starting load for", duration, "seconds.")
    start_time = time.time()

    # Allocate matrices to use ~2-3 GB of GPU memory
    size = 16384  # Tune this if needed
    a = cp.random.rand(size, size, dtype=cp.float32)
    b = cp.random.rand(size, size, dtype=cp.float32)

    while time.time() - start_time < duration:
        cp.dot(a, b)  # Heavy GPU compute
        cp.cuda.runtime.deviceSynchronize()  # Wait for GPU to complete

    print("[GPU] Done.")

def gpu_heavy_task(duration=30):
    print("[GPU] Stressing GPU for", duration, "seconds...")
    size = 16384  # Large matrices to use ~2.5-3 GB memory
    a = cp.random.rand(size, size, dtype=cp.float32)
    b = cp.random.rand(size, size, dtype=cp.float32)

    start = time.time()
    while time.time() - start < duration:
        cp.dot(a, b)  # triggers CUDA compute
        cp.dot(b, a)  # reverse to ensure varied compute
        cp.cuda.runtime.deviceSynchronize()

    print("[GPU] Done.")

gpu_heavy_task()
