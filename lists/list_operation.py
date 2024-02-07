list1=['a', True, 3, 4.5, 3]
list2=[100, False, 'John', 0.0, True]

#Index before update

print("Values before updates :", list2)

#updating index 2 in a list2 

Newvalue="Doe"
list2[1]=Newvalue

print("values after updates: ", list2)



#  concatinating

new_list=list1+list2

print(new_list)

# counting

count=new_list.count('a')
print(count)

#sort (only sorts numbers)
unsorted_items=[32,12,1,5,3,4,1]
unsorted_items.sort()

print("items sorted : ",unsorted_items)

#reverse items

unsorted_items.reverse()
print("items reversed : ",unsorted_items)

#copying items

copied_lists = unsorted_items.copy()
print(copied_lists)







