
import logging
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from subprocess import PIPE, CalledProcessError, CompletedProcess, Popen


def stream_command(
    args,
    *,
    stdout_handler=logging.info,
    stderr_handler=logging.error,
    check=True,
    text=True,
    stdout=PIPE,
    stderr=PIPE,
    **kwargs,
):
    """Mimic subprocess.run, while processing the command output in real time."""
    with (
        Popen(args, text=text, stdout=stdout, stderr=stderr, **kwargs) as process,
        ThreadPoolExecutor(2) as pool,  # two threads to handle the (live) streams separately
    ):
        exhaust = partial(deque, maxlen=0)  # collections recipe: exhaust an iterable at C-speed
        exhaust_async = partial(pool.submit, exhaust)  # exhaust non-blocking in a background thread
        exhaust_async(stdout_handler(line[:-1]) for line in process.stdout)
        exhaust_async(stderr_handler(line[:-1]) for line in process.stderr)
    retcode = process.poll()  # block until both iterables are exhausted (process finished)
    if check and retcode:
        raise CalledProcessError(retcode, process.args)
    return CompletedProcess(process.args, retcode)

# stream_command(["echo", "test"], stdout_handler=print, stderr_handler=print)

# outs, errs = [], []
def stdout_handler(line):
    # outs.append(line)
    print(line)
def stderr_handler(line):
    # errs.append(line)
    print(line)


if __name__ == "__main__":
    stream_command(
        ["bash", "search_pdf.sh"],
        stdout_handler=stdout_handler,
        stderr_handler=stderr_handler,
    )
    # test
    # print(outs)
    # ['test']
