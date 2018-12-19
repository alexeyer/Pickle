import pickle

with open('pickle.p', 'r') as f:
    l = pickle.load(f)
with open('values.txt', 'w') as y:
    y.write(str(l.values()))

