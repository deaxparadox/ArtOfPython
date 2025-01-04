import os
import sys
import argparse
from functools import partial

def arg_paraser() -> argparse.Namespace:
    arguments = argparse.ArgumentParser()
    arguments.add_argument(
        'PATH',
        help="Enter the path.",
        type=str
    )
    arguments.add_argument(
        "-v",
        "--verbose",
        default=True,
        action="store_true",
        help="increase output verbosity",
    )
    
    # subparsers
    # subparsers = arguments.add_subparsers(help="Subcommands")

    # dirs parsers
    # arg_paraser_dir = subparsers.add_parser(
    #     "dir", 
    #     help="Directory manipulation command.",
        
    # )
    # arg_paraser_dir.add_argument(
    #     "-n", 
    #     "--name", 
    #     help="Specify the directory name", 
    #     type=str
    # )

    return arguments.parse_args()

def replace(path: str, pat1: str, pat2: str) -> str:
    __cur = path.split(pat1)
    return pat2.join(__cur)

def lower_name(path: str) -> str:
    return path.lower()


def action(path, /, *args) -> None:
    """
    [
        lower_name,
        partial(replace, pat1=" ", pat2="-")
    ]
    """
    __act_list = []
    
    for f in args:
        if callable(f):
            __act_list.append(f)
    
    r = None
    for act in __act_list:
        if not r:
            r = act(path)
        r = act(r)  
    return r
    
    
    
def main() -> None:
    args = arg_paraser()
    # args.get
    print("checking %s" % args.PATH)
    
if __name__ == "__main__":
    main()