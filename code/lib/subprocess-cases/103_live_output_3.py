import subprocess
import argparse
from time import sleep

def stream_process(process):
    go = process.poll() is None
    for line in process.stdout:
        print(line.decode('utf8'), end="")
    return go

def main():
    process = subprocess.Popen(["bash", "count10.sh"],   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while stream_process(process):
        sleep(0)
    return False

if __name__ == "__main__":
    main()
