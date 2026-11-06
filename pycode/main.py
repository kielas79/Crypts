print("Commands must be written exactly as shown.")
# 'filler' means it's yet to be filled with real text
while True:
    choice = input("Type 'start' to begin. type 'stop' to close \n"
    "If you're seeing this message again, it means your input was erroneus. \n ")
    if choice == "start":
        import world_data
        import time
        import sys
        def text_config(text, speed=0.04, line_pause=1.5):
            # Above is default speed ^ and here is the ^ delay between lines
            # This function was made by ai, but the rest is done by me
            for letter in text:
                sys.stdout.write(letter)
                sys.stdout.flush()
                if letter == "\n":
                    time.sleep(line_pause)
                else:
                    time.sleep(speed)        
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
            text_config(text=f"Current room: ???\nfiller text\nYou look around you...\n{world_data.rooms["start"]["desc"]}")
            while True:
                choice = input(text_config(text=f"\nWhere do you wish to go? \n Available paths: \n {world_data.rooms["start"]["paths"]}"))
                if choice == "door":
                    text_config(text="\nYou walk up to the rusty door\n")
                    if key == True:
                        metal_door_unlocked = True
                        key = False
                        text_config(text="You introduce the key... and it turns. \n (type door again)\n")
                    if metal_door_unlocked == True:
                        text_config(text="filler\n")   
                    else:
                        text_config(text="\nYou twist the knob...\nThe door is locked.\nYou fell a little bit into desperation,knowing this door is the only exit\n")
                        break
                if choice == "bed":
                    text_config(text="\nYou walk up to the bed")
                    if key == False and metal_door_unlocked == False:
                        text_config(text="\nAs you neared the bed, you let out a yawn, already tired from what was happening\nYou laid out in the bed, thinking about everything.\nFor some reason, the room felt familiar, even though you've never seen this room before.\nfiller\n")
                        text_config(text="You quickly fell asleep...\n", line_pause=5, speed=0.01)
                        key == True
                        break
                    elif key == True:
                        text_config(text="\nNothing else around here... \n(You already have the key!)\n")
                        break
                    elif key == False and metal_door_unlocked == True:
                        text_config(text="\nNow's not a good time to rest... \n I should go see what's behind the door\n")
                        break
                    else:
                        print("bug warning")
                        break

                else:
                    text_config(text="That's not an option")
                    break
        
    elif choice == "stop":
        break
    else:
        continue
