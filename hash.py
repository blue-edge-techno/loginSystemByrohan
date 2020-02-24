def hashing(string):
    great=list(string)
    for x in range(len(great)):
        a=ord(great[x])**4
        a=str(a)
        great[x]=a

    c=''.join(great)
    c=int(c)
    c=c%10000000000000000000000000007
    return str(c)

def main():
    inp=input("\n\n\tEnter the string you want to hash : ")
    print("\n\n\tYour required hash is ",hashing(inp),"\n\n")

if __name__=="__main__":
    main()
