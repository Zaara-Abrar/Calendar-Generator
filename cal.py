import calendar
import random
upper_limit=0
lower_limit=0

#if upper_limit > 2024:
#    print("Calendar not exists")

try: 
   upper_limit= int(input("Enter upper limit of year: "))
   lower_limit= int(input("Enter lower limit of year: "))
except ValueError:
   print("Enter integer value ")
except TypeError:
   print("Enter valid input ")

year= random.randint(a= lower_limit,b=upper_limit) # generates a random no. between two limits
print(calendar.calendar(year)) # print calendar using calendar() of calendar module

month= random.randint(1,12)
print(calendar.month(year,month)) #prints specific month and year calendar

'''
random.sample(sequence,num_of_items)
random.choice(sequence) ''' #it returns number of random songs with iteration
#the difference between both is that 'sample' returns no. of random elements