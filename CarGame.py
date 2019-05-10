index = ""
while True:
    inputvalue = input(">")
    if(inputvalue.lower() == "help"):
        print("""
Start -- to start the car
Stop - to stop the car
quit - to terminate""")
    elif(inputvalue.lower() == "start"):
        if(index == "start"):
            print("car has already started !!!")
        else:
            print("Car started - Ready to go")
            index="start"
    elif(inputvalue.lower() == "stop"):
        if(index == "stop"):
            print("car has already stopped !!!")
        else:
            print("Car stopped.")
            index = "stop"
    elif(inputvalue.lower() == "quit"):
        print("Terminating ...")
        break
    else:
        print("I don't understand !!!")