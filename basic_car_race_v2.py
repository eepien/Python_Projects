
#Car reminds user if state is a repeat.
car_command = ""
started = False
print("Enter car command: start, stop, quit or help below ")
while  True:
    car_command = input(">").lower()
    if car_command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif car_command == "stop":
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car Stopped.")
    elif car_command =="help":
        print("""
start - to start the car                             
stop - to stop the car
quit - to quit
        """)
    elif car_command.lower() =="quit":
        break
    else:
        print("Sorry I don't understand that!")