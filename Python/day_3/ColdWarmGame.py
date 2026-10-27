import random
start = int(input("Enter the number on start "))
finish = int(input("Enter the number on finish "))
rnd = random.randint(start,finish)
chosen = int(input(f"a random number between {start} and {finish} is chosen. Can you guess it?))"))
while chosen != rnd:
    if abs(chosen - rnd) < 5:
        print("Very hot!")
    elif abs(chosen - rnd)  < 10:
        print("Hot!")
    elif abs(chosen - rnd) < 20:
        print("Warm")
    elif abs(chosen - rnd) < 30:
        print("Cold")
    elif abs(chosen - rnd) < 50:
        print("So cold")  
    elif abs(chosen - rnd)  < 70:
        print("Very cold!")
    else:
        print("Forest!!!")
    chosen = int(input("Your answer:"))
print(f"Yes {rnd}. You right!")