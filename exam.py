from collections import Counter,OrderedDict


def countFromInput(x):
    inputlist = list(map(int, x.strip(',').split(',')))
    sortedcounter = OrderedDict(sorted(Counter(inputlist).items()))
    for k,v in sortedcounter.items():
        print(f"{k}:{v}")

x = input()
try:
    countFromInput(x)
except:
    print("Cannot count the number from your input.")