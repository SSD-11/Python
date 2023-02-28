# CORREO ELECTRONICO
import re

correo = "samuserna2005@gmail.com"
pattern = re.compile(r'^[a-zA-Z0-9_-]+\w[.]?[a-z0-9]+[@]\w+[.]\w{2,3}\w$')
result = pattern.search(correo)
if result:
    print("Correo Valido")
else:
    print("Correo Invalido")

# CORREO INSTITUCIONAL
import re

correo = "samuel.sernadelgado@inemjose.edu.co"
pattern = re.compile(r'^[a-zA-Z0-9_-]+\w[.]?[a-zA-Z0-9_-]+[@]\w+[.]\w{2,3}\w+[.]\w{2,3}$')
result = pattern.search(correo)
if result:
    print("Correo Valido")
else:
    print("Correo Invalido")
