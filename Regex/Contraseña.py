# CONTRASEÑA

import re

pwd = "Incorrecta11*"
pattern = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')
result = pattern.search(pwd)
if result:
    print("Contraseña Válida")
else:
    print("Contraseña NO Válida")
