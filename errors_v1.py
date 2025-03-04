import sys 
import os

# Tratando erros com LBYL
# LBYL - Look before you leap
# Olhe antes de pular

if os.path.exists("names.txt"):
    print("O arquivo existe")
    names = open("names.txt").readlines()
    
else:
    print("[Error] file not found")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)

