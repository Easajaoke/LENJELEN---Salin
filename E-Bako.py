#Sistem Penjualan Sembako UD Sinar Jaya (E-Bako)

def get_login():
    print('=' * 20)
    print('halaman login E-Bako')
    username = input('masukan username anda: ')
    password = input('masukan password: ')
 
    if username == 'admin' and password == 'adminpass':
        print('login berhasil...\n\n')
        main_menu()
    else:
        print('login gagal coba lagi..')
        get_login()
