# IP Address

import re

ip = "201.221.176.43"
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
result = pattern.search(ip)
if result:
    print("IP Valida")
else:
    print("IP Invalida")
