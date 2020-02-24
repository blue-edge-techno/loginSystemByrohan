import random,os,time

def stpass():
    os.system("cls")
    print("\n\n\n\t\t"+'\033[1m \033[34m \033[4m' +  "GENERATE STRONG PASSWORD\n" + '\033[0m')
    n=int(input("\n\n\t\tLength of the password : "))
    if n<4:
        print("\n\n\t\tSorry we don't process password of length less than 4\n")
        os.system("pause")
        return stpass()

    m=input("\n\n\t\tInclude symbols ? (y/n) : ")
    m=1 if "y" in m else 0

    nums=["0","1","2","3","4","5","6","7","8","9"]
    alph=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
    "R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i",
    "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    sym=["!","@","#","$","%","^","&","(",")","<",">","?","/","[","]","{","}","|","~"]

    strpass=[]
    if m is 1:
        for _ in range(int(n/5)):
            strpass.append(random.choice(sym))
        for _ in range(int(2*n/5)):
            strpass.append(random.choice(nums))
        for _ in range(n-int(n/5)-int(2*n/5)):
            strpass.append(random.choice(alph))

    else:
        for _ in range(int(2*n/5)):
            strpass.append(random.choice(nums))
        for _ in range(n-int(2*n/5)):
            strpass.append(random.choice(alph))

    random.shuffle(strpass)
    stp="".join(strpass)

    print("\n\n\t\tYour strong password : "+'\033[1m \033[32m \033[4m' + stp + '\033[0m')
    res=input("\n\n\t\tDon't liked it generate other ? (y/n) : ")
    if "y" in res:
        return stpass()
    else:
        return stp

def main():
    p=stpass()

if __name__=="__main__":
    main()
