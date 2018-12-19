import pickle

l = ["dog", "cat", "mouse"]
D = {"A": 100,"B": 200,"c": l}
with open('pickle.p', 'w') as f:
    pickle.dump(D, f, protocol=pickle.HIGHEST_PROTOCOL)

