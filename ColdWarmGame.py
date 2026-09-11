import random
start = int(input("Enter the number on start "))
finish = int(input("Enter the number on finish "))
rnd = random.randint(start,finish)
chosen = int(input(f"a random number between {start} and {finish} is chosen. Can you guess it?))"))
while chosen != rnd:
    if chosen - rnd < 5:
        print("Very hot!")
    elif chosen - rnd < 10:
        print("Hot!")
    elif chosen - rnd < 20:
        print("Warm")
    elif chosen - rnd < 30:
        print("Cold")
    elif chosen - rnd < 50:
        print("So cold")  
    elif chosen - rnd < 70:
        print("Very cold!") 
    chosen = int(input("Your answer:"))
