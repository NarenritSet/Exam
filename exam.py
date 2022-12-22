from collections import Counter,OrderedDict


def countFromInput(x):
    #Get the string from input, remove exceeded comma, split them into list, then convert items to int with map() function.
    inputlist = list(map(int, x.strip(',').split(',')))
    #Count items with Counter() then sorted key with sorted()
    #Now there is a list of items and their amount, finally, create the Dictionary with order by OrderedDict()
    sortedcounter = OrderedDict(sorted(Counter(inputlist).items()))
    for k,v in sortedcounter.items():
        print(f"{k}:{v}")

x = input('Input: ')
try:
    countFromInput(x)
except:
    print("Cannot count the number from your input.")