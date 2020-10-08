import fileinput
url =[]
with fileinput.input(files=('userurl.txt')) as f:
    for line in f:
        url.append(line.replace("\n", ""))
print(url)

with open('finaluserurl.txt', 'w') as f:
    print(url, file=f)
