countries_list1 = ["Spain", "Peru", "Brazil", "China", "Egypt", "Serbia"]
countries_list2 = ["Estonia", "Germany", "Moldova", "Vietnam", "Libya"]

del countries_list1[3], countries_list2[2]  # China, Moldova
print(f"{countries_list1} / {countries_list2}")  # ['Spain', 'Peru', 'Brazil', 'Egypt', 'Serbia'] / ['Estonia', 'Germany', 'Vietnam', 'Libya']

print(countries_list2[1:3], countries_list2[-1])  # ['Germany', 'Vietnam'], Libya
print([1, 5, 4] * 2)  # [1, 5, 4, 1, 5, 4]
print("Vietnam" in countries_list2, "China" not in countries_list2, "Ethiopia" in countries_list1)  # True, True, False
print([65, 20] + [15, 31])  # [65, 20, 15, 31]

print(f"First list length: {len(countries_list1)}")  # 5, can also use internal function: countries_list1.__len__()
print(min(countries_list1), max(countries_list1))  # Brazil, Spain

countries_list2[2] = "Libya"; print(countries_list2.count("Libya")); del countries_list2[2]  # 2

countries_list2.append("Fiji"); print(countries_list2)  # ['Estonia', 'Germany', 'Libya', 'Fiji']

countries_list2.insert(2, "Vietnam"); print(countries_list2)  # ['Estonia', 'Germany', 'Vietnam', 'Libya', 'Fiji']

countries_list2.pop(); print(countries_list2)  # ['Estonia', 'Germany', 'Vietnam', 'Libya']

countries_list2.remove("Germany"); print(countries_list2)  # ['Estonia', 'Vietnam', 'Libya']

countries_list2.extend(["Denmark", "Hungary"]); print(countries_list2)
print(countries_list2.index("Denmark"))  # 3

countries_list2.reverse(); print(countries_list2)  # ['Hungary', 'Denmark', 'Libya', 'Vietnam', 'Estonia']
countries_list2.sort(); print(countries_list2)  # ['Denmark', 'Estonia', 'Hungary', 'Libya', 'Vietnam']

# List comprehension
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]

charactersDenmark = [x for x in countries_list2[countries_list2.index("Denmark")]]
print(charactersDenmark)  # ['D', 'e', 'n', 'm', 'a', 'r', 'k']