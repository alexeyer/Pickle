import os

try:
    os.makedirs("gmail")
except OSError as e:
    print (e)

print "test"
