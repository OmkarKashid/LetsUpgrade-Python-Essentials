list1=[(1,2,3), [1,2], ['a','hit','less']]
size=len(list1)
for i in range(size):
    for each in list1[i]:
        list1.append(each)
del list1[0:size]
print(list1)