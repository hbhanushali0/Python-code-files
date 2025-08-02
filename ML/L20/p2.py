
import pickle

with open("db.model", "rb") as f:
    model = pickle.load(f)

fs = float(input("enter fasting sugar "))
fu = int(input("0 no and 1 yes --> freq urination "))
d = [[fs,fu]]
print(model.predict(d))


