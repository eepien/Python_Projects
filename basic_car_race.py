car_command = ""
print("Enter car command: start, stop, quit or help below ")
while  car_command != "quit":
    car_command = input(">").lower()                             # .lower() converts all input to lowercase.
    if car_command == "start":
        print("Car started...Ready to go!")
    elif car_command == "stop":
        print("Car Stopped.")
    elif car_command =="help":
        print("""
        start - to start the car                             
        stop - to stop the car
        quit - to quit
        """)                                                    #Note that we can remove the double indentation
    elif car_command.lower() =="quit":
        break
    else:
        print("Sorry I don't understand that!")
#see version 2 of the program that does exactly the same thing below:
