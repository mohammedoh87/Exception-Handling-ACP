try:
    age = int(input("How old are you? "))
    if age < 0:
        print("ERROR!! Please enter a positive integer")
    if age > 0:    
        if age % 2 == 0:
            print("Your age is even")
        else:
            print("Your age is odd")
except ValueError:
    print("INVALID INPUT")