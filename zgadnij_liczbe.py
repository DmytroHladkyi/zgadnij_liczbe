from random import randint

trials = 0
number1 = randint(0, 10)

while True:
    user = int(input("Podaj liczbę: "))
    trials += 1
    if user == number1:
        print("Bravo to była", number1, ". Potrzebowałes", trials, "próby.")
        break
    elif user < number1:
        print("Podaj więszką liczbę.")
        
    elif user > number1:
        print("Podaj mniejszą liczbę.")