import time
#functon to display option and take user's input
def Select_options():
    print("Enter 1 to Inject Innow Plain text key")
    print("type exit to for exit")

    opt = input(">> ")
    if opt == '1':
        print("Loading key injection Process")
        print(".........................")
        time.sleep(1)
        inject_key()
    elif opt == 'exit':
        print("Exiting the program")
        print(".........")
        print("Success")
        exit()
    else:
        print("Inavlid Entry")
        exit()

#Function to inject key
def inject_key():
    print("enter 1 to inject keys")
    key_type = input('->>')
    if key_type == '1':
        key_val = input('KSN:')
        if key_val == '123456':
            key_val2 = input('DUKPT:')
            if key_val2 == '0123456':
                print("wait a second....\n")
                time.sleep(1)
                print("injecting keysss.......")
                time.sleep(1)
                print("Keys inject process completed Succesfully")
                exit()
            else:
                print("Inavlid Key")
                exit()
        else:
            print("Invalid Key")
            exit()
    else:
        print("Invalid Selection")
        exit()
