class  car :
       
    def __init__(self,m,b) :
        print("i am here")
        self.bhp=b;
        self.made=m;
    def display(self) :
        print("CAR details")
        print("bhp:",self.bhp)
        print("made:",self.made)
    def update_bhp(self,new_bhp) :
        self.bhp=new_bhp;

def display2() :
    print("CAR details")
    print("bhp:",bhp)
    print("made:",made)

swift=car(1248,"maruti")

swift.display();

swift.update_bhp(1399)

swift.display();



