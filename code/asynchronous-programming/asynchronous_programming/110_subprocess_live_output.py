import asyncio
import subprocess
from time import sleep

async def stream_process(process):
    go = process.poll() is None
    for line in process.stdout:
        print(line.decode('utf8'), end="")
    return go

async def main():
    process = asyncio.create_subprocess_shell(
        "flask --app simple_crud_api run --debug --reload".split(" "),
        stdout=asyncio.subprocess.PIPE, 
        stderr=asyncio.subprocess.STDOUT
        )
    while await stream_process(process):
        sleep(0)
    return False

    
    
if __name__ == "__main__":
    asyncio.run(main)