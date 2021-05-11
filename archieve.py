#Variables
name = "Dillon"

print(name)

x_position = 3.14
print(x_position)

print(type(x_position))

number = 10
print(number)
print(type(number))

print(type(name))

#############################################
#Booleans and variables into strings

is_game_over = True
print(is_game_over)

name = "Dillon"
age = 27
print("Hello my name is {} and I am {} years old".format(name,age))

PI = 3.14
print("The mathamatical value for PI is {}".format(PI))

phone_number = 7095551234
print("The phone number is: {}".format(phone_number))

####################################################
#Arithmetic Operators + = * / % // **

x_position = 10

forward = x_position + 1
print(forward)

backward = x_position - 1
print(backward)

remainder = 5 % 2
print(remainder)

floor_division = 5 // 2
print(floor_division)

five_squared = 5 ** 2
print(five_squared)

x_position += 1
print(x_position)

first_name = "Dillon "
last_name = "Porter "
print(first_name + last_name)


################################################
#Logical Operators < > <= >= != not and or

x_position = 6
end_position = 10

is_at_end = x_position == end_position
print(is_at_end)
print(not is_at_end)


score = 8
is_game_over = score >= 9 or is_at_end
print(is_game_over)



######################################################
#list [12, "string", True]

enemy_position = [5, 10, 15, 28, 31, 34, 44, 48, 66, 88, 99, 101]
print(len(enemy_position))
print(enemy_position)
print(enemy_position[8])

enemy_position.append(98)
print(enemy_position)

enemy_position.insert(3, 55)
print(enemy_position)

enemy_position.remove(98)
print(enemy_position)


##############################################
#tuples a nonmutable list of data (arrays)

high_score = ("Dillon", 180, 8, 13, 16, 28, 31, 34)
print(high_score)

high_score = ("Random Name", 22, 34, 55, 66, 11, 2, True, False)
print(high_score)

name = high_score[0]
print(name)

print("Random" in name)

###################################################################
#dictionaries

actions = {"r": 1, "l" : 2, "d": 3}
print(actions)

actions["u"] = 4
actions["r"] = 10
print(actions)

actions.pop("u")
print(actions)

print(actions.keys())
print(actions.values())
print(actions.items())

print(actions.get("r"))

###################################
#control flow - If statements

number = 22

if number >= 10:
  print("Is greater than 10")
elif number <= 10:
  print("Is less than 10")
else: 
  print("Not a number")


animal = "bear"

if animal == "dog":
  print("dog")
elif animal == "cat":
  print("cat")
elif animal == "bear":
  print("bear")
else:
  print(animal)


key = "y"

if key == "r":
  print("Move Right")
elif key == "l":
  print("Move Left")
elif key == "u":
  print("Move up")
elif key == "d":
  print("Move Down")
else:
  print("invalid key")


  number = 6

  if number <= 5:
    print("You're too young")
  elif number <= 19:
    print("You're old enough")
  elif number <= 55:
    print("You get a discount")
  elif number <= 85:
    print("You get in for free!")
  else:
    print("babies aren't allowed to enter!")

###############################################
#Control Flow - While Lookup
number = 0
end_number = 10
end_game = 6

while number < end_number:
  number += 1
  print(number)
  if number == end_game:
    print("Sorry, try again!")
    break
  if number == end_number:
    print("Congrats, you Won!!")


##########################################
#for in loop

enemy_positions = [5, 10 , 15]

lotto_numbers = [8, 13, 16, 28, 31, 34]

for enemy_position in enemy_positions:
  print(enemy_position)

for i in range(0,4):
  print("Hello")

for numbers in lotto_numbers:
  print(numbers)


################################
#functions
position = 0

def move_player(position, by_amount):
  position += by_amount
  return position

position = move_player(position, 6)
position = move_player(position, 7)
print("The plaayer moved", position, "steps")


#######################
#objects
class GameObject:

  def __init__(self, name, x_pos, y_pos):
    self.name = name
    self.x_pos = x_pos
    self.y_pos = y_pos
  
  def move(self, by_x_amount, by_y_amount ):
    self.x_pos += by_x_amount
    self.y_pos += by_y_amount


game_object = GameObject("Enemy", 1, 2)


##inheritance

class Enemy(GameObject):
  def __init__(self, name, x_pos, y_pos, health):
    super().__init__(name, x_pos, y_pos) 
    self.health = health
     #instead of repeating the code, use the Super().__init__ to reinitalize the first def __init__ chr
  
  def take_damage(self, amount):
    self.health -= amount


game_object = GameObject("Random Name", 1, 2)
enemy = Enemy("Enemyplayer", 5, 10, 100)

print(game_object.name, game_object.x_pos)
print(enemy.name)

enemy.take_damage(40)
print(enemy.health)


