import pyautogui as pg
import time
import webbrowser
points = 0

# Question 1

answer = pg.prompt(
"""
Which would you rather do?
a) eat veggie chips with Kayla ALL day?
b) ride a pig to school for a week
c) play monopoly with a cat

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# Question 2

answer = pg.prompt(
"""
Who is your favorite actor/actress in Stranger Things?
a) Eleven 
b) Mike
c) Will
d) Dustin
e) Lucus
f) Nancy
g) Johnathon
h) Steve
i) Hopper
j) Joyce
k) Bob
L) Dr. Brenner

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4
elif answer == "e":
    points += 5
elif answer == "f":
    points += 6
elif answer == "g":
    points += 7
elif answer == "h":
    points += 8
elif answer == "i":
    points += 9
elif answer == "j":
    points += 10
elif answer == "k":
    points += 11
elif answer == "L":
    points += 12




# Question 2

answer = pg.prompt(
"""
If you had a child what would you name it
a) Lamp
b) Cuko
c) Monty
d) linis
e) cuscus
f) Lily
g) JJ
h) Craig

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4
elif answer == "e":
    points += 5
elif answer == "f":
    points += 6
elif answer == "g":
    points += 7
elif answer == "h":
    points += 8


# Question 3

answer = pg.prompt(
"""
who is your idol
a)muagi linus
b)purple dirt
c)five black pants

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



# Question 4

answer = pg.prompt(
"""
favorite type of berry??
a) nacks 
b) blackberry sweater jacks
c) razzyies
d) blubs
e) straws
f) crestrons
"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4
elif answer == "e":
    points += 5
elif answer == "f":
    points += 6



 # Question 5

answer = pg.prompt(
"""
where do you want to live?
a) inside a crab carcus
b) under the ping pong table in your moms ex boyfriends uncles mailmans house?
c) In a frozen yogurt machine
d) with your dead rabbit
e) in a prison
f) in the mall at annies pretzels stand
"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4
elif answer == "e":
    points += 5
elif answer == "f":
    points += 6

# END OF SURVEY
pg.alert("You are...")

# A weirdo

