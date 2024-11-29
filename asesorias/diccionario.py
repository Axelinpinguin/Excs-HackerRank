persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print()
print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print()
print(persona.values())   # Imprime dict_values(["Juan", 25, "Madrid"])
print()  
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])
print()
persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}