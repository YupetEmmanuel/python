students={'James': 63, 'Sarah': 91, 'Alex': 97}
fruits={('Orange', 'green mango'): 'sour fruits', 'Banana': 'sweet fruit', 'Apple': 'sweet fruit'}
capitals={"Uganda": "Kampala"}

print(students)
print(fruits)


k=capitals["Uganda"]

#accessing Kampala
print(k)
print(capitals["Uganda"])

di = students.get('James')

print(di)
print(students.get("Alex"))


D1 = students|fruits|capitals

for d in D1:
    print(d, end=(", "))
   
    



