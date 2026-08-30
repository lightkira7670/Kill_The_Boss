import random
import time
while True:
    health=200
    print("="*90)
    print(" ⚔️ MONSTER BATTLE ⚔️".center(90))
    print("="*90)
    print(' Defeat the Boss "SUPERMAN" to Save the Kingdom!'.center(90))
    print("Kill The Boss Without Dying To Win".center(90))
    boss_health=500
    print("="*90)
    time.sleep(2)
    character=["👺 Goblin", "💀 Skeleton", "🧟 Zombie", "🐉 Dragon"]
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
            ur_character=random.choice(character)
            time.sleep(1)
            print("The computer has chosen: ", ur_character)
            break
        elif choice.upper()=="Y":
            user_character=input("Which character do you want to choose?(1/2/3/4)? ")
            if user_character in ["1","2","3","4"]:
                time.sleep(1)
                ur_character=character[int(user_character)-1]
                print("You have chosen: ", ur_character)
                break
            else:
                print("Invalid choice. Please choose a valid character number (1-4).")
        else:
            print("Invalid choice")
            choice=input("Do you want to choose your character or let the computer choose for you? (y/n): ")
            time.sleep(1)
    print("Health of your character is: ", health,"❤️")
    for i in range(3):
        print("🌎 The earth is shaking!"+"!"*i)
        time.sleep(1)
    print("-"*90)
    print("⚠️ THE BOSS HAS APPEARED! ⚠️".center(90))
    print("👹 SUPERMAN".center(90))
    print(f"❤️ Boss Health: {boss_health}/500".center(90))
    print("-"*90)
    while health>0 and boss_health>0:
        option=["⚔️ Attack","❤️ Heal","your status"," 🏃Run"]
        for i in range(len(option)):
            print(i+1, option[i])
        move=input("What do you want to do? (1/2/3/4): ")
        print("-"*90)
        if move=="1":
            damage=random.randint(50,70)
            boss_health-=damage
            print("⚔️ You attacked SUPERMAN!")
            time.sleep(1)
            print(f"💥 Damage dealt: {damage}")
            time.sleep(1)  
            if boss_health<=0:
                print("You have defeated the boss!")
            else:
                print(f"👹Superman's HP: {boss_health}")
            print()
            if boss_health<=0:
                break
            print("👹 SUPERMAN ATTACKS YOU!")
            time.sleep(1)
            boss_damage=random.randint(30,50)
            health-=boss_damage
            print(f"💥 Damage taken: {boss_damage}")
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
                print("👹 SUPERMAN is dead!!  You have won the battle!".center(90))
                time.sleep(1)
                break
            else:
                print(f"👹 SUPERMAN's Health: {boss_health}".center(90))
                time.sleep(1)
            print("-"*90)
            time.sleep(1)
        elif move=="2":
            if health>=200:
                print("You are already at full health!")
                time.sleep(1)
                print("👹 SUPERMAN attacks you!")
                time.sleep(1)
                boss_damage=random.randint(15,30)
                health-=boss_damage
                print(f"your health is now: {health}")
                time.sleep(1)
                print("-"*90)
            else:
                old_health=health
                heal=random.randint(30,60)
                health+=heal
                print("🧪 You used a healing potion!")
                time.sleep(1)
                if health>200:
                    health=200
                real_heal=health-old_health
                print(f"💚 Health restored: +{real_heal}")
                print(f"❤️ Your health: {health}/200")
                time.sleep(1)
                print()
                print("👹 SUPERMAN attacks you!")
                time.sleep(1)
                boss_damage=random.randint(15,30)
                health-=boss_damage
                print(f"your health is now: {health}")
                time.sleep(1)
                print("-"*90)
        elif move=="3":
            print("╔"+"═"*88+"╗")
            print("📊 YOUR STATUS".center(90))
            print("╠"+"═"*88+"╣")
            time.sleep(1)
            print(f"🧙 Character: {ur_character}".center(90))
            print(f"❤️ Health: {health}/200".center(90))
            time.sleep(1)
            print("╠"+"═"*88+"╣")
            time.sleep(1)
            print()
            print()
            print("👹 BOSS STATUS".center(90))
            time.sleep(1)
            print("👹 SUPERMAN".center(90))
            time.sleep(1)
            print(f"❤️ Boss Health: {boss_health}/500".center(90))
            print("╚"+"═"*88+"╝")
            time.sleep(1)
        elif move=="4":
            print("🏃 You are attempting to flee the battle!")
            confirm=input("Are you sure you want to run away? (y/n): ")
            if confirm.upper()=="Y":
                print("You ran away from the battle!")
                time.sleep(2)
                print()
                print("#"*90)
                print("GAME OVER".center(90))
                time.sleep(1)
                print("#"*90)
                print("You ran away from the battle and lost the game!")
                print("👹 SUPERMAN has taken over the kingdom and you have failed to save it!")
                time.sleep(1)
                print("-"*90)
                exit()
            elif confirm.upper()=="N":
                print("🔥 You chose to stay and fight!")
                time.sleep(1)
            else:
                print("Invalid choice! Please choose 'y' or 'n'.")
        else:
            print("Invalid option! Choose 1, 2, 3, or 4.")
    if health<=0:
        print()
        print("#"*90)
        time.sleep(1)
        print("💀 GAME OVER 💀".center(90))
        print("☠️ SUPERMAN HAS DEFEATED YOU! ☠️".center(90))
        time.sleep(1)
        print("#"*90)
        print()
        print("👹 SUPERMAN has defeated you and taken over the kingdom!")
        print("You have failed to save the kingdom!")
        print("Better luck next time!")
        time.sleep(1)
        break 
    elif boss_health<=0:
        print()
        print("👹 SUPERMAN's HP:0".center(90))
        print("#"*90)
        time.sleep(1)
        print("🏆⚔️ YOU WIN! ⚔️🏆".center(90))
        time.sleep(1)
        print("#"*90)
        print()
        print("🎉 SUPERMAN HAS BEEN DEFEATED! 🎉".center(90))
        print("Congratulations!")
        print("👑 YOU ARE A TRUE HERO! 👑".center(90))
        time.sleep(2)
        print("Thank you for playing the game!")
        time.sleep(1)
        break       
