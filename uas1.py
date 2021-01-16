class aktor(User):

    def register(self):
        notelp = input("No Telepon : ")
        register = f'INSERT INTO Admin (notelp, status) VALUES ("{notelp}", "Admin")'
        self.execute(register)
        self.commit();
        print("Akun Berhasil Ditambahkan")
        
