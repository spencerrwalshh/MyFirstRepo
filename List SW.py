name = "Abigail Spencer Barlow Walsh"


subjects = ["english", "Art", "History", "Math", "Spanish", "Science", "Compsci"]


print ("Hola" + name)

for i in subjects:
    print("One of my classes is" + i)


horses = ["Stormy","Queen","Cassino","Togo", "Bo", "Ravel"]

for i in horses:
    if i == "Togo":
        print( i + "is the best horse ever.")
    elif i == "Queen":
        print ("Queen is very cute")
    else:
         print ("one of the best horses is" + i)



horseshows = []

while true:
    print("What horse show do you like? Type 'end' to quit.")
    answer = input ()

    if answer == "end":
        break
    else:
        horseshows. append(answer)

for i in movies:
    print("One of your favorites is" + i)
