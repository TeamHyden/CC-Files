from colorama import Fore

import os

while(1==1):

    text = f"""
    {Fore.GREEN}
    ____________xxxxxxxxxxxx TEAM HYDEN xxxxxxxxxx_________________________
    {Fore.RESET}

    {Fore.RED}_____________MASS GENERATOR_____________{Fore.RESET}

    (1) Mass checker 

    {Fore.RED}_____________SOLO CHECKER_____________{Fore.RESET}


    (2) BIN CHECKER
    (3) CC CHECKER
    (4) GATES CHECKER
    (0) to Exit
    """


    nowloc = os.getcwd()

    print(text)

    import os 
    print('_________________________________________________\n')

    import subprocess
    u = int(input("Enter your response: "))

    print('_________________________________________________\n')


    if u == 1:
        os.chdir('darkweb/web/main/project')
        subprocess.call('python app.py')
        os.chdir(nowloc)


    elif u ==2:
        os.chdir('darkweb/ccs/binchecker')
        subprocess.call('python main.py')
        os.chdir(nowloc)


    elif u==3:
        os.chdir('darkweb/ccs/cc-checker')
        subprocess.call('python cc-checker.py')
        os.chdir(nowloc)


    elif u==4:
        os.chdir('GATES')
        print(Fore.BLUE+'(1)STRIPE GATEWAY'+Fore.RESET)
        print(Fore.BLUE+'(2)BRAINTREE GATEWAY'+Fore.RESET)
        gateno = int(input("Enter gate no. "))
        if gateno == 1:
            os.chdir('stripe')
            subprocess.call('python stripe.py')
            os.chdir(nowloc)


        elif gateno ==2:
            os.chdir('braintree')
            subprocess.call('python braintree.py')
            os.chdir(nowloc)


        else:
            print(Fore.RED+"WRONG GATE NUMBER"+Fore.RESET)
            os.chdir(nowloc)



    elif u ==0:
        os.chdir(nowloc)


    else:
        print('wrong input')

