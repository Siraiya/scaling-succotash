print("Welcome to Siraiya's Multiplication quiz")
print("\n")
print("Today we will go over our multiples of 2")
print("\n")
print("RULES:")
print("\n")
rules = "~You can enter your answer as the letter or the number\n~You cannot enter anything else other than what is presented\n~If you get it wrong or enter the wrong thimg, you will have to start all over."
print(rules)
print("\n")
print("Question one:")
print("--------------------")
print("What is 2 * 2?")
print("a)4\nb)7\nc)5\nd)2")
answer = "a"
while True:
    try:
        player_answer = input(":")
    except ValueError:
        pass
    else:
        if player_answer == answer:
            break
    print("Please Try Again")

print("Well Done")
print("\n")
print("Question Two:")
print("--------------------")
print("What is 2 * 8?")
print("a)14\nb)16\nc)10\nd)7")
answer = "b"
while True:
    try:
        player_answer = input(":")
    except ValueError:
            pass
    else:
        if player_answer == answer:
                break
    print("Give it another shot")

print("Goodjob, Now keep going")
print("\n")
print("Question Three:")
print("--------------------")
print("What is 2 * 5?")
print("a)16\nb)14\nc)9\nd)10")
answer = "d"
while True:
    try:
        player_answer = input(":")
    except ValueError:
        pass
    else:
        if player_answer == answer:
            break
    print("Try again buddy")

print("goodjob, You're Outstanding")
print("\n")

print("Question Four:")
print("--------------------")
print("What is 2 * 12?")
print("a)22\nb)24\nc)14\nd)11")
answer = "b"
while True:
    try:
        player_answer = input(":")
    except ValueError:
        pass
    else:
        if player_answer == answer:
            break
    print("Take your time")

print("Wow, Are you sure You're not Einstein?")
print("\n")

print("Question Five:")
print("--------------------")
print("What is 2 * 4?")
print("a)4\nb)6\nc)8\nd)11")
answer = "c"
while True:
    try:
        player_answer = input(":")
    except ValueError:
        pass
    else:
        if player_answer == answer:
            break
    print("That is Incorrect")

print("Great Job")
print("\n")

print("Question Six:")
print("--------------------")
print("What is 2 * 6?")
print("a)12\nb)6\nc)17\nd)4")
answer = "a"
while True:
    try:
        player_answer = input(":")
    except ValueError:
        pass
    else:
        if player_answer == answer:
            break
    print("Try Again")

print("Such Talent You Have :)")

