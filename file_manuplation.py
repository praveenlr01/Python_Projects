class donor:
    def details():
        name=input("Enter your  name: ")
        db.update({"name : ":name})
        age=int(input("Enter your age: "))
        if age<18:
            print("sorry,you are not eligble")
            main_pro()
        else:
            db.update({"age : ":age})
        ph=int(input("Enter your phone number: "))
        db.update({"ph no : ":ph})
        ho=input("Enter your native: ")
        db.update({"native : ":ho})
        bg=input("Enter your blood group: ")
        donor=open(f'{bg}.txt','a')
        donor.write("\n\tdonor details\t")
        for i in db:
            donor.write(f'\n{i} : {db[i]}')
        print("created successfully")
        donor.close()

class reciver:
    def search():
        opt=int(input("[1]Search \nEnter: "))
        if opt==1:
            blood=input("Enter the blood group : ")
            rec=open(f'{blood}.txt','r')
            view=rec.read()
            print(view)
        else:
            print("Invalid Entery.")
                
db={}
d=donor
r=reciver

def main_pro():
    while True:
        opt=int(input("[1]Donor [2]Reciver \nEnter: "))
        if opt==1:
            d.details()
        elif opt==2:
            r.search()
        else:
            print("Invalid Entery.")
main_pro()
