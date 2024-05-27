# 
# Working: getting the live output and writing to file.
# 

import subprocess
import shlex

def output_live(process: subprocess.Popen) -> None:
    # Poll process.stdout to show stdout live
    while True:
        __output = process.stdout.readline()
        if process.poll() is not None:
            break
        if __output:
            print(__output.strip().decode('utf-8'))
        rc = process.poll()    
    
def output_live_and_file(process: subprocess.Popen):
    # Poll process.stdout to show stdout live
    with open("log.txt", "a") as f:
        while True:
            __output = process.stdout.readline()
            if process.poll() is not None:
                break
            if __output:
                message = __output.strip().decode('utf-8')
                print(message)
                f.write(message+"\n")
            rc = process.poll()    
    

# invoke process
process = subprocess.Popen(["ping", "127.0.0.1", "-t"],shell=False,stdout=subprocess.PIPE)

output_live_and_file(process)