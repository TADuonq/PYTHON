database = {'home': 'ngoi nha',
            'baby': 'em be'}
def show_menu():
    print("--------------------")
    print("CHUONG TRINH TU DIEN")
    print("--------------------")
    print("1. Them tu")
    print("2. Tim tu")
    print("3. Xoa tu")
    print("4. Xem tat ca") 
    print("An 0 de thoat chuong trinh")
    
def add():
    word = input("Tu moi:")
    mean = input("Nghia la: ")
    database[word] = mean
    print("+ Tu moi da duoc them")
    
def find():
    word = input("Tu gi: ")
    if word in database:
        print("Tim thay: [%s: %s]") % (word, database[word])
    else: 
        print("Khong tim thay tu: [%s]" % word)
def delete():
    word = input("Tu gi: ")
    if word in database:
        delete(database[word])
        print("Tu da bi xoa: [%s]" % word)
    
def view_all():
    for word, mean in database.items():
        print("[%s:%s]" % (word, mean))
    
show_menu()
choice = int(input("Ban muon lam gi: "))
while choice != 0:
    if choice == 0:
        break
    elif choice == 1:
        add()
    elif choice == 2:
        find()
    elif choice == 3:
        delete()
    elif choice == 4:
        view_all()
    else:
        print("Khong co lua chon nay.")
        
    choice = int(input("Ban muon lam gi: "))
print("Hen gap lai!!!")