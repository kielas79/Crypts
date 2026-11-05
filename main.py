print("Commands must be written exactly as shown.")
# 'filler' means it's yet to be filled with real text
while True:
    choice = input("Type 'start' to begin. type 'stop' to close \n"
    "If you're seeing this message again, it means your input was erroneus. \n ")
    if choice == "start":
        import world_data
        import time
        key = False
        metal_door_unlocked = False
        print_delay = 3
        greater_print_delay = 5
        sleep_delay = 7
        print("==================================================")
        print("                    THE CRYPT                     ")
        print("==================================================")
        time.sleep(3)
        while True:
            print("Current room: ???")
            time.sleep(1.5)
            print("filler text \nYou look around you...")
            time.sleep(print_delay)
            print(world_data.rooms["start"]["desc"])
            time.sleep(print_delay)
            while True:
                choice = input(f"Where do you wish to go? \n Available paths: \n {world_data.rooms["start"]["paths"]}\n")
                if choice == "door":
                    print("You walk up to the rusty door")
                    time.sleep(2)
                    if key == True:
                        metal_door_unlocked = True
                        key = False
                        print("You introduce the key... and it turns. \n (type door again)")
                    if metal_door_unlocked == True:
                        print("filler")   
                    else:
                        print("You twist the knob...")
                        time.sleep(1)
                        print("The door is locked. \nYou fell a little bit into desperation, knowing this door is the only exit")
                        break
                if choice == "bed":
                    time.sleep(1)
                    print("You walk up to the bed")
                    time.sleep(3)
                    if key == False and metal_door_unlocked == False:
                        print("As you neared the bed, you let out a yawn, already tired from what was happening")
                        time.sleep(print_delay)
                        print("You laid out in the bed, thinking about everything.")
                        time.sleep(print_delay)
                        print("For some reason, the room felt familiar, even though you've never seen this room before.")
                        time.sleep(print_delay)
                        print("You quickly fell asleep...")
                        time.sleep(sleep_delay)
                        print("filler")
                        key == True
                        time.sleep(3)
                        break
                    elif key == True:
                        print("Nothing else around here... \n (You already have the key!)")
                        time.sleep(2)
                        break
                    elif key == False and metal_door_unlocked == True:
                        print("Now's not a good time to rest... \n I should go see what's behind the door")
                        time.sleep(2)
                        break
                    else:
                        print("bug warning")
                        break

                else:
                    print("That's not an option")
                    time.sleep(1.5)
                    break
        
    elif choice == "stop":
        break
    else:
        continue
