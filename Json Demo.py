import json

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.current:User = {}
        self.loadUser()
    
    def loadUser(self):
        pass

    def register(self, user: User):
        self.users.append(user)
        print('Kullanıcı Oluşturuldu.')
    def login(self):
        pass
    def savetoFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))
            
        with open('users.json','w') as file:
            json.dumps(list, file)

reposiory = UserRepository()


while True:
    print('Menü'.center(50,'*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- identity\n5 -Exit\nseçiminiz: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username=username, password=password, email=email)
            reposiory.register(user)

            #print(reposiory.users)
        elif secim == '2':
            pass
        elif secim == '3':
            pass
        elif secim == '4':
            pass
        else:
            print('Yanlış Seçim')

    

