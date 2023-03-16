with open("myfile.txt","r") as f:
    t=f.read()
with open("copy.txt","w") as f:
    f.write(t)