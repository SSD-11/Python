# FECHA

import re

fecha = "22/05/2005"
pattern = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])[- /.](0?[1-9]|1[012])[- /.](19|20)\d\d$')
result = pattern.search(fecha)
if result:
    print("Fecha Valida")
else:
    print("Fecha Invalida")

# Año bisiesto

import re

year = "29/02/2016"
pattern = re.compile(
    r'^(?:(?:(?:0?[1-9]|1\d|2[0-8])[/](?:0?[1-9]|1[0-2])|(?:29|30)[/](?:0?[13-9]|1[0-2])|31[/](?:0?[13578]|1[02]))[/](?:0{2,3}[1-9]|0{1,2}[1-9]\d|0?[1-9]\d{2}|[1-9]\d{3})|29[/]0?2[/](?:\d{1,2}(?:0[48]|[2468][048]|[13579][26])|(?:0?[48]|[13579][26]|[2468][048])00))$')
result = pattern.search(year)
if result:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
