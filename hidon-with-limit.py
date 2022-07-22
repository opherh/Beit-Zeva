hidon = {
    "q1":{
        "title": "1.What is my name?",
        "ans1":"Matan",
        "ans2":"Opher",
        "ans3":"Doron",
        "correct":"Opher"
    },
    "q2":{
        "title": "2.What is my age?",
        "ans1":"21",
        "ans2":"22",
        "ans3":"28",
            "correct":"28"
    },
    "q3":{
        "title": "3.Where do I live?",
        "ans1":"Tel Aviv",
        "ans2":"Herzeliya",
        "ans3":"Netanya",
        "correct":"Tel Aviv"
    }
}

counter = 0
cont = True
while (cont and counter <10):
    print("Welcome to our quiz! Please choose a question:\nBe advised! you may only 10 mistakes before getting kicked out!")
    for i in range(3):
        print(hidon["q" + str(i+1)]["title"]) #שימו לב - אני לכל המשתנים יש שמות זהים ואני משחק עם לולאה שמריצה את ה-COUNTER
    user_choice = input("Please enter a number:\n")

    print("Great! Here are your possible answers\n",hidon["q"+user_choice]["title"])

    is_correct = False
    while (is_correct == False and counter < 10):
        for p in range(3):
            print(hidon["q"+user_choice]["ans"+str(p+1)])
        user_ans = input("Please type in the answer:\n")
        if (user_ans == hidon["q"+user_choice]["correct"]):
            print("Success! Good job!")
            is_correct = True
        else:
            print("Aww... Please try again!")
            counter +=1
            print("You have ", 10-counter, " mistakes left!")

    if (counter >= 10):
        print("Ah... seems like you answered wrong 10 times! Try again..")
        cont = False
    else:
        want_cont = input("Do you want to continue with the quiz? Type in YES, otherwise - type NO")
        if (want_cont == 'NO'):
            cont = False

print("See you later!")

