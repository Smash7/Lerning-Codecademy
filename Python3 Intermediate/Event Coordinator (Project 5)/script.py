guests = {}
# Generator Functions
# tasks 1-4


def read_guestlist(file_name):
  text_file = open(file_name, 'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
      # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    n = yield name
    if n != None:
      name, age = n.split(',')
      guests[name] = int(age)

# taks 5&6


def table1(Name, Table):
  yield (Name, "Chicken", "Table 1", "Seat {}".format(Table))


def table2(Name, Table):
  yield (Name, "Beef", "Table 2", "Seat {}".format(Table))


def table3(Name, Table):
  yield (Name, "Fish", "Table 2", "Seat {}".format(Table))


def assign_seating(guests):
  counter = 1
  for guest in guests:
    if counter < 6:
      yield from table1(guest, counter)
      counter += 1
    elif counter < 11:
      N = counter - 5
      yield from table2(guest, N)
      counter += 1
    elif counter < 16:
      N = counter - 10
      yield from table3(guest, N)
      counter += 1
    else:
      return "No More Seats Available"


# Calling the Functions
# taks 1
guest_list = read_guestlist(
    r'Python3 Intermediate/Event Coordinator (Project 5)/guest_list.txt')

# task 2
next(guest_list)  # prime the generator
guest_list.send('Jane,35')

for i in range(10):
  print(next(guest_list))

# task 3
for guest in guest_list:
  print(guest)

# task 4
over_21 = (adult for adult in guests if guests[i] >= 21)

for guest in over_21:
  print(guest + ' is over 21')

# task 5 & 6
assignment = assign_seating(guests)

for seating in assignment:
  print(seating)
