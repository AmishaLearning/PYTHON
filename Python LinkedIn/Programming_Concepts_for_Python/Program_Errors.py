# Errors

""" Trying to Download Things That Don't Exist """

# import urllib.request

# try:
#     webpage = urllib.request.urlopen('http://www.goodgle.com')
#     for line in webpage:
#         print(line)
# except:
#     print('Could not access webpage')

# try:
#     webpage = urllib.request.urlopen('http://www.goodgle.com')
# except:
#     print('Could not access webpage')
# else:# runs only when try block is executed successfully
#     for line in webpage:
#        print(line)

# VALIDATE INPUT
  
""" Overloading a Circuit Breaker """

class CircuitBreaker:
    def __init__(self, max_amps):
        self.capacity = max_amps  # max capacity in amps
        self.load = 0             # present load in amps

    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception('Connection will exceed Capacity')
        elif self.load + amps < 0:
            raise Exception('Connection will cause a negative load')
        else:
            self.load += amps

# cb = CircuitBreaker(20)
# print(cb.capacity)
# print(cb.load)

# cb.connect(12)
# cb.connect(7)
# cb.connect(10)
# print(cb.load)

# cb1 = CircuitBreaker(20)
# print(cb1.load)
# cb1.connect(12)
# print(cb1.load)
# cb1.connect(15)
# print(cb1.load)

# cb2 = CircuitBreaker(20)
# cb2.connect(35)
# print(cb2.load)
# cb2.connect(-1)

# """ Handling Household Problems """

# class ElectricalError(Exception):
#     def __init__(self, device, problem):
#         self.device = device
#         self.problem = problem

#     def __str__(self):
#         return f'The {self.device} is {self.problem}!'

# class PlumbingError(Exception):
#     def __init__(self, device, problem):
#         self.device = device
#         self.problem = problem

#     def __str__(self):
#         return f'The {self.device} is {self.problem}!'

# def cause_error(error_type):
#     if error_type == 'electrical':
#         raise ElectricalError('circuit breaker', 'overloaded')
#     elif error_type == 'plumbing':
#         raise PlumbingError('dishwasher', 'spraying water')
#     else:
#         raise Exception('A generic Household Problem')

# try:
#     cause_error('yard')
# except ElectricalError as e:
#     print(e)
#     print('Barron fix it')
# except PlumbingError as e:
#     print(e)
#     print('Call the plumber')
# except:
#     print('Call the landlord')
    
# Polling

# """ Polling for Pizza to Cure My Hunger """
# NOt recommended

# hungry = True  # I need a pizza!

# while (hungry):
#     print('Opening the front door')
#     front_door = open('front_door.txt', 'r', encoding='utf-8')

#     if 'Delivery Person' in front_door:
#         print('The pizza is here!!!!!!!!!!')
#         hungry = False
#     else:
#         print('Not yet...')

#     print('Closing the front door.\n')
#     front_door.close()

# import time

# hungry = True  # I need a pizza!

# while (hungry):
#     print('Opening the front door')
#     front_door = open('front_door.txt', 'r', encoding='utf-8')

#     if 'Delivery Person' in front_door:
#         print('The pizza is here!!!!!!!!!!')
#         hungry = False
#     else:
#         print('Not yet...')

#     print('Closing the front door.\n')
#     front_door.close()
#     time.sleep(1)

# Event - Driven Program

""" A Brief Study in Handling Life Events """

import asyncio
import time

def alarm():  # handler for when the alarm goes off
    print('Wake Up!')
    print('Calling the Pizza Company.\n')
    loop.call_later(1, alarm)  # schedule another alarm

def doorbell():  # handler for when the doorbell rings
    print('Ding! Dong!')
    time.sleep(3)
    print('Opening the door... "Thanks for bringing the pizza!"\n')
    loop.stop()
    
def phonecall():  # handler for when the phone rings
    print('Ring Ring!')
    print('Answering the phone... "Hello! Who is this?"\n')

loop = asyncio.get_event_loop()
loop.call_later(1, alarm)      # schedule initial alarm event
loop.call_later(4, doorbell)   # schedule doorbell event
loop.call_later(5, phonecall)  # schedule phone call event

print('Starting the event loop...\n')
loop.run_forever()  # run until stop() is called

print('The event loop stopped; closing it down.')
loop.close()

