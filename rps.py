import random

while True:
    user = input("Rock Paper or Scissors ?")
    tools = ["Rock", "Paper", "Scissors"]
    bot = tools[random.randrange(len(tools))]
    print("Bot Picks ", bot)
    if user == bot:
        print("Draw")
    elif user == "Rock":
        if bot == "Paper":
            print("Bot Wins")
        else:
            print("User Wins")
    elif user == "Paper":
        if bot == "Scissors":
            print("Bot Wins")
        else:
            print("User Wins")
    elif user == "Scissors":
        if bot == "Rock":
            print("Bot Wins")
        else:
            print("User Wins")
    else:
        print("Choose Between Rock Paper And Scissors")


        def game(user):
            # user = input("Rock Paper or Scissors ?")
            tools = ["Rock", "Paper", "Scissor"]
            bot = tools[random.randrange(len(tools))]
            self.botlabel.setText(bot)
            print("Bot Picks ", bot)
            if user == bot:
                self.result.setText("Draw")
            elif user == "Rock":
                if bot == "Paper":
                    self.result.setText("Bot Wins")
                else:
                    self.result.setText("User Wins")
            elif user == "Paper":
                if bot == "Scissors":
                    self.result.setText("Bot Wins")
                else:
                    self.result.setText("User Wins")
            elif user == "Scissor":
                if bot == "Rock":
                    self.result.setText("Bot Wins")
                else:
                    self.result.setText("User Wins")
            else:
                print("Choose Between Rock Paper And Scissors")


        self.rock.clicked.connect(partial(game, "Rock"))
        self.paper.clicked.connect(partial(game, "Paper"))
        self.scissor.clicked.connect(partial(game, "Scissor"))
