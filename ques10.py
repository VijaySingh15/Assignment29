import pickle
with open("books","rb") as f:
    bookfile=pickle.load(f)
print(bookfile)