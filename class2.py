# passing attribute 

class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("i am Making a Call")
    def play_game(self):
        print("I am playing a Game")
    
ob=Phone()

ob.set_color("yelloW")
ob.set_cost(9999)

print(ob.show_color())
print(ob.show_cost())