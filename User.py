class User:
    def __init__(self, name, email, drivers_license, age):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license
        self.age = age
        print("Intizializing")
    def __str__(self):
        print(f"My name is {self.name} and I am {self.age} years old")
    
    # 
dalton = User("Dalton", "egglestondalton@yahoo.com", "WDLA12324AD", 22)
michael = User("Michael", "feaW@gmail.com", "SF223AWDAD3", 22)
christopher = User("Christopher", 'giadawd@gmail.com', "WDA2323ADFA", 44)
print(dalton)




    