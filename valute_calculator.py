import re

s = "192.168.0.4:8000"

match = re.findall(r"\d+\.\d+\.\d+\.\d+\:\d+", s)

print(match)
