command = ""
cstart=0
cstop=0

while True:
    command = input("> ").lower()

    if command == "start":
        if cstart==0:

            print("car started")
            cstart+=1
        else:
            print("car is already started")
    elif command == "stop":
        if cstop==0:

            print("car stopped")
            cstop+=1
        else:
            print("Car is already stopped")
    elif command == "help":
        print("""
start - start the car
stop - stop the car
quit - close program
""")
    elif command == "quit":
        print("Exiting program...")
        break
    else:
        print("Invalid command. Type 'help' for available commands.")
