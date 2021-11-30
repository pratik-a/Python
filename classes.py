class myclass():
    def method(self):
        print("method 1")
        
    def method1(self, strng):
        print("method ", strng)
        
class secclass():
    def method(self):
        myclass.method(self)
        print("method 2")
        
    def method1(self, strng):
        print("method 2", strng)
        
def main():
    c = myclass()
    c.method()
    c.method1("hello")
    
    c1 = secclass()
    c1.method()
    c1.method1("hello")
    

if __name__=="__main__":
    main()
