import pickle
bookstore={"python core":399,"OOPs with C++":349,"C Programming":299}
with open("books","wb") as f:
    pickle.dump(bookstore,f)
