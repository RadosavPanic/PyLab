data = set(); print(type(data))  # <class 'set'>
data = {32, 60, 87}; print(type(data))  # <class 'set'>

python_students = {'John', 'Peter', 'Ben', 'Sara', "Emily", "David"}
javascript_students = {'Emily', 'David', 'Alex', 'Sophia'}

# Set union
print(python_students | javascript_students)  # {'Sophia', 'Ben', 'John', 'Sara', 'Alex', 'Emily', 'Peter', 'David'}
print(python_students.union(javascript_students))  # {'Sophia', 'Ben', 'John', 'Sara', 'Alex', 'Emily', 'Peter', 'David'}

# Set intersection
print(python_students & javascript_students)  # {'Emily', 'David'}
print(python_students.intersection(javascript_students))  # {'Emily', 'David'}
print(python_students.isdisjoint(javascript_students))  # False, returns True if sets have null intersection

# Set difference
print(python_students - javascript_students)  # {'Peter', 'Ben', 'John', 'Sara'}
print(javascript_students - python_students)  # {'Sophia', 'Alex'}
print(python_students.difference(javascript_students))  # {'Peter', 'Ben', 'John', 'Sara'}
print(javascript_students.difference(python_students))  # {'Sophia', 'Alex'}

# Built-ins
ages = {23, 52, 40, 11, 25, 64}
print(len(ages), min(ages), max(ages), sum(ages))  # 6, 11, 64, 215
print(sorted(ages))  # [11, 23, 25, 40, 52, 64], returns new sorted list (does not sort Set itself)
print(ages.copy())  # {64, 52, 23, 40, 25, 11}, copy() returns a copy of the set

ages.add(100); print(ages)  # added 100, {64, 52, 100, 23, 40, 25, 11}
ages.discard(23); ages.remove(11)  # {64, 52, 100, 40, 25}, discard and remove both remove element from the set
print(ages.pop())  # 64, arbitrary element popped and returned
print(ages)  # {52, 100, 40, 25}
ages.update({30, 31, 32})  # {32, 52, 100, 40, 25, 30, 31}, updates set by union with another set

# subset, superset
A, B = {1, 2, 3}, {1, 2, 3, 4, 5}
print(A <= B); print(A.issubset(B))  # True, A is subset because its all elements are contained in set B
print(B >= A); print(B.issuperset(A))  # True, B is superset because it contains set A fully
print(B.issubset(A))  # False, set A doesn't contain set B elements fully

# A.remove(10)  # KeyError: 10, raises an error because element doesn't exist
A.clear(); print(A)  # set(), clears all elements from the set

B = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
B = B.union({10, 12, 14}); print(B)  # {0, 2, 4, 6, 8, 10, 12, 14}