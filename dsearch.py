#!/usr/bin/python3
#-*-coding: utf-8-*-
# desenvolvido por major
# felipe silva: github.com/felipefs01
#######
import requests
url = str(input("Alvo>"))
word = str(input("Wordlist>"))
c = 0
with open(word, "r") as rw:
    with open("DSearch_log.txt", "w") as wwd:
        for out in rw.readlines():
            c = c+1
            x = url + "/" + out.rstrip("\n")
            getd = requests.get(x)
            code = getd.status_code
            print("{} -> {}".format(getd.status_code, x))
            ok = "{} -> {}".format(getd.status_code, x)
            wwd.write(ok)
            wwd.write("\n")
print("Scan completo!")
