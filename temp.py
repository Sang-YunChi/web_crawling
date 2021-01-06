file = open("searchResponse.txt", "r")
data = []
while True:
    line = file.readline().strip()
    if not line:
        break
    data.append(line)

for d in data:
    print(d)