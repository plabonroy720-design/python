
print("======== Number Gaussing Game ========")
import random
try:
    computer = random.randint(1, 100)
    g=0
    a=5

    print(computer)
    while a>0:
        
        m=int(input("Gause a number  (1-100) : "))

        
        if m<computer:
            print("Too low!")
            g+=1
            a-=1
            print(f'Guses are left: {a}')
            if a == 0:
                print("Try Again Next Time!")
                print(f"The correct number was: {computer}")
                break
    
        elif m>computer:
            print("Too high !")
            g+=1
            a-=1
            print(f'Guses are left: {a}')

            if a == 0:
                print("Try Again Next Time!")
                print(f"The correct number was: {computer}")
                break

        else:
            print("")
            print("Congratulation !")
            print("You gussed sucessfully")
            g+=1

            print(f'Guses are left: {a}')
            
            if g<=5:
                print("Excelent! You are a Pro Player....")
            else:
                print("Good Jod Keet Practacing....")
            break
        

except ValueError:
    print("Enter number only ....")
    print("")
    print(f'Number of guses {g}')
    print("")

finally:
    print("======= The Game is Over =======")
