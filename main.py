print("Commands must be written exactly as shown.")
while True:
    choice = input("Type 'start' to begin. type 'stop' to close \n"
    "If you're seeing this message again, it means your input was wrong. \n ")
    if choice == "start":
        import world_data
        print("==================================================")
        print("                    THE CRYPT                     ")
        print("==================================================")
        print("filler text")
        print("You look around you...")
        

    elif choice == "stop":
        break
    else:
        continue
