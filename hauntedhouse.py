import sys
import time

def typewriter_effect(sentence):
    # Loop through each character and print the sentence
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)

    time.sleep(1)
    print('\n')

def intro():
    a = (r"""
             _    _         _    _ _   _ _______ ______ _____    _    _  ____  _    _  _____ ______ 
            | |  | |   /\  | |  | | \ | |__   __|  ____|  __ \  | |  | |/ __ \| |  | |/ ____|  ____|
            | |__| |  /  \ | |  | |  \| |  | |  | |__  | |  | | | |__| | |  | | |  | | (___ | |__   
            |  __  | / /\ \| |  | | . ` |  | |  |  __| | |  | | |  __  | |  | | |  | |\___ \|  __|  
            | |  | |/ ____ | |__| | |\  |  | |  | |____| |__| | | |  | | |__| | |__| |____) | |____ 
            |_|  |_/_/    \_\____/|_| \_|  |_|  |______|_____/  |_|  |_|\____/ \____/|_____/|______|
                                                                                                    
                                                                                         """)
    print(a)
    
    time.sleep(2)
    typewriter_effect("The haunted manor looms before you, a colossal structure that seems to defy time itself. The sky above is a perpetual twilight, shrouded in thick, swirling clouds that cast the landscape in a gloomy, muted light. The air is heavy, carrying the scent of damp earth and decaying wood, mingled with an indescribable feeling of dread that seeps into your bones. ")
    typewriter_effect("The manor's exterior is a twisted amalgamation of architectural styles, as if it had been built and rebuilt over centuries, each new addition more warped and decayed than the last. The walls are made of dark, weathered stone, stained by years of neglect and the relentless passage of time. Ivy creeps up the sides, its leaves blackened and brittle, as though even the plants are cursed by the manor's malevolence. Tall, narrow windows, their glass cracked or missing entirely, stare out like empty eyes, revealing nothing of the horrors within. ")
    time.sleep(2)
    typewriter_effect("The front of the manor is dominated by a massive, arched entrance, its heavy wooden doors carved with grotesque figures and symbols, worn smooth by countless years of exposure to the elements. The doors are slightly ajar, creaking on rusted hinges as they sway in the wind, inviting you—or perhaps daring you—to step inside. Flanking the entrance are a pair of twisted, dead trees, their gnarled branches reaching out like skeletal hands, as if trying to pull you in. ")
    a = (r"""
        
       

                                        ███                     
                                    █▓▓█████▓▓█                 
                                █▓██████░██████▓█              
                            █▓▓██████░░░░░░░██████▓▓█          
                        █▓██████░░░░░█▒▒▒█░░░░░██████▓█       
                    █▓▓█████░░░░░░░░▒█░▓░█▒░░░░░░░▒█████▓▓█   
                    █▓██████░░░░░░░░░░░▒█░▓░█▒░░░░░░░░░░░██████▓█
                        ░░░░░░░░░░░░░░░█▒▒▒█░░░░░░░░░░░░░░░     
                        ░░░░░░░░░░░░░█████████░░░░░░░░░░░░░     
                        ░░░▒▒▒▒▒▒▒░░░██▓▓▒▓▓██░░░▒▒▒▒▒▒▒░░░     
                        ░░░▒░█▓░░▒░░░██▓▓▒▓▓██░░░▒▒░▓█░▒░░░     
                        ░░░▒░░▓░░▒░░░██▓▓▒▓▓██░░░▒░░▓░░▒░░░     
                        ░░░▒▓▓▓▓▓▒░░░██▓▓▒▓▓██░░░▒▓▓▓▓▓▒░░░     
                        ░░░▒░░▓░░▒░░░██▒▒▒▒▒██░░░▒░░▓░░▒░░░     
                        ░░░▒░░▓░░▒░░░██▓▓▒▓▓██░░░▒░░▓░░▒░░░     
                        ▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒     
                        ▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒     
                        █▓▓█▓▓█▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓█▓▓█▓▓█    
                        █▓▓█▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█▓▓█    
                                ▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓              

  


        """)
    print(a)
    typewriter_effect("Do you dare enter this haunted manor? ")
    
    while True:
        choice = input("Do you enter? 'y' or 'n': ")
        choice = choice.lower()
        if choice == "y":
            room1()
            break
        elif choice == "n":
            intro()
            break
        else: 
            print("Invalid choice. Please enter 'y' or 'n'. ")

def room1():
    typewriter_effect("As you step into the dusty entrance hall of the first room of the house, the door creaks shut behind you. A thin layer of cobwebs clings to every surface, and the air is thick with the smell of damp and decay. ")
    time.sleep(2)
    typewriter_effect("Your footsteps echo ominously as you approach the fork in the hallway. ")
    time.sleep(2)
    typewriter_effect("To your left, the hallway seems to stretch on forever, shrouded in darkness. ")
    time.sleep(2)
    typewriter_effect("To your right, a heavy wooden door stands closed, its paint chipped and peeling. A faint, flickering light seeps out from underneath, providing the only source of warmth in this cold, abandoned house. ")
    time.sleep(2)
    typewriter_effect("As you stand there, deciding which way to go, you hear a soft, eerie whisper from the darkness to your left. It's impossible to make out the words, but the sound sends shivers down your spine. ")
    typewriter_effect("You turn your attention to the heavy wooden door on your right, its flickering light beckoning you. As you approach, you notice that the door isn't just closed, but locked as well. The sound of the whispering seems to grow louder, more insistent, as if trying to dissuade you from investigating further. ")
    
    while True:
        choice = input("Which door will you take? 'left' or 'right': ")
        choice = choice.lower()
        if choice == "left":
            room2()
            break
        elif choice == "right":
            hallway()
            break
        else: 
            print("Invalid choice. Please enter 'left' or 'right'. ")

def hallway():
    typewriter_effect("Curiosity wins over caution, and you step into the hallway. The walls here are close, the air thick with the scent of mildew and dust. The farther you go, the more the hallway seems to narrow, the shadows closing in as if trying to swallow you whole. The floor beneath your feet shifts slightly with each step, as though the manor itself is alive and responding to your presence. ")
    time.sleep(2)
    typewriter_effect("The hallway bends and twists in ways that defy logic, the turns becoming sharper, the walls seeming to pulse with a faint, eerie glow. You press on, your heart pounding in your chest, as the disorienting path draws you deeper into the darkness. The sounds of the manor—the distant creaks, the faint whispers—grow muffled, as if you’re being drawn into a world apart from the one you left behind. ")
    time.sleep(2)
    typewriter_effect("After what feels like an eternity, you see a faint light ahead. Relief washes over you, and you quicken your pace, eager to escape the suffocating corridor. As you reach the light, the hallway opens up into a familiar space. ")
    time.sleep(2)
    typewriter_effect("You freeze in place as realization dawns on you. ")
    time.sleep(2)
    typewriter_effect("You are back at the entrance of the house. ")
    intro()
    
def room2():
    a = (r"""
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▒▓▓▓▓
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▒▒▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▒▒▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        """)
    print(a)
    typewriter_effect("As you step through the doorway, the flickering light reveals a small room, cluttered with dusty furniture and forgotten knick-knacks. ")
    time.sleep(2)
    typewriter_effect("A grandfather clock ticks away in the corner, its pendulum swinging back and forth with a hypnotic rhythm. In the center of the room, a small table holds a candle, its flame dancing and casting shadows on the walls. The room seems to be a makeshift study, with stacks of yellowed books and scattered papers covering every surface. ")
    time.sleep(2)
    typewriter_effect(" You come to a stop at another fork in the hallway, unsure of which path to take. You have two options: a door to your left leading to a maze of narrow corridors, and a set of stairs to your right that ascend to the upper floor. You strain your ears, trying to catch any sound that might give you a clue as to which way to go. ")
    typewriter_effect("And to your left there is a door ")
    time.sleep(2)
    typewriter_effect("Which one do you take? ")
    
    while True:
        choice = input("Which path will you take? 'left' or 'right': ")
        choice = choice.lower()
        if choice == "left":
            trapdoor()
            break
        elif choice == "right":
            room3()
            break
        else: 
            print("Invalid choice. Please enter 'left' or 'right'. ")

def trapdoor():
    typewriter_effect("With a deep breath, you grasp the iron ring and pull. The door creaks open, revealing a dark, narrow staircase descending into the depths below. The air that wafts up from the opening is cold and musty, carrying with it the faint scent of earth and something else—something old and forgotten. The darkness below feels oppressive, as if it’s hiding secrets that were meant to stay buried. ")
    time.sleep(2)
    typewriter_effect("You take a moment to steel yourself before descending the stairs, your hand trailing along the damp, rough walls for balance. Each step echoes ominously, the sound swallowed by the blackness around you. The deeper you go, the more the air seems to thicken, weighing down on your chest and making it hard to breathe. ")
    time.sleep(2)
    typewriter_effect("After what feels like an eternity, you reach the bottom of the stairs. Your eyes strain to see in the pitch darkness, but slowly, as your vision adjusts, you make out the faint outlines of a narrow passageway ahead. The floor is uneven, and you can feel the cold stone beneath your feet. The passage twists and turns, each bend bringing with it a growing sense of dread. ")
    time.sleep(2)
    typewriter_effect("Finally, you see a faint light ahead, a soft glow that seems to beckon you forward. Relief floods through you as you hurry towards it, eager to escape the claustrophobic darkness. As you step into the light, the passageway opens up into a familiar room. ")
    typewriter_effect("You freeze in place as realization dawns on you. ")
    time.sleep(2)
    typewriter_effect("You are back at the entrance of the house. ")
    intro()
    
    
def room3():
    a = (r"""
                         
                                                    ▓▓▓▓▓             ▓▓▓█▓                              
                                                    █▓▓▓█▓▓           ▓▓▓▓█▓▓                              
                                                ▓▓▓▓█▓▓▓▓         █▓▓▓▓▓█▓▓                              
                                                ▓▓▓▓██░▓▓▓▓        ▓▓▓▓▓▓▓█▓▓                              
                                            █▓▓▓▓ ▓▓█▒▓▓▓▓       ▓▓▓▓▓▓▓▓█▓▓                              
                                            ▓▓▓▓█▓  ▓▓█▒▓▓        ▓▓▓▓▓▓▓▓▓                                 
                                        ▓▓▓▓  ▓▓  ▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                
                                        ▓▓▓▓▓▓  ▓▓  ▓▓█         ▓▓▓█▓▓▓▓▓                                   
                                    ▓▓▓▓ ▓▓▓  ▓▓              ▓▓▓▓▓▓▓                                     
                                    ▒▓▓▓▓  ▓▓▓  ▓▓██████████████▓▓▓▓▓▓▓                                     
                                ▓▓▓▓▓▓  ▓▓▓                  ▓▓▓▓▓                                       
                                ▓▓▓▓ ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓                                       
                                ▓▓▓▓▓ ▓▓                        ▓▓▓█                                       
                                ▓▓▓▓▓▓ ▓▓                        ▓▓▓▓▓                                      
                            █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                            ▓▓▓▓▓▓▓                           ▓▓▓▓░▓▓▓▓                                  
                            ▓▓▓▓█▓▓▓                           ▓▓▓▓ ░▓▓▓▓▓                                
                        ░▓█▓▓▓▓█▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ░▓▓ ▓▓▓▓▓▓                            
                        ▓▓▓▓█▓▓▓█▓                              ▓▓▓ ░▓▓   ▓█▓▓▓▓▓▓▓▓▓█                    
                        █▓▓▓█▓▓▓█▓                              ▓▓▓ ░▓▓   ▓▓█    █▓▓██                    
                        █▓▓▓█▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███ ░▓▓   ▓▓█    █▓▓▓▓                    
                        █▓▓▓█▓▓▓░                                   ░▓▓   ▓▓█    █▓▓▓▓                    
                        █▓▓▓█▓▓▓░                                   ░▓▓   ▓▓▓    █▓▓▓▓                    
                        █▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓   ▓▓█    █▓▓▓▓                    
                        █▓▓▓█▓▓                                           ▓▓█    █▓▓▓▓                    
                        █▓▓▓█▓▓                                           ▓▓█    █▓▓▓▓                    
                        █▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████   █▓▓▓▓                    
                        █▓▓▓█                                                    █▓▓▓▓                    
                        █▓▓▓█                                                    █▓▓▓▓                    
                        █████                                                    █▓▓▓▓                    
                                                                                    
        """)
    print(a)
    
    typewriter_effect(" As you cautiously approach the staircase, the scraping noise grows louder, more persistent. You can't quite tell what's causing it, but it seems to be coming from the upper floor. You grip the railing, its cold, rough surface sending another shiver down your spine, and begin to ascend the stairs. ")
    time.sleep(2)
    typewriter_effect("With every step, the air grows colder, and you can feel the weight of the house pressing down on you. The staircase seems to stretch on forever, each creak and groan of the wood beneath your feet echoing like a mournful wail. Your breath comes in short gasps, the cold air searing your lungs. As you reach the top, you find yourself in a narrow hallway with three doors. ")
    typewriter_effect("To your left, a door painted a sickly shade of green stands slightly ajar, revealing nothing but darkness beyond. In the center, a door with ornate carvings seems to hum with an unseen energy. To your right, a door made of heavy, weathered wood is closed tightly, its handle glinting in the dim light. ")
    
    while True:
        choice = input("Which door will you choose? 'left', 'middle', or 'right': ")
        choice = choice.lower()
        if choice == "left":
            hazard1()
            break
        elif choice == "middle":
            hazard1()
            break
        elif choice == "right":
            room4()
            break
        else: 
            print("Invalid choice. Please enter 'left', 'middle', or 'right'.")

def room4():
    a = (r"""
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
        ░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█░░░░░░▓████████▒▓█▓▓▓▓▓▓▓█░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█░░░░░░░░░░░░ 
        ░░░░░░░░░░▒▓▓██████████████▓▓█░░░░░░▓████████▒▓▓▓▓▓▓▓▓▓█░░░░░░░▒▓▓██████████████▓▓█░░░░░░░░░░░░ 
        ░░░░░░░░░░▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█░░░░░░▓████████▓▓▓▓▓▓▓▓▓▓█░░░░░░░▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█░░░░░░░░░░░░ 
        ░░░░░░░░░░▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█░░░░░░▓████████▓▓▓▓▓▓▓▓▓▓█░░░░░░░▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█░░░░░░░░░░░░ 
        ░░░░░░░░░░▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█░░░░░░▓████████▓▓▓▓▓▓▓▓▓▓█░░░░░░░▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█░░░░░░░░░░░░ 
        ░░░░░░░░░░▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█░░░░░░▓████████▓▓▓▓▓▓▓▓▓▓█░░░░░░░▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█░░░░░░░░░░░░ 
        ░░░░░░░░░░▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█░░░░░░▓████████▓▓▓▓▓▓▓▓▓▓█░░░░░░░▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█░░░░░░░░░░░░ 
        ░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█░░░░░░▓████████▓  ▓▓▓▓▓▓▓█░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█░░░░░░░░░░░░ 
        ▒▒▒▒▒▒▒▒▒░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▓████████▓  ▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒ 
        ▒▒▒▒▒▒▒▒▒░▒▓▓█████████████▓▓▓█▒▒▒▒▒▒▓████████▓  ▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▓▓█████████████▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒ 
        ▒▒▒▒▒▒▒▒▒▒▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█▒▒▒▒▒▒▓████████▓▓▓▓▓▓▓▓█▓█▒▒▒▒▒▒▒▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█▒▒▒▒▒▒▒▒▒▒▒▒ 
        ▒▒▒▒▒▒▒▒▒▒▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█▒▒▒▒▒▒▓████████▓▓█▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█▒▒▒▒▒▒▒▒▒▒▒▒ 
        ▒▒▒▒▒▒▒▒▒▒▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█▒▒▒▒▒▒▓████████▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█▒▒▒▒▒▒▒▒▒▒▒▒ 
        ▒▒▒▒▒▒▒▒▒▒▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█▒▒▒▒▒▒▓████████▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█▒▒▒▒▒▒▒▒▒▒▒▒ 
        ▒▒▒▒▒▒▒▒▒▒▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█▒▒▒▒▒▒▓████████▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█▒▒▒▒▒▒▒▒▒▒▒▒ 
        ▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▓████████▓▓▓▓▓▓▓▒▓▓█▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒ 
        ██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████▓████████▓▓▓▒▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████ 
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████████ 
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
                                                                                                 
         """)
    print(a)
    typewriter_effect("The door swings open with a loud creak, and you step into the room beyond. The air is cold and heavy, and you feel a chill run down your spine. The room is dimly lit by a single flickering candle on a small table. The walls are lined with dusty bookshelves, filled with ancient tomes and forgotten scrolls. ")
    time.sleep(2)
    typewriter_effect("Three more doors now stand before you, one on the left, one in the middle, and one on the right. ")
    
    while True:
        choice = input("Which door will you choose? 'left', 'middle', or 'right': ")
        choice = choice.lower()
        if choice == "left":
            hazard2()
            break
        elif choice == "middle":
            hazard2()
            break
        elif choice == "right":
            room5()
            break
        else: 
            print("Invalid choice. Please enter 'left', 'middle', or 'right'.")

def room5():
    a = (r"""
         __     ______  _    _   ______  _____  _____          _____  ______ _____  
         \ \   / / __ \| |  | | |  ____|/ ____|/ ____|   /\   |  __ \|  ____|  __ \ 
          \ \_/ | |  | | |  | | | |__  | (___ | |       /  \  | |__) | |__  | |  | |
           \   /| |  | | |  | | |  __|  \___ \| |      / /\ \ |  ___/|  __| | |  | |
            | | | |__| | |__| | | |____ ____) | |____ / ____ \| |    | |____| |__| |
            |_|  \____/ \____/  |______|_____/ \_____/_/    \_|_|    |______|_____/ 
    """)
    print(a)
    typewriter_effect("Congratulations! You have escaped the haunted house. ")
    typewriter_effect("You step out into the fresh air, feeling the weight of the house lift from your shoulders. ")
    typewriter_effect("You vow never to return to this place again. ")
    time.sleep(5)
    print("Thanks for playing, game will close in 15 seconds.")
    time.sleep(15)
    exit()

def hazard1():
    typewriter_effect("You find yourself in a dark room, with no way out. You feel a presence in the room, but you can't see it. You try to find a way out, but it's too late. The darkness consumes you. ")
    a = (r"""
          _____          __  __ ______    ______      ________ _____  
         / ____|   /\   |  \/  |  ____|  / __ \ \    / |  ____|  __ \ 
        | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
        | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
        | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
         \_____/_/    \_|_|  |_|______|  \____/   \/   |______|_|  \_\
                                                               
          """)
    print(a)
    time.sleep(5)
    print("Thanks for playing, game will close in 15 seconds.")
    time.sleep(15)
    exit()

def hazard2():
    typewriter_effect("You enter a room and suddenly the floor gives way beneath you. You fall into a pit of spikes. ")
    a = (r"""
          _____          __  __ ______    ______      ________ _____  
         / ____|   /\   |  \/  |  ____|  / __ \ \    / |  ____|  __ \ 
        | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
        | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
        | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
         \_____/_/    \_|_|  |_|______|  \____/   \/   |______|_|  \_\
                                                               
          """)
    print(a)
    time.sleep(5)
    print("Thanks for playing, game will close in 15 seconds.")
    time.sleep(15)
    exit()

intro()
