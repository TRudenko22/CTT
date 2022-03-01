from teaMenu import *
import random
import time
from rich import print as rprint
dctTea = random.choice(teas)

sTeaFormat = f"""
   [yellow] Name: [/yellow][green]{dctTea['Name']} [/green]
   [yellow] Tea Type:[/yellow] [green]{dctTea['Style']} [/green]
   [yellow] Tea Description:[/yellow][green] {dctTea['Desc']} [/green]
"""

rprint("\n[green]Welcome to the Crepes Tea House Tea Selector[/green]")
rprint("[green]Your Tea for this evening is:[/green]")
time.sleep(3)
rprint(sTeaFormat)
