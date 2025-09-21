# PrettyTable Demo
# A simple demonstration of the PrettyTable library for creating formatted tables

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charamander"])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.align = 'c'
print(table)
