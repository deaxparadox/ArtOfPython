#! /usr/bin/env python3

import click
import sys

@click.command()
@click.option(
    "--interpreter", default=True,
    help="Show the current interpretor path."
)
def hello(interpreter):
    """Simple program to check the default interpreter."""
        
    if interpreter:
        print(sys.executable)
        

if __name__ == '__main__':
    hello()