is_started = False
while True:
    inputvalue = input(">")
    if(inputvalue.lower() == "help"):
        print("""
Start -- to start the car
Stop - to stop the car")
quit - to terminate""")
    elif(inputvalue.lower() == "start"):
        if is_started:
            print("car has already started !!!")
        else:
            print("Car started - Ready to go")
            is_started= True
    elif(inputvalue.lower() == "stop"):
        if not is_started:
            print("car has already stopped !!!")
        else:
            print("Car stopped.")
            is_started = False
    elif(inputvalue.lower() == "quit"):
        print("Terminating ...")
        break
    else:
        print("I don't understand !!!")