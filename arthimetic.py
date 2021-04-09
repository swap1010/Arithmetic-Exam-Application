import random

levels = ["simple operations with numbers 2-9", "integral squares of 11-29"]
choices = ["yes", "YES", "y", "Yes"]
print("Which level do you want? Enter a number:")
print(f"1 - {levels[0]}")
print(f"2 - {levels[1]}")
choice = int(input())
correct = 0
while choice != 1 or choice != 2:
    if choice == 1:
        for _ in range(5):
            operations = [" + ", " - ", " * "]
            question = str(random.randint(2, 9)) + random.choice(operations) + str(random.randint(2, 9))
            print(question)
            while True:
                try:
                    user_ans = int(input())
                    break
                except ValueError:
                    print("Incorrect format.")
            if user_ans == eval(question):
                print("Right!")
                correct += 1
            else:
                print("Wrong!")
        break
    elif choice == 2:
        for _ in range(5):
            question = int(random.randint(11, 29))
            print(question)
            while True:
                try:
                    user_ans = int(input())
                    break
                except ValueError:
                    print("Incorrect format.")
            if user_ans == question ** 2:
                print("Right!")
                correct += 1
            else:
                print("Wrong!")
        break
    else:
        print("Incorrect format.")
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        choice = int(input())
print(f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no.")
choice2 = input().strip()
if choice2 in choices:
    name = input("What is your name?\n")
    s = f"{name}: {correct}/5 in level {choice} ({levels[choice - 1]})."
    with open("results.txt", "a") as f:
        f.write(s)
    print('The results are saved in "results.txt".')
