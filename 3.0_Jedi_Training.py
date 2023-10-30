# 3.0 Jedi Training (20pts)  Name:Logan Mills


# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name. (1pt)

name = input("What's your name? ")
print("Hello ", name, "how was your day?")
response = input("Good or bad? ")

if response.lower() == "good":
    print("That's good to hear")
elif response.lower() == "bad":
    input("That must suck, what happened? Did you run into an issue in your code? ")
    print("I see, hope it gets better")
else:
    print("Respond with Good or Bad")

# 2. Write a program where a user enters a base and height, and you print the area of a triangle. (1pt)

x = int(input("What's the base of your triangle? "))
y = int(input("What's the height of your triangle? "))

answer = x * y
answer /= 2
print("The area is", answer)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference. (1pt)

which = input("Are you calculating area or circumference? ")
if which.lower() == "area":
    r = float(input("What's the radius of your circle? "))
    answer = r ** 2
    answer *= 3.14
    print("The area of your circle is", answer)
elif which.lower() == "circumference":
    r = float(input("What's the radius of your circle? "))
    answer = r * 2
    answer *= 3.14
    print("The area of your circle is", answer)
else:
    print("Choose area or circumference")

# 4. Ask a user for an integer and then print the square root. (1pt)

import math

number = int(input("What number would you like the square root of? "))
answer = math.sqrt(number)

print(answer)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next. (1pt)
print("May the mass times acceleration be with you!")
m = int(input("What's the mass of the object? "))
a = int(input("What's the acceleration of the object? "))

f = m * a

print("The force is", f)


'''
6. TEMPERATURE PROGRAM (5pts)
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test your program with the following data:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: -40 Please tell me what this output is!

'''

temp = float(input("Whats the temperature (in Fahrenheit)? "))

temp -= 32
temp *=5
temp /= 9

print("It is", temp, "Celsius")

'''
7. TRAPEZOID PROGRAM (5pts)
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''

from time import sleep  # Figured I'd add a small loading bar to make it more fun
from progress.bar import Bar  # pip install progress.bar, progress bar only works in cmd or terminal, not in PyCharm

b1 = int(input("Whats the first base of your trapezoid? "))
b2 = int(input("Whats the second base of your trapezoid? "))
h = int(input("Whats the height of your trapezoid? "))

print("\n")

with Bar('Calculating') as bar:  # Figured I'd add an unnecessary progress bar cause it looks cool
    for i in range(100):
        sleep(0.01)
        bar.next()

print("\n")
b = b1 + b2
b /= 2
answer = b * h

print("The area of your trapezoid is", answer)

'''
8. GRADING PROGRAM (5pts)
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''

sem = float(input("What is your semester grade? "))
fin = float(input("What is your final exam grade? "))
wor = float(input("How much is your final worth? "))

semwor = 100 - wor
semwor /= 100
sem *= semwor
wor /= 100
fin *= wor
overall = fin + sem

print(overall)









