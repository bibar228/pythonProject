import os
directory = "D:\\видос"
x = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        d = f.split("\\")
        if d[2][-3:] == "mp4":
            x.append(d[2])

print(x)
with open("videos.txt", "w", encoding="UTF-8") as file:
    for i in x:
        file.write(i+"\n")


