from hashlib import new
import json
import os
from psutil import users

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
        self.loadUsers()
    
    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r', encoding='utf=8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
                    #print(user['username'])
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print('Kullanıcı Oluşturuldu.')
   
    def login(self, username, password):
            for user in self.users:
                if user.username == username and user.password == password:
                    self.isLoggedIn = True
                    self.current = user
                    print('Giriş Yapıldı.')
                    break
    def logout(self):
        self.isLoggedIn = False
        self.current = {}
        print('Çıkış Yapıldı.')

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.current.username}')
        else:
            print('giriş yapılmadı.')
            
    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))      
        with open('users.json','w') as file:
            json.dump(list, file)

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
            if reposiory.isLoggedIn:
                print('Zaten giriş yapılmış')
            else:
                username = input('username: ')
                password = input('password: ')
                reposiory.login(username, password)
        elif secim == '3':
            reposiory.logout()
        elif secim == '4':
            reposiory.identity()
        else:
            print('Yanlış Seçim')

    

