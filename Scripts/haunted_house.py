import sys
import time

def print_slowly(text, delay=0.03):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def introduction():
    print_slowly("\nWelcome to the Haunted House!")
    print_slowly("Your goal is to find the hidden treasure.")
    print_slowly("Explore the house by moving through its floors and rooms.\n")
    print_slowly("-------------------------------------------------------------")

def floor_1():
    available_rooms = ['Living Room', 'Kitchen', 'Dining Room']
    while available_rooms:
        print_slowly("\nYou are on the first floor. Which room do you want to explore?")
        for index, room in enumerate(available_rooms, start=1):
            print_slowly(f"{index}. {room}")
        choice = int(input("Enter the number of your choice: "))
        if choice < 1 or choice > len(available_rooms):
            print_slowly("\nInvalid choice. Try again.")
        else:
            room = available_rooms.pop(choice - 1)
            print_slowly(f"\nYou enter the {room}.")
            if room == 'Living Room':
                print_slowly("The room is dark and cold, but you find nothing unusual.")
                print_slowly("Suddenly, the candles on the fireplace light up on their own!")
                print_slowly("You gasp and think, 'Could it be a draft? It's still eerie...'")
            elif room == 'Kitchen':
                print_slowly("Old pots and pans are scattered on the floor, but there's no treasure.")
                print_slowly("A gust of wind blows through the room, and the cupboard doors start banging!")
                print_slowly("You shudder, 'It must be the wind, right? Still, it's unsettling...'")
            elif room == 'Dining Room':
                print_slowly("The table is set for dinner, but there's no one around.")
                print_slowly("You hear footsteps approaching, but no one appears.")
                print_slowly("You feel uneasy, 'Old houses make strange noises, right? I hope that's all it is...'")
            print_slowly("-------------------------------------------------------------")
    print_slowly("\nYou have explored all the rooms on the first floor.")
    floor_2()

def floor_2():
    available_rooms = ['Master Bedroom', 'Guest Room', 'Library']
    while available_rooms:
        print_slowly("\nYou are on the second floor. Which room do you want to explore?")
        for index, room in enumerate(available_rooms, start=1):
            print_slowly(f"{index}. {room}")
        choice = int(input("Enter the number of your choice: "))
        if choice < 1 or choice > len(available_rooms):
            print_slowly("\nInvalid choice. Try again.")
        else:
            room = available_rooms.pop(choice - 1)
            print_slowly(f"\nYou enter the {room}.")
            if room == 'Master Bedroom':
                print_slowly("The bed looks like someone just slept in it, but there's no treasure.")
                print_slowly("The mirror on the wall suddenly shatters!")
                print_slowly("You jump in shock, 'It must be due to the temperature change...or is it?'")
            elif room == 'Guest Room':
                print_slowly("An old trunk sits in the corner. You open it, it contains an old newspaper from 1865. It Reads - Foster Home takes in kids off the streets... a sight to see! -")
                print_slowly("The room temperature drops, and you see your breath in the air.")
                print_slowly("You shiver and think, 'The insulation must be terrible in this old house.'")
            elif room == 'Library':
                print_slowly("Books line the walls, but you find nothing valuable.")
                print_slowly("A book flies off the shelf and lands on the floor with a thud.")
                print_slowly("You feel your heart race, 'Could it be the wind? This is really strange... you check the book and it is labeled - Granger Foster Home- with a publication date of March 12, 1865 -'")
            print_slowly("-------------------------------------------------------------")
    print_slowly("\nYou have explored all the rooms on the second floor.")
    floor_3()

def floor_3():
    available_rooms = ['Attic']
    secret_room_unlocked = False

    while available_rooms:
        print_slowly("\nYou are on the third floor. Which room do you want to explore?")
        for index, room in enumerate(available_rooms, start=1):
            print_slowly(f"{index}. {room}")
        choice = int(input("Enter the number of your choice: "))
        if choice < 1 or choice > len(available_rooms):
            print_slowly("\nInvalid choice. Try again.")
        else:
            room = available_rooms.pop(choice - 1)
            print_slowly(f"\nYou enter the {room}.")
            if room == 'Attic':
                print_slowly("The attic is full of dusty boxes and cobwebs. You see a locked door.")
                print_slowly("A cold breeze suddenly blows through the room, making you shiver.")
                print_slowly("You think, 'I have to check behind that door, but I'm not looking forward to it.'")

                failed_attempts = 0
                while not secret_room_unlocked and failed_attempts < 3:
                    code_attempt = int(input("Enter the code to unlock the door: "))
                    if code_attempt == 1865:
                        secret_room_unlocked = True
                        print_slowly("The door unlocks!")
                        available_rooms.append('Secret Room')
                    else:
                        failed_attempts += 1
                        print_slowly("Incorrect code. The door remains locked.")
                        if failed_attempts < 3:
                            print_slowly(f"You have {3 - failed_attempts} attempts remaining.")
                if not secret_room_unlocked:
                    print_slowly("You've failed to unlock the door 3 times.")
                    print_slowly("Suddenly, the room turns pitch black, and an oppressive, suffocating darkness envelops you.")
                    print_slowly("A cacophony of anguished screams and demonic laughter fills your ears, driving you to the brink of madness.")
                    print_slowly("The walls close in, pulsating like the flesh of some grotesque, monstrous creature.")
                    print_slowly("You feel a million icy fingers clawing at your skin, tearing away at your very soul.")
                    print_slowly("A horrifying, indescribable entity appears before you, its twisted visage a nightmare beyond your darkest fears.")
                    print_slowly("You feel your sanity shatter as you're consumed by an eternity of unrelenting torment and despair.")
                    print_slowly("Your screams are forever lost in the abyss of the haunted house's darkest secrets.")
                    print_slowly("Game Over.")
                    sys.exit(0)
            elif room == 'Secret Room':
                print_slowly("You find the hidden treasure! Congratulations!")
                print_slowly("Thank you for playing the Haunted House game!")
                sys.exit(0)
            print_slowly("-------------------------------------------------------------")
    print_slowly("\nYou have explored all the rooms on the third floor, but you didn't find the treasure. Try again!")

def main():
    introduction()
    floor_1()

if __name__ == "__main__":
    main()