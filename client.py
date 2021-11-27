import rpyc
import sys
import os
from random import randint
import time


if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))
server = sys.argv[1]
c = rpyc.connect(server,18861, config={'sync_request_timeout': 30000})



n = int(input())
lista = []
for i in range(n):
    lista.append(randint(0,n))
    
start = time.time()
c.root.soma_vetor(lista)
end = time.time()
print(end-start)
