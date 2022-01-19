def operation(num1,num2,num3):

    if num1>num2 and num1>num3 :
       print("num1 is grt");
    elif num2>num3:
        print("num2 is grt");
    else:
        print("num3 is grt");

num1, num2, num3 = input("Enter 3 values: ").split();

# num1=input("1 num : ");
# num2=input("2 num : ");
# num3=input("3 num : ");

if __name__=="__main__":
    operation(num1,num2,num3);
