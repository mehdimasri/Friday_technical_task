import re
from functions import *


list_of_complex_add = ["Am Bächle 23",
                       "Winterallee 3",
                       "Musterstrasse 45",
                       "Blaufeldweg 123B",
                       "Auf der Vogelwiese 23 b",
                       "4, rue de la revolution",
                       "No 4 rue de la rev",
                       "200 Broadway Av",
                       "Calle Aduana, 29",
                       "Calle 39 No 1540"]

file = open("address.txt",'r',encoding="utf-8")
txt = file.read()

for item in txt.split("\n"):
    string_to_json(item)

