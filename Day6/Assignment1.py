list1=[1,2,3,4,5,6,7,8]
list2=["a","b","c","d","e"]
dict1={}
min_size=min(len(list1),len(list2))
dict1.update((list1[a],list2[a]) for a in range(min_size))
print(dict1)
