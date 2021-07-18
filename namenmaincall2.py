def call():
    print("function called")

def messg():
    print("function messg", __name__)

def main():
    call()
    messg()
    print("from calling")


if __name__ == '__main__':
    main()
