lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
med = round(len(lst)/2)

sub_List=lst[med-3:med+3]

even_List = sub_List[::2]

result = even_List[len(even_List)-1]**2
print(result)
