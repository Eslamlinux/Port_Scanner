
class vehicle:
    def __init__(self, company,color,model):
        self.company = company
        self.color = color
        self.model = model

    def Print_All_Data(self):
        print("company name:",self.company,"\nColor:",self.color, "\nModel:",self.model)
class car(vehicle):
    def Tech_Detels(self,Car_Speed,Engin):
        self.Car_Speed = Car_Speed
        self.Engin = Engin 
    def get_Tech_Detels(self):
        print("speed =",self.Car_Speed,"\nEngin:",self.Engin)
class truck(car):
    def Tech_Detels(self,Tyre_size):
        return Tyre_size


first = car("BMW","Blue",8812)
first.Tech_Detels("20m/m","unknown")

first_t = truck("NSR","green",231)
first_t.Tech_Detels("17-14")
# first_t.Tech_Detels("25m/m","Nsr Engin")



first.Print_All_Data()
first.get_Tech_Detels()
print(dir(first))
print("---------------------")
first_t.Print_All_Data()
# first_t.get_Tech_Detels()

class after:
    def start():
        pass

