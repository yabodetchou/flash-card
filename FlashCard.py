import time


class FlashCard:


    def topics(self):
        # create the cards
        # key question value answer
        cards = {
            "History": {
                "Who was the first african american woman that refused to give up her seat on a Montgomery Alabama bus?": "Rosa Parks",
                "What was the name of the ship that sank in April 1912?": "Titanic",
                "Who was the disciple of Jesus who wrote the book of Revelations?": "John"
            },
            "Math": {
                "What is (4+3)*37": "259",
                "What is 5% of 200?": "10",
                "What is the square root of 8 to the nearest tenths?": "2.8"
            },
            "Art": {
                "What type of paint is the Mona Lisa?": "Oil",
                "What media was the Last Supper?": "Tempera",
                "Is Starry Night Acrylic or Oil": "Oil"

            },
            "Chemistry": {
                "What is the chemical formula for Salt?": "NaCl",
                "How many hydrogen atoms does table sugar (C12H22O11)?": "22",
                "How many ionic bonds are in water?": "0"
            }
        }
        return cards

    def revision(self):
        for (k,v) in self.topics().items():
            studying = input(f"Type {k} to start studying {k}: ")
            if studying == k:
                for questions, answers in v.items():
                    print(f"question: {questions} \nanswer: {answers.lower()}")
        self.practice()


    def practice(self):
        test = "yes"
        player = input("Would you like to test your knowledge?: yes or no ")
        if player != "yes":
            self.revision()
        else:
            print("Revision starts in 10 seconds")
            time.sleep(10)
            self.prompt()

    def prompt(self):
        count = 0
        for (k,v) in self.topics().items():
            for questions, answers in v.items():
                answers = answers.lower()
                while True:
                    player = (input(f"{questions}: "))
                    if player == answers:
                        count +=1
                        print(f"score: {count}")
                        break
                    else:
                        print("restarting...")
                        time.sleep(4)
                        self.prompt()



obj = FlashCard()
obj.practice()






















