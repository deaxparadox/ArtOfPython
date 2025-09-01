import cupy as cp
import multiprocessing
import time
import os

def gpu_worker(duration=30):
    print("[GPU] Starting load for", duration, "seconds.")
    start_time = time.time()
    size = 16384  # Large enough to stress GPU but not max out memory
    a = cp.random.rand(size, size, dtype=cp.float32)
    b = cp.random.rand(size, size, dtype=cp.float32)

    while time.time() - start_time < duration:
        result = cp.dot(a, b)
        cp.cuda.runtime.deviceSynchronize()

    print("[GPU] Finished.")

def cpu_worker(duration=30):
    print(f"[CPU {os.getpid()}] Starting load for {duration} seconds.")
    end_time = time.time() + duration
    while time.time() < end_time:
        _ = sum(i*i for i in range(10000))  # simple CPU load
    print(f"[CPU {os.getpid()}] Finished.")

def spawn_cpu_workers(percent=0.5, duration=30):
    total_cores = multiprocessing.cpu_count()
    cores_to_use = max(1, int(total_cores * percent))
    print(f"[CPU] Spawning {cores_to_use} of {total_cores} cores (~{int(percent*100)}% load)")

    processes = []
    for _ in range(cores_to_use):
        p = multiprocessing.Process(target=cpu_worker, args=(duration,))
        p.start()
        processes.append(p)
    return processes

if __name__ == "__main__":
    duration = 30  # seconds
    print("[Main] Starting 50% CPU and 50% GPU stress test...")

    # Start CPU stress
    cpu_processes = spawn_cpu_workers(percent=0.5, duration=duration)

    # Start GPU load (in main process)
    gpu_worker(duration)

    # Wait for CPU processes to finish
    for p in cpu_processes:
        p.join()

    print("[Main] Stress test complete.")
