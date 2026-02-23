"""introducting list"""

my_numbers: list[float] = [] #data type i expect everything to be is inside [], cannot no use () or {}, only [] for specificying data type. 
my_numbers.append(1.5) #adding something to end of list is called append, always function_name.append(argument)
print(my_numbers)

game_points: list[int] = [102, 86, 94] #must seperate list by commas. this declared and initializes the variable.
print(game_points)
print(game_points[2])

print(len(game_points))
print(game_points[len(game_points) - 1])


# is this type of modification transferrable


name: str = "Izzy"
name_list: list[str] = list(name)
name_list[3] = "i"
# try changing the y to an i
print(name_list)

grocery_list: list[str] = ["egg", "milk", "bread"] #egg is 0, milk is 1, bread is 2. 
grocery_list.pop(2) #pop method, pop off list. specifices INDEX that you want to pop off. so always an int. this change slie to just egg and milk. ....pop(1) would remove milk. it would then be eggs, bread. eggs would be 0 and bread would then be 1.




