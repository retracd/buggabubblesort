def ptl():
    return ", ".join((str(i) for i in l))

l = [5, 4, 3, 2, 1]

print("original list:              " + ptl())

print("\nbubble sort:")
for itr in range(ln :=  len(l) - 1):
    for itr2 in range(ln):
        if (l[itr2] > l[itr2 + 1]):
            l[itr2], l[itr2 + 1] = l[itr2 + 1], l[itr2]
    print(f"iteration {itr + 1} of bubble sort: " + ptl())
print("\nbubble sorted list:         " + ptl())
