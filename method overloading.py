#  It is worked in same method names and different arguments

class Area:
    def find(self,length=None,breadth=None):
        if length!=None and breadth!=None:
            print(f"Area of Rectangle is {breadth*length}")
        elif length!=None:
            print(f"Area Of Square is {length*length}")
        else:
            print("Nothing TO find")
        
        
ob=Area()
ob.find(10,20)