import random
lis1 = []
lis2 = []
class cricket:
    def __init__(self):
        self.Sum1 = 0
        self.Sum2 = 0
        self.count = 0
        self.toss = random.randint(0, 1)
        self.wickets1 = 0
        self.wickets2 = 0
        self.totA = 0
        self.totB = 0
        self.no_of_overs = int(input("enter no of overs"))

    def display(self):
        print("no_of_overs:", self.no_of_overs)
        print("Toss is", self.toss)
        if self.toss == 0:
            print("team1 won the toss")
            choose = input("Choose bat or field: ")
            if choose == 'field':
                self.team2()
                print("the innings are over and the another  team is batting start")
                self.team1()
            elif choose == 'bat':
                self.team1()
                print("the innings are over and the another  team is batting start")
                self.team2()

        elif self.toss == 1:
            print("team2 won the toss")
            choose = input("choose bat or field:")
            if choose == 'field':
                self.team1()
                print("the innings are over and the anotehr team is batting start")
                self.team2()
            elif choose == 'bat':
                self.team2()
                print("the innings are over and the another  team is batting start")
                self.team1()

    # def toss_coin(self):
    #     pass

    def team1(self):
        for i in range(1, self.no_of_overs + 1):
            for j in range(6):
                runs1 = random.randint(0, 7)
                if (runs1 == 7):
                    self.wickets1 = self.wickets1 + 1
                    continue

                lis1.append(runs1)
                self.totA += runs1
                print(runs1)
            print(lis1)
            self.Sum1 = sum(lis1)
            self.Cal()
            if self.wickets1 == 10:
                break
            print("wickets:", self.wickets1)
            print(f"------{i}over completed")
        print("Team1 score is:", self.Sum1, "-", self.wickets1)

        print("team1 batting complete---------")

    def team2(self):
        for i in range(1, self.no_of_overs + 1):

            for j in range(6):
                runs2 = random.randint(0, 7)
                if (runs2 == 7):
                    self.wickets2 = self.wickets2 + 1
                    continue
                lis2.append(runs2)
                self.totB += runs2
                if self.wickets2 == 10:
                    break
                print(runs2)
            print(lis2)
            self.Sum2 = sum(lis2)
            # print("sumee---",self.Sum2)

            if self.wickets2 == 10:
                self.Cal()
                break
            print(f"-------{i}over completed")
            self.Cal()

            print("wickets:", self.wickets2)

        print("Team2 Score is: ", self.Sum2, "-", self.wickets2)

    def Cal(self):
        if (self.totB > self.totA):
            #             print(f"the team 1 won the match  by {10 - self.wickets1} ")
            return f"the team 1 won the match  by {10 - self.wickets1} "
        elif (self.totA > self.totB):
            return f"the team 2 won the match  by {10 - self.wickets2} "


obj = cricket()
obj.display()
#obj.toss_coin()
# obj.Cal()
if obj.Sum1 > obj.Sum2:
    print("team1 win the match--------by", obj.Sum1 - obj.Sum2, "runs")
elif obj.Sum1 < obj.Sum2:
    print("team2 win the match--------by", obj.Sum2 - obj.Sum1, "runs")
else:
    print("Draw the match -----------")