import time

from rich.live import Live
from rich.table import Table

from rich import print
from rich.layout import Layout

layout = Layout()



table = Table()
table.add_column("Row ID")


layout.split_column(
    Layout(name="upper"),
    Layout(table)
)

with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
    for row in range(12):
        time.sleep(0.4)  # arbitrary delay
        # update the renderable internally
        table.add_row(f"{row} {row} [red]ERROR")