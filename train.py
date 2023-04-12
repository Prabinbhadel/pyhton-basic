class train:
    
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=[i for i in range(1,seats)]
        

    def getstatus(self):
        print(f"the name of the train is{self.name}")
        print(f"the available seats in the train is{self.seats}")

    def fareinfo(self):
        print(f"the fare of the train is {self.fare}")
    
    def bookTicket(self):
        if len(self.seats):
            print(f"the available seats are{self.seats}")
            choice=int(input("enter the ticket number"))
            print(f"you have booked tiket no {choice}")
            self.seats.remove(choice)
        else:
            print("sorry!! the train has already reached the maximum capacity")
    
    def cancelTicket(self):
        a=int(input("enter the ticket you want to cancel"))
        self.seats.append(a)
        print(f"you have cancelled your ticket no{a}")

        

intercity=train("intercity : 001",3000,10)
intercity.getstatus()
intercity.fareinfo()
intercity.bookTicket()
intercity.getstatus()
intercity.cancelTicket()
intercity.getstatus()

