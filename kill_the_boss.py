import random
import time
while True:
    health=200
    print("="*90)
    print(" ⚔️ MONSTER BATTLE ⚔️".center(90))
    print("="*90)
    print(' Defeat the Boss "SUPERMAN" to Save the Kingdom!'.center(90))
    print("Kill The Boss Without Dying To Win".center(90))
    boss_health=650
    print("="*90)
    time.sleep(2)
    character=["Goblin", "Skeleton", "Zombie", "Dragon"]
    print("The characters option are: ")
    time.sleep(1)
    for i in range(len(character)):
        print(i+1, character[i])
        time.sleep(1)
    print()
    choice=input("Do you want to choose your character or let the computer choose for you? (y/n): ")
    print()
    while True:
        if choice.upper()=="N":
            random_character=random.choice(character)
            time.sleep(1)
            print("The computer has chosen: ", random_character)
            break
        elif choice.upper()=="Y":
            user_character=input("Which character do you want to choose?(1/2/3/4)? ")
            if user_character in ["1","2","3","4"]:
                time.sleep(1)
                print("You have chosen: ", character[int(user_character)-1])
                break
            else:
                print("Invalid choice. Please choose a valid character number (1-4).")
        else:
            print("Invalid choice")
            choice=input("Do you want to choose your character or let the computer choose for you? (y/n): ")
            time.sleep(1)
    print("Health of your character is: ", health,"❤️")
    for i in range(3):
        print("The earth is shaking!"+"!"*i)
        print()
        time.sleep(1)
    print("-"*90)
    print("The Boss has appeared!".center(90))
    print(f"Superman's Health: {boss_health}".center(90))
    print("-"*90)
    while health>0 and boss_health>0:
        option=["Attack","Heal","your status","Run"]
        for i in range(len(option)):
            print(i+1, option[i])
        move=input("What do you want to do? (1/2/3/4): ")
        print("-"*90)
        if move=="1":
            damage=random.randint(50,70)
            boss_health-=damage
            print("You attacked the Superman!")
            time.sleep(1)
            print(f"damage dealt: {damage}")
            time.sleep(1)  
            if boss_health<=0:
                print("You have defeated the boss!")
            else:
                print(f"Superman's HP: {boss_health}")
            print()
            if boss_health<=0:
                break
            print("superman attacks you!")
            time.sleep(1)
            boss_damage=random.randint(15,30)
            health-=boss_damage
            print(f"damage taken: {boss_damage}")
            time.sleep(1)
            if health<=0:
                for i in range(3):
                    print("🩸","."*i, end="" )
                    time.sleep(1)
                print("You have been defeated by the boss!")
                break
            else:
                print(f"your health: {health}")
            print("-"*90)
            if boss_health<=0:
                print("Superman is dead!!  You have won the battle!".center(90))
                time.sleep(1)
            else:
                print(f"Superman's Health: {boss_health}".center(90))
                time.sleep(1)
            print("-"*90)
            time.sleep(1)
        elif move=="2":
            if health>=200:
                print("You are already at full health!")
                time.sleep(1)
                print("superman attacks you!")
                time.sleep(1)
                boss_damage=random.randint(5,15)
                health-=boss_damage
                print(f"your health is now: {health}")
                time.sleep(1)
                print("-"*90)
            else:
                heal=random.randint(30,60)
                health+=heal
                print("You healed yourself!")
                if health>200:
                    health=200
                print(f"your health: {health}")
                time.sleep(1)
                print()
                print("superman attacks you!")
                time.sleep(1)
                boss_damage=random.randint(5,15)
                health-=boss_damage
                print(f"your health is now: {health}")
                time.sleep(1)
                print("-"*90)
        elif move=="3":
            print("="*90)
            print("YOUR STATUS".center(90))
            time.sleep(1)
            print(f"Health Of Your Character: {health}/200".center(90))
            time.sleep(1)
            print()
            print()
            print("BOSS STATUS".center(90))
            time.sleep(1)
            print("Boss: Superman".center(90))
            time.sleep(1)
            print(f"health: {boss_health}/650".center(90))
            time.sleep(1)
            print("="*90)
        elif move=="4":
            print("You ran away from the battle!")
            time.sleep(2)
            print()
            print("#"*90)
            print("GAME OVER".center(90))
            time.sleep(1)
            print("#"*90)
            print("You ran away from the battle and lost the game!")
            print("Superman has taken over the kingdom and you have failed to save it!")
            time.sleep(1)
            print("-"*90)
            exit()
        else:
            print("Invalid option! Choose 1, 2, 3, or 4.")
    if health<=0:
        print()
        print("#"*90)
        time.sleep(1)
        print("GAME OVER".center(90))
        time.sleep(1)
        print("#"*90)
        print()
        print("superman has defeated you and taken over the kingdom!")
        print("You have failed to save the kingdom!")
        print("Better luck next time!")
        time.sleep(1)
        break 
    elif boss_health<=0:
        print()
        print("#"*90)
        time.sleep(1)
        print("YOU WIN!".center(90))
        time.sleep(1)
        print("#"*90)
        print()
        print("You have defeated the boss and saved the kingdom!")
        print("Congratulations!")
        print("You are a true hero!")
        print("Thank you for playing the game!")
        time.sleep(1)
        break
