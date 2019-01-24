#01- Remove duplicates from the list

varList1=["vidya","suryawanshi","vidya","suryawanshi","sandeep"]
varSet1=list(set(varList1))

print varSet1

#02- Find the length of all words of a list

varList2=["vidya","suryawanshi","sandeep"]
lenList=len(varList2[0])+len(varList2[1])+len(varList2[2])

print lenList

#03- Print a specified list after removing the 0th, 4th, 5th elements

varList3=["Red","Green","White","Black","Pink","Yellow"]
str1,str2,str3="Red","Pink","Yellow"

varList3.remove(str1)
varList3.remove(str2)
varList3.remove(str3)

print varList3