class Jui:
    def __init__(self):
        self.total_cost = 0

    def Menu(self):
        while(True):
            print("1.Mango:20 \n 2.lemon:30\n3.orange:40")
            n=int(input("enter the menu"))
            match n:
                case 1:
                    print("you entered mango")
                    self.mango()
                case 2:
                    print("you entered lemon")
                    self.lemon()
                case 3:
                    print("you entered orange")
                    self.orange()
                case 4:
                    print(f'the total cost is {self.total_cost}')
                    exit()


    def mango(self):
        m = int(input("enter quantity of mango"))
        print("your order quantity for mango is:", m)
        self.total_cost += 20 * m

    def lemon(self):
        k = int(input("enter qusantity of lemon"))
        print("your order quantity for lemon is:", k)
        self.total_cost += 30 * k

    def orange(self):
        x = int(input("enter quantity of orange"))
        print("your order quantity for orange is:",x)
        self.total_cost += 40 * x




c=Jui()
c.Menu()


