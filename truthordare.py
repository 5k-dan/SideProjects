import random
while True:
    Truths = ["When was the last time you lied?" ,
              "What's the worst thing you've ever done at work?",
              "What's the worst thing anyone's ever done to you?",
              "What's the best thing anyone's ever done for you?",
              "What's your worst habit?",
              "What's the most you've spent on a night out?",
              "What's the best rumour you've heard about yourself?"]
    Dares = ["Ask a Lizzo on a date",
             "No phone for an hour",
             "GET A JOB"]

    Prompt = (input("Truth or Dare?"))

    if Prompt == "Truth":
        print(random.choice(Truths))

    elif Prompt == "Dare":
        print(random.choice(Dares))


    else:
        print("Not in correct format!")
        continue