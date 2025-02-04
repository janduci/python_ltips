names = ["Alex", "Isadora", "Catarina", "Luci", "Garcia", "Rodrigo", "Jose", "Luis", "Maria", "Joao", "Bruno", "Bia"]

print(sorted(names, key=lambda name: name.count("i")))

print(list(filter(lambda name: name[0].lower() == "b", names)))

print(list(map(lambda name: "Hello " + name, names)))

