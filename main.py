from teaMenu import *
import random

dctTea = random.choice(teas)

sTeaFormat = f"""
    Name: {dctTea['Name']}

    Tea Type: {dctTea['Style']}

    Tea Description: {dctTea['Desc']}
"""

print("\nWelcome to the Crepes Tea House Tea Selector")
print("Your Tea for this evening is:")
print(sTeaFormat)

