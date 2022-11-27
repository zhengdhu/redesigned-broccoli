#引用库
from time import *
from os import *
import sys
from io import open


list1 = []
list2 = []
def cv(c):
    if c == "exit":
        exit()
    m = c.split(";")
    for i in range(len(m)):
        v = m[i]
        if "if" in v:
            p = v.index("(")
            p = p+1
            o = v.index(")")
            bn = v[p:o]
            kl = v.index("{")
            poj = kl+1
            ko = v.index("}")
            if bn:
                cv(v[poj:ko])
                continue
        if "javav" in v:
            p = v.split(" ")
            if p[1] in list1:
                d = list1.index(p[1])
                print(list2[d])
            else:
                print(p[1])
        if "var" in v:
            l = v.split(" ")
            try:
                int(l[1])
                print("ero")
            except:
                list1.append(l[1])
                list2.append(l[3])

crowdg = input("Do you want to read a file with a .oc suffix or enter it directly?:")
if(crowdg == 'y'):
    print("Thank you for using the file execution method, bolt q")
    zxcvbnm = input("file:")
    if(zxcvbnm.endswith(".oc")):
        with open(zxcvbnm) as edj:
            asdfghjkl = edj.read()
            print("Executing...")
            cv(asdfghjkl)
        exit()
    else:
        print("error!!!")
else:
    print("Well, we can let you type directly, but we recommend you run the file because he is still in closed beta, you can give us suggestions!!")
while True:
    l = input(">>>")
    cv(l)