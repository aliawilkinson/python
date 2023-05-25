numbers = [1,2,3]
new_nums = [(x + 1) for x in numbers]    
print(new_nums)


name = "Alegria"
new_name_list = [l for l in name]
print(new_name_list)

range_list = [num * 2 for num in range(1,5)]
print(range_list)

names = ["Alex","Alia","Lily","Maddi","Mando","Alejandro"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

long_cap_names = [name.upper() for name in names if len(name) > 5]
print(long_cap_names)

# Challenge
# All names 5 or more, turn them to uppercase
# return: all caps names