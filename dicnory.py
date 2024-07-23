#tuple
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
first_fruit = fruits[0]
fruits[1] = "blueberry"

#dictionarie
person = {
    "name": "John",
    "age": 30
}
person["age"] = 31

#set
colors = {"red", "green", "blue"}
colors.add("yellow")

#if statment
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")   

#for loop
for fruit in fruits:
    print(fruit)

#while
count = 0
while count < 5:
    print(count)
    count += 1

def greet(name):
    return f"Hello, {name}"

message = greet("Alice")