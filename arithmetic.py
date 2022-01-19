

def operation(num1,num2):
    print("sum = ",int(num1)+int(num2));
    print("min = ",int(num1)-int(num2));
    print("mul = ",int(num1)*int(num2));
    print("div = ",int(num1)/int(num2));

def uinput():
    global num1,num2;
    num1=input("first num : ");
    num2=input("first num : ");

if __name__=="__main__":
    uinput();
    operation(num1,num2);


