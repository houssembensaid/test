from hashlib import md5
from getpass import getpass
def menu():
    while True:
        try:
            print("selectionner un choix svp :\n"
                  "1==> register :\n"
                  "2==> login :\n"
                  "3==> quiter :\n"
                  )
            code=int(input("please chose one :\n"))
            if code==1:
                register()
                break
            elif code==2:
                login()
                break
            elif code==3:
                print("quuiter")
            else:
                print("merci d'introduire un choix valide")
        except ValueError:
            print("merci d'introduire un entier")
        menu()
def register():
    l=[]
    user={}
    id=int(input("donner votre id: \n"))
    nom=input("donner votre nom :\n")
    prenom=input("donner votre prenom:\n")
    tel=input("donner votre num:\n")
    pwd=getpass("donner votre mot de passe:\n")
    l.append([nom,prenom,tel,md5(pwd.encode()).hexdigest()])
    user[id]=l
    for i,j in user.items():
        print(f"user{i}has the password:\n\t"
              f"nom:{j[0][0]}\n\t prenom :{j[0][1]}\n\t tel:{j[0][2]}")
def login ():
    if (len(user)==0):
        print('the base is empty please register first \n')
        register()
    else :
        new_user=int(input("donner votre id pour s'authentifier: \n"))
        trouver=False
        count=3
        for i,j in user.items():
            if i==new_user:
                trouver=True
                while count>0:
                    new_pass=input(f"please give your password({count}tries):\n")
                    if j[0][3]==md5(new_pass.encode()).hexdigest():
                        print(f"welcom{j[0][0]}")
                        break
                    else:
                        count -=1
                    if count==0:
                        print("your account  blocked")
                    if (trouver==False):
                        print(f"{new_user}is not registred")
                        menu()











