#File IO
with open("notes.txt", "r") as f:
    t = f.readlines()
    print(t)
    print("No of lines =", len(t))

    c = 0
    for i in t:
        c += len(i.split())

    print("No of words =", c)

#Exception handling
try:
    with open("data.txt","r") as f:
        print(f.read())
except Exception as e:
    print("Not found")