# LISTS

# row = ["Ford", "Audi", "BMW", "Lexus"]
# row.append("Mercedes")
# print(row)
# print(row[4])
# row[2] = "Jeep"
# print(row)

# row.append("Honda")
# print(row)
# print(row[4])

# row.insert(0, "Kia")
# print(row)
# print(row[4])

# print(row.index("Mercedes")) # index method stops as soon as it finds the first occurance

# print(row.pop(5))
# print(row)

# row.remove("Lexus")
# print(row)

# MULTIDIMENSIONAL LISTS

# # 2D List of lists - index cars by row
# lot_2d = [['Toyota', 'Audi', 'BMW'], 
#           ['Lexus', 'Jeep'], 
#           ['Honda', 'Kia', 'Mazda']]

# # 3D list of lists of lists - index cars by floor, row, spot
# lot_3d = [[['Telsa', 'Fiat', 'BMW'],
#            ['Honda', 'Jeep'],
#            ['Saab', 'Kia', 'Ford']],
#           [['Subaru', 'Nissan'],
#            ['Volvo']],
#           [['Mazda', 'Chevy'],
#            [],
#            ['Volkswagen']]]

# print(lot_2d)
# print(lot_2d[2])
# print(lot_2d[2][1])

# print(lot_3d)
# print(lot_3d[0])
# print(lot_3d[0][2])
# print(lot_3d[0][2][1])

# for car in lot_3d:
#     print(car)

# for floor in lot_3d:
#     for row in floor:
#         for car in row:
#             print(car)

# TUPLES - Immutable

# my_tuple = ('a', 'b', 'c', 1, 2, 3)
# print(my_tuple)
# print(my_tuple[2])

# my_tuple[2] = 'd'

# Queues : First In First Out (FIFO)

# import queue
# q = queue.Queue()
# print(q.empty())
# q.put('bag1')
# print(q.empty())
# q.put('bag2')
# q.put('bag3')
# print(q.get())
# print(q.get())
# print(q.get())
# # As the queue is empty the program will keep on running in search of the next item....So we have to be careful while using queue
# q = queue.Queue(maxsize = 2)
# print(q.empty())
# q.put('bag1')
# print(q.full())
# q.put('bag2')
# print(q.full())
# # q.put('bag3') again the program will stuck as the queue is full and we are trying to add more so it will keep on running until the queue is empty

# q.put_nowait('bag3') # shows that the queue is full rather than running the program

# Stacks : Last In First Out (LIFO)

# stack = list()
# stack.append('bill1')
# stack.append('bill2')
# print(stack.pop())
# stack.append('bill3')
# stack.append('bill4')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop()) # throws error as the stack is empty


