enrolled_students = {
    "John": {"courses": ["Python", "JavaScript"], "active_subscription": True},
    "Peter": {"courses": ["React", "C#"], "active_subscription": True},
    "Ben": {"courses": ["PHP", "Laravel"], "active_subscription": False},
    "Sara": {"courses": ["HTML", "CSS", "Python"], "active_subscription": True},
    "Emily": {"courses": ["Django", "Flask"], "active_subscription": False},
    "David": {"courses": ["Java", "Spring"], "active_subscription": True},
    "Alex": {"courses": ["Node.js", "MongoDB"], "active_subscription": False},
    "Sophia": {"courses": ["C++", "Algorithms"], "active_subscription": True}
}

print(enrolled_students["John"]["courses"])  # ['Python', 'JavaScript']
print(enrolled_students["Peter"].get("courses"))  # ['React', 'C#']
print(enrolled_students.get("Ben").get("courses"))  # ['PHP', 'Laravel']
print(enrolled_students.get("Alex")["active_subscription"])  # False

enrolled_students["Emily"]["active_subscription"] = True
print(enrolled_students.get("Emily").get("active_subscription"))  # True

fields_to_update = {
    "David": {"active_subscription": False},
    "Alex": {"active_subscription": True}
}

for key, value in fields_to_update.items():
    enrolled_students[key].update(value)

for key, value in enrolled_students.items():
    if key == "David" or key == "Alex":
        print(f"{key}: {value}")
"""
David: {'courses': ['Java', 'Spring'], 'active_subscription': False}
Alex: {'courses': ['Node.js', 'MongoDB'], 'active_subscription': True}
"""

print(enrolled_students.keys())  # dict_keys(['John', 'Peter', 'Ben', 'Sara', 'Emily', 'David', 'Alex', 'Sophia'])
print(enrolled_students.values())  # dict_values([{...}])

enrolled_students["John"]["courses"].append("Fast API")
print(enrolled_students["John"]["courses"])  # ['Python', 'JavaScript', 'Fast API']
enrolled_students["John"]["courses"].remove("JavaScript")
print(enrolled_students["John"]["courses"])  # ['Python', 'Fast API']

for student, values in enrolled_students.items():
    if not values["active_subscription"]:
        print(f"{student} doesn't have active subscription.")
"""
Ben doesn't have active subscription.
David doesn't have active subscription.
"""
