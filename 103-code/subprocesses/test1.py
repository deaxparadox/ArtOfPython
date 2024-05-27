# 
# Working: getting the live output
# 

import subprocess
import shlex

def output(process: subprocess.Popen) -> None:
    # Poll process.stdout to show stdout live
    while True:
        __output = process.stdout.readline()
        if process.poll() is not None:
            break
        if __output:
            print(__output.strip().decode('utf-8'))
        rc = process.poll()    

# invoke process
process = subprocess.Popen(["ping", "127.0.0.1", "-t"], shell=False, stdout=subprocess.PIPE)

output(process)