class emp():
    def __init__(self,name,num):
        self.name=name;
        self.num=num;

    def show(self):
        print("name : ",self.name, "num : ",self.num);

class detail(emp):
    def __init__(self,name,num,pos,sal):
        emp.__init__(self,name,num);
        self.sal=sal;
        self.pos=pos;

    def show(self):
        emp.show(self);
        print("pos : ",self.pos, "sal : ",self.sal);
        
emp1=detail("apple",1,"intern",20000);
emp2=detail("mango",3,"emp",50000);

if __name__=="__main__":
    emp1.show();
    emp2.show();



