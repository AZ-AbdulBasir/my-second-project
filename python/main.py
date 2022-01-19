first_set = {10, 20, 30, 40, 50}
print(first_set.remove(10))
print(first_set.remove(20))
print(first_set.remove(30))
print(first_set)




first_set = {10, 20, 30, 40, 50}
second_set = {60, 70, 80, 20, 10}
print(first_set.intersection(second_set))







first_set = {10, 20, 30, 40, 50}
second_set = {30, 40, 50, 60, 70}
print(first_set.discard(10))
print(first_set.discard(20))
print(first_set.discard(60))
print(first_set.discard(70))
print(first_set)





first_set = {10, 20, 30, 40, 50}
second_set =  {30, 40, 50, 60, 70}
print(first_set.add(70))
print(first_set.add(60))
print(first_set.discard(40))
print(first_set.discard(50))
print(first_set.discard(30))
print(first_set)






my_list = ['Ten', 'Twenty', 'Thirty']
another_list = [10, 20, 30]
my_dict = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
print(my_dict)

students_list = [
    [1, 'Sam', 18, 'id-387'],
    [2, 'Michael', 18, 'id-235'],
    [3, 'Thomas', 18, 'id-321']
]

students_dict = {}

for i in students_list:
    students_dict[i[0]] = i[1:]
print(students_dict)

# 1
new_students_dict = students_dict.copy()
for i in new_students_dict:
    if students_dict[i][1] == 23:
        del students_dict[i]
print(students_dict)

# 2
for i in new_students_dict:
    if new_students_dict[i][0].startswith("Michael"):
        new_students_dict[i][1] += 1
print(new_students_dict)

# 3
for i in new_students_dict:
    if new_students_dict[i][0].startswith("Michael "):
        new_students_dict[i][0] = new_students_dict[i][0].replace('Michael', 'Thomas')
print(new_students_dict)


