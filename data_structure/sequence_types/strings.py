name = input("Enter your name: ")
score = int(input("Enter your score: "))

print("Welcome {}, with score of {}.".format(name, score))  # Welcome John, with score of 41.
print("Score: {1} - {0}".format(name, score))  # Score: 41 - John
print(f"Name: {name}, score: {score}")  # Name: John, score: 41

# Slicing (start:end:step) - end character is excluded
str1 = "Django"
print(str1[:], str1[::])  # Django, slicing parameters excluded
print(str1[2:5], str1[3:], str1[:4])  # ang, ngo, Djan
print(str1[::2])  # Dag, step: 2, other parameters excluded

print(" ".join(["John", "Doe"]))  # John Doe

print(str1.isupper(), str1.islower())  # False, False
print(str1.upper(), str1.lower())  # DJANGO, django
print(str1.find("go"))  # 4
print(str1.index("ja"))  # 1
print(str1.replace("Dj", "M"))  # Mango
print(str1.startswith("Dj"))  # True
print(str1.endswith("go"))  # True
print(str1.zfill(10))  # 0000Django (fills string with zeros to 10 characters if it contains less than 10)
print(str1.swapcase())  # dJANGO
print(str1.swapcase().capitalize())  # Django
