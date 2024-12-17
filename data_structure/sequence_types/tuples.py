# Tuples are read-only lists (immutable)

pl_languages = ("JavaScript", "PHP", "C++", "Python", "Perl", "Ruby", "Go", "Rust", "Java", "C#", "Assembly")

# Updating and deleting is not possible
# pl_languages[1] = "Laravel"  # TypeError: 'tuple' object does not support item assignment
# del pl_languages[2]  # TypeError: 'tuple' object doesn't support item deletion

# Deleting whole tuple is possible only
# del pl_languages
# print(pl_languages)  # NameError: name 'pl_languages' is not defined

print(pl_languages[1:4])  # ('PHP', 'C++', 'Python')
print((31, 5) * 2)  # (31, 5, 31, 5)
print("Perl" in pl_languages)  # True
print("Kotlin" not in pl_languages)  # True

print(len(pl_languages), min(pl_languages), max(pl_languages))  # 11, Assembly, Rust

print(pl_languages.count("Go"))  # 1
print(pl_languages.index("Ruby"))  # 5