import rpyc
import sys
import os
if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))
server = sys.argv[1]
print(server)
c = rpyc.classic.connect(host=server, port=18812)

print(c.root.get_answer())