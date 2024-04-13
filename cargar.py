import json

file_name = "data.json"

with open(file_name, "r") as data:
    datos = json.load(data)
    #print("\nIP: " + datos["ip"] + "\nSO: " + datos["so"] )
    print(datos["info"][0])

# template string python
    


"""
for i in datos:
    print(datos[i])
"""
