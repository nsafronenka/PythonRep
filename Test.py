import random                       # import random module to generate random values

thislist = []                       # lists for random values
oddValues = []                      # lists for odd values
evenValues = []                     # lists for even values


for i in range(100):                # generating 100 values
    val = random.randint(0, 1000)   # generate random number from 0-1000
    thislist.append(val)            # add generated values to the common list
    if val % 2 == 0:                # check whether the value is even or odd, finding the remainder of division
        evenValues.append(val)      # add even values to even list
    else:
        oddValues.append(val)       # add odd values to odd list

print("RandomValues", thislist)     # print all Values
print("OddValues", oddValues)       # print Odd Values
print("EvenValues", evenValues)     # print Even Values


print("OddAverage", sum(oddValues) / len(oddValues))        # print average of odd values, I was thinking to use try-except,
                                                            # but it doesn't make a sense due to the len(oddValues) can't be 0 in my case
print("EvenAverage", sum(evenValues) / len(evenValues))     # print average of even values.


n = len(thislist)                                              # calculate the length of the list
for k in range(0, n-1):                                        # number of scans within the list
    for i in range(0, n-k-1):                                  # the number of comparisons each time decreases by the value k
        if thislist[i] > thislist[i+1]:                                 # compare neighbour values
            thislist[i], thislist[i+1] = thislist[i+1], thislist[i]     # swap values to change the order

print("FromMinToMaxValues", thislist)                           # print sorted list













