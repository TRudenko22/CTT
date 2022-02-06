from teaMenu import *
import random
import time
from rich import print as rprint

dctTea = random.choice(teas)

sTeaFormat = f"""
    Name: {dctTea['Name']}

    Tea Type: {dctTea['Style']}

    Tea Description: {dctTea['Desc']}
"""

rprint("\n[green]Welcome to the Crepes Tea House Tea Selector[/green]")
rprint("[cyan]Your Tea for this evening is:[/cyan]")
time.sleep(3)
print(sTeaFormat)

