people = [{"name": "someone", "age": 25}, {"name": "thing", "age": 22}, {"name": "random", "age": 20}]

by_age = sorted(people, key=lambda x: x["age"])
print(by_age)

print()

by_name_age = sorted(people, key=lambda x:(x["name"], x["age"]))
print(by_name_age)