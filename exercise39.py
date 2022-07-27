person={
    'name':"gopika",
    'age':25,
    'place':"thrissur",
    'job':"SE_trainee"
}
course={
    'sub1':'python',
    'sub2':'php',
    'sub2':'cpp'
}
person["address"]="kavungal house"
print(person)
print('-'*20)
print(person['name'])
print(person['age'])
print(person['place'])
for i,j in list(person.items()):
    print(f"gopika likes {j}")


