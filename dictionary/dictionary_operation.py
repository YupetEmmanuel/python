dict1={'a':1,"b":2}
dict2={'b':3,'c':4}

#updating Dictionary

dict1.update(dict2)
print(dict1)
print(dict2)

print(dict2.get('b'))

#comparision

dict3={'a':1,'b':2}
dict4={'a':3,'b':4}

print(dict3!=dict4)

#length of a dict

print(len(dict4))

#sorting items in a dict
dict5={'b':2,'a':4,'c':3,'k':99}

sorted_dict=dict(sorted(dict5.items()))
print(sorted_dict)

