import re
from functions import *


file = open("address.txt",'r',encoding="utf-8")
txt = file.read()

for item in txt.split("\n"):
    string_to_json(item)

