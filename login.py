import stdiomask,os,time,sys,genepass,random
from hash import hashing
from send_email import send_mail

def passwurd():
    os.system("cls")
    res=input("\n\n\n\t\tSuggest strong password ? (y/n) : ")
    if "y" in res:
        password1=genepass.stpass()
        print("\n\n\t\t"+'\033[1m \033[32m \033[4m' +  "Congratulation, You are added in our community\n" + '\033[0m')
        return password1

    else:
        print("\n\n\n\t\tChoose your password : ",end='')
        password1=stdiomask.getpass(mask='*')
        print("\n\n\t\tConfirm your password : ",end='')
        password2=stdiomask.getpass(mask='*')
        if password1==password2:
            return password1
        else:
            print("\n\n\t\t"+'\033[1m \033[31m \033[4m' + "Oops, Password didn't match\n\n"+'\033[0m')
            time.sleep(1.5)
            return passwurd()

def verify(user,email):
    os.system("cls")
    print("\n\n\n\t\t"+'\033[1m \033[34m \033[4m' +  "EMAIL VERIFICATION\n" + '\033[0m')
    otp=random.choice(range(100000,1000000))
    message="Your six digit one time password (OTP) for email verification is "+str(otp)
    sub="VERIFY YOUR EMAIL ADDRESS"
    print("\n\n\t\tPLEASE WAIT FOR A MOMENT... ☻ ")
    if send_mail(email,message,sub):
        os.system("cls")
        print("\n\n\n\t\t"+'\033[1m \033[34m \033[4m' +  "EMAIL VERIFICATION\n" + '\033[0m')
        print("\n\n\t\tAn OTP is sent to your email address")
        print("\n\t\tCheck your inbox or spam folder")
        verification_code=int(input("\n\t\tEnter the verification code you received : "))
        if verification_code==int(otp):
            print("\n\n\t\t"+'\033[1m \033[32m \033[4m' +  "EMAIL ADDRESS VERIFIED\n\n" + '\033[0m')
            os.system("pause")
            return True
        else:
            print("\n\n\t\t"+'\033[1m \033[31m \033[4m' +  "SORRY, VERIFICATION CODE DOESN'T MATCH\n\n" + '\033[0m')
            verification_code=int(input("\n\t\tEnter the verification code you received : "))
            if verification_code==int(otp):
                print("\n\n\t\t"+'\033[1m \033[32m \033[4m' +  "EMAIL ADDRESS VERIFIED\n\n" + '\033[0m')
                os.system("pause")
                return True
            else:
                print("\n\n\t\t"+'\033[1m \033[31m \033[4m' +  "SORRY, VERIFICATION CODE DOESN'T MATCH\n\n" + '\033[0m')
                os.system("pause")
                return False
    else:
        print("\n\n\t\t"+'\033[1m \033[31m \033[4m' +  "SORRY, VERIFICATION FAILED\n\n" + '\033[0m')
        os.system("pause")
        return False

def create():
    os.system("cls")
    with open("logindata.txt",'r+') as f:
        str=f.read()
    words=str.split('\n')
    woods=[words[i].split() for i in range(len(words))]
    usernames=[woods[x][0] for x in range(len(woods))]
    emails=[woods[x][1] for x in range(len(woods))]
    print("\n\n\n\t\t"+'\033[1m \033[34m \033[4m' +  "WELCOME TO OUR COMMUNITY\n" + '\033[0m')
    username=input("\n\n\n\t\tChoose your USERNAME ID : ")
    email=input("\n\t\tEnter your email ID : ")
    if username in usernames or email in emails:
        print("\n\n\t\t"+'\033[1m \033[31m \033[4m' +  "SORRY, USERNAME or EMAIL ID ALREADY EXIST\n" + '\033[0m')
        time.sleep(2)
        create()
    else:
        if not verify(username,email):
            create()

        else:
            os.system("cls")
            password=passwurd()
            print("\n\n\t\t"+'\033[1m \033[32m \033[4m' + "Congratulation, You are added in our community\n" + '\033[0m')
            password=hashing(password)
            data="\n"+username+' '+email+' '+password
            with open("logindata.txt","a") as file:
                file.write(data)

            res=int(input("\n\n\t\t1) Login\n\t\t2) Exit\n\n\t\tEnter your response : "))
            if res==1:
                login()
            else:
                sys.exit()

def login():
    os.system("cls")
    with open("logindata.txt",'r+') as f:
        strung=f.read()
    words=strung.split('\n')
    woods=[words[i].split() for i in range(len(words))]
    usernames=[woods[x][0] for x in range(len(woods))]
    passwords=[woods[x][2] for x in range(len(woods))]
    emails=[woods[x][1] for x in range(len(woods))]

    print("\n\n\n\t\t"+'\033[1m \033[34m \033[4m' +  "WELCOME BACK\n" + '\033[0m')
    username=input("\n\n\n\t\tEnter Your USERNAME ID : ")
    if username in usernames:
        i=usernames.index(username)
        print("\n\t\tPASSWORD : ",end='')
        password=stdiomask.getpass(mask='*')
        hashed=hashing(password)

        if hashed==passwords[i]:
            print("\n\n\n\t\t"+'\033[1m \033[32m \033[4m' +  "CORRECT PASSWORD\n\n\n\n\n" + '\033[0m')
            sys.exit()
        else:
            print("\n\n\n\t\t" + '\033[1m \033[31m \033[4m' + "INCORRECT PASSWORD\n\n" + '\033[0m')
            time.sleep(2)
            ras=input("\n\t\tForgot password (y/n) ? : ").upper()
            if "Y" in ras:
                email=input("\n\t\tEnter your email ID : ")
                if emails[i]!=email:
                    print("\n\n\t\t"+'\033[1m \033[31m \033[4m' +  "SORRY, EMAIL ID DOESN'T MATCH\n" + '\033[0m')
                    time.sleep(2)
                    login()

                if not verify(username,email):
                    login()
                else:
                    password=passwurd()
                    password=hashing(password)
                    passwords[i]=password
                    data='rough'+' '+ "rough@gmail.com" + ' ' + "8764657854679765467979664471"
                    with open("logindata.txt","w") as file:
                        file.write(data)
                    for x in range(1,len(passwords)):
                        data="\n"+usernames[x]+' '+emails[x]+' '+passwords[x]
                        with open("logindata.txt","a") as file:
                            file.write(data)

                    print("\n\n\n\t\t"+'\033[1m \033[32m \033[4m' +  "DONE !!\n\n\n" + '\033[0m')
                    os.system("pause")
                    login()

            else:
                login()
    else:
        print("\n\n\n\t\t"+'\033[1m \033[31m \033[4m' +  "SORRY, USERNAME DOESN'T EXIST" + '\033[0m')
        ras=input("\n\n\t\tDo you want to create account ? (y/n) :  ")
        ras=ras.upper()
        if "Y" in ras:
            create()

def main():
    os.system("cls")
    print("\n\n\n\t\t"+'\033[1m \033[34m \033[4m' + "WELCOME USER" + '\033[0m')
    print("\n\n\t\tHello Dear, welcome back\n\n")
    print("\t\t1) Login\n\n\t\t2) Create account\n\n\t\t3) Exit")
    res=int(input("\n\n\t\tEnter your response : "))
    if res==1:
        login()
    elif res==2:
        create()
    else:
        sys.exit()

if __name__=="__main__":
    main()
