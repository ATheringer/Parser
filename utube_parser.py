import sys


def read(filename):
    with open(filename, "r") as f:
        ls = f.readlines()
    f.close()
    return ls

def write(filename, data):
    with open(filename, "w") as f:
        for line in data:
            f.write(line)
        f.close()
    return


def lineParser(x):
    xs = x.split(' ', 1)
    start = xs[0]
    tname = xs[1]
    tlist = tname.split(' http://soundcloud.com/')
    name = tlist[0]
    start = start.replace("[", "").replace("]", "").replace(":"," ")
    ys = start.split(" ")
    for i in range(len(ys)):
        ys[i] = int(ys[i])
    if(len(ys) == 2):
        start = ys[1] + (ys[0] * 60)
    elif(len(ys) == 3):
        start = ys[2] + (ys[1] * 60) + (ys[0] * 3600)
    else:
        print("Error: Weird time format")
    fs = [str(start), name]
    return fs

def fileParser(xs):
    fstr = ""
    tls = []
    fls = []
    for x in xs:
        x = lineParser(x)
        tls.append(x)
    for i in range(len(tls) - 1):
        fstr = tls[i][0] + "\t" + tls[i+1][0] + "\t" + tls[i][1] + "\n"
        fls.append(fstr)
    return fls


def main():
    myfile = sys.argv[1]
    if(not myfile):
        print("Error: You must provide a file to parse.")
        return
    data = read(myfile)
    fdata = fileParser(data)
    newfile = myfile + "_adfm.txt"
    write(newfile, fdata)
    return

main()
