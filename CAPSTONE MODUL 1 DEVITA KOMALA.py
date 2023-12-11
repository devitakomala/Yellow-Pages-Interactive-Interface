#IMPORT
from tabulate import tabulate
import os

## Clear Screen View
def clear_terminal() :
    os.system('clear')

clear_terminal ()

#DATA 
industries = [
    {'Kode IND':1,'Nama Industri': 'Online Marketplace'},
    {'Kode IND':2,'Nama Industri': 'Food and Beverage'},
    {'Kode IND':3,'Nama Industri': 'Book Store and Stationery'},
    {'Kode IND':4,'Nama Industri': 'Electronic Appliances'}
]

businesses = [ 
    {"Kode IND": 1, "Nama Bisnis": "Tokopedia", "No. Telp": "021-1111", "Alamat": "Jalan Dr. Prof Satrio 11", "Kode Pos": "12950"},
    {"Kode IND": 1, "Nama Bisnis": "Shopee", "No. Telp": "021-2222", "Alamat": "Jalan Karet Sawah 26A", "Kode Pos": "12930"},
    {"Kode IND": 1, "Nama Bisnis": "Blibli", "No. Telp": "021-3333", "Alamat": "Jalan Budi Kemuliaan 1", "Kode Pos": "10110"},
    {"Kode IND": 1, "Nama Bisnis": "Zalora", "No. Telp": "021-4444", "Alamat": "Jalan Gatot Subroto 18", "Kode Pos": "12710"},
    {"Kode IND": 1, "Nama Bisnis": "Love Bonito", "No. Telp": "021-5555", "Alamat": "Jalan M.H. Thamrin 1", "Kode Pos": "10310"},

    {"Kode IND": 2, "Nama Bisnis": "Sari Bundo", "No. Telp": "021-6666", "Alamat": "Jalan Ir. H. Juanda 12", "Kode Pos": "10120"},
    {"Kode IND": 2, "Nama Bisnis": "Tomoro Coffee", "No. Telp": "021-7777", "Alamat": "Jalan Sudirman 51", "Kode Pos": "12940"},
    {"Kode IND": 2, "Nama Bisnis": "Sinar Medan", "No. Telp": "021-8888", "Alamat": "Jalan Pecenongan Utara 27", "Kode Pos": "10120"},
    {"Kode IND": 2, "Nama Bisnis": "Simetri Coffee", "No. Telp": "021-9999", "Alamat": "Jalan Wijaya 6", "Kode Pos": "12160"},
    {"Kode IND": 2, "Nama Bisnis": "Talaga Sampireun", "No. Telp": "021-1010", "Alamat": "Jalan Prajurit KKO Usman", "Kode Pos": "10410"},

    {"Kode IND": 3, "Nama Bisnis": "Gramedia", "No. Telp": "021-1111", "Alamat": "Jalan Matraman Raya 46", "Kode Pos": "13150"},
    {"Kode IND": 3, "Nama Bisnis": "Paper Clip", "No. Telp": "021-1212", "Alamat": "Jalan Boulevard Bar. Raya 12", "Kode Pos": "14240"},
    {"Kode IND": 3, "Nama Bisnis": "Gunung Agung", "No. Telp": "021-1313", "Alamat": "Jalan Kwitang 38", "Kode Pos": "10420"},
    {"Kode IND": 3, "Nama Bisnis": "Toko Buku Senen", "No. Telp": "021-1414", "Alamat": "Jalan Senen RW. 3", "Kode Pos": "10420"},
    {"Kode IND": 3, "Nama Bisnis": "Periplus", "No. Telp": "021-1515", "Alamat": "Jalan M.H. Thamrin 28", "Kode Pos": "10350"},

    {"Kode IND": 4, "Nama Bisnis": "Electronic City", "No. Telp": "021-1616", "Alamat": "SCBD Jalan Sudirman 52", "Kode Pos": "12190"},
    {"Kode IND": 4, "Nama Bisnis": "Ace Hardware", "No. Telp": "021-1717", "Alamat": "Jalan Arteri Pd. Indah", "Kode Pos": "12240"},
    {"Kode IND": 4, "Nama Bisnis": "Hartono Elektronik", "No. Telp": "021-1818", "Alamat": "Jalan Arteri Pd. Indah 2", "Kode Pos": "12240"},
    {"Kode IND": 4, "Nama Bisnis": "Maju Jaya", "No. Telp": "021-1919", "Alamat": "Jalan Sultan Hasanuddin 1", "Kode Pos": "12160"},
    {"Kode IND": 4, "Nama Bisnis": "Cahaya Abadi", "No. Telp": "021-2020", "Alamat": "Jalan Angkasa Pura 40", "Kode Pos": "10720"}
]

#FUNCTIONS

# MENU 1 DISPLAY ALL DATA
def display_data(data_list): #parameter function nya berupa data businesses
    print(tabulate(data_list, headers='keys', tablefmt="grid"))

#calling/display kode IND utk following choices 2-5 dan iterasi
def display_industry_code(): 
    print("Kode Industri Existing:")
    for industry in industries:
        print(f"{industry['Kode IND']}. {industry['Nama Industri']}")

#bool utk mencegah error kode IND
def validasi_industry_code(code): 
    try:
        x = int(code)
        for industry in industries:
            if industry ["Kode IND"] == x:
                return True
    except ValueError:
        return False


# MENU 2 CARI DATA
def cari_data():
    while True:
        print("Cari berdasarkan:")
        print("1. Nama Bisnis")
        print("2. Kode Industri")
        print("3. Display Semua Data")
        print("4. Kembali ke menu utama")
        choice = input("Masukkan pilihan anda (1-4): ")

        if choice == '1':
            search_term = input("Masukkan nama bisnis: ")

            hasil = []
            for business in businesses:
                business_name = business.get('Nama Bisnis', '').lower()
                if search_term.lower() in business_name: #buat nyari
                    hasil.append(business)

        elif choice == '2':
            valid_industry_code = False
            while not valid_industry_code:
                display_industry_code()
                nyari_kode_industri = input("Masukkan kode industri: ")
                try:
                    nyari_kode_industri = int(nyari_kode_industri)
                    if validasi_industry_code(str(nyari_kode_industri)): #validasi apakah kode ind ada
                        nyari_kode_industri = str(nyari_kode_industri) #di konversi jadi integer
                        valid_industry_code = True
                    else:
                        print("Kode industri tidak valid, masukkan kode industri existing")
                except ValueError:
                    print("Kode industri tidak valid, masukkan kode yang benar") 
            
            hasil = []
            for business in businesses:
                bisnis_kode_ind = str(business.get('Kode IND', '')).lower ()
                if nyari_kode_industri.lower() in bisnis_kode_ind:
                    hasil.append(business)

        elif choice == '3':
            hasil = businesses
        elif choice == '4':
            break
        else:
            print("Pilihan tidak ada, Pilih dari 1-4")
            continue

        if hasil:
            display_data(hasil)
        else:
            print('Data tidak ditemukan')

        more_search = input("Apa anda ingin mencari data lagi? (y/n): ").lower()
        if more_search != 'y':
            break


# MENU 3 TAMBAH DATA
def tambah_data():
    bisnis_baru = {}

    print("\n1. Tambah Bisnis dalam Industri yang Sudah Ada")
    print("2. Tambah Industri Baru dan Bisnisnya")
    print("3. Kembali ke menu utama")

    while True:
        try:
            choice = int(input("Pilih opsi (1-3): "))
            if choice == 1:
                display_industry_code()
                while True:
                    try:
                        kode_industri = int(input("Masukkan kode industri: "))
                        if validasi_industry_code(kode_industri): #masukkin kode ind sesuai
                            bisnis_baru['Kode IND'] = kode_industri
                            break
                        else: 
                            print("Kode industri tidak valid, masukkan kode industri yang valid")
                    except ValueError:
                        print("Input tidak valid, masukkan kode industri yang valid (angka)")
            elif choice == 2:
                nama_ind_baru = input("Masukkan nama industri baru: ")
                kode_ind_baru = max(industries, key=lambda x: x['Kode IND'])['Kode IND'] + 1 #otomatis assign kode industri yang baru
                industries.append({'Kode IND': kode_ind_baru, 'Nama Industri': nama_ind_baru}) #menambah industri baru pake append
                print(f"Kode untuk industri baru: {kode_ind_baru}.") #output
                bisnis_baru['Kode IND'] = kode_ind_baru #agar konsisten update ke kamus bisnis baru
            elif choice == 3:
                break
            else:
                print("Pilihan tidak valid")
                continue

            bisnis_baru['Nama Bisnis'] = input("Masukkan nama bisnis: ")

            while True:  
                bisnis_baru['No. Telp'] = input("Masukkan nomor telpon: ")
                if bisnis_baru['No. Telp'].isdigit(): #helper
                    break
                else:
                    print("Input tidak valid. Masukkan nomor telpon yang benar (numerik).")

            while True:
                bisnis_baru['Kode Pos'] = input("Masukkan kode pos: ")
                if bisnis_baru['Kode Pos'].isdigit(): #helper
                    break
                else:
                    print("Input tidak valid. Masukkan kode pos yang benar (numerik).")

            bisnis_baru['Alamat'] = input("Masukkan alamat: ")

            businesses.append(bisnis_baru)
            print("Data sukses ditambah!")

            tambah_bisnis_lagi = input ("Apakah anda ingin menambah bisnis lagi? (y/n): ").lower
            if tambah_bisnis_lagi != 'y': 
                break
        except ValueError:
            print("Input tidak valid")


#MENU 4 UPDATE DATA
def update_data () :
    print("\nMenu Update Data")

    display_industry_code()

    while True:
        try:
            industry_code = int(input("Masukkan kode industri: ")) #pilih kode industri
            industri_ketemu = False
            for industry in industries:
                if industry ['Kode IND'] == industry_code:
                    industri_ketemu = True
                    break

            if industri_ketemu:
                break
            else:
                print("Kode industri tidak valid, masukkan kode industri yang valid")
        except ValueError:
            print("Input tidak valid, masukkan kode industri yang valid (angka)")

#menampilkan bisnis di industri yang diinginkan
    bisnis_dalam_industri = [] #kode industri = inputan akan dimasukkan ke list yang baru
    for business in businesses:
        if business['Kode IND'] == industry_code: #kalo ketemu lakukan << 
            bisnis_dalam_industri.append (business) #untuk masukkin ke list bisnis_dalam_industri
    
    print(f"\nIndustri di bisnis {industry_code}:")
    for business in bisnis_dalam_industri:
        print(f"{business['Nama Bisnis']} ({business['No. Telp']}), {business['Alamat']}, {business['Kode Pos']}")

#mengupdate bisnis
    while True:
        nama_bisnis_update = input("\nMasukkan nama bisnis yang ingin di update: ")
        bisnis_ketemu = any(business['Nama Bisnis'].lower() == nama_bisnis_update.lower() for business in bisnis_dalam_industri) #validasi input
        if bisnis_ketemu:
            break
        else:
            print("Nama bisnis tidak ada, masukkan nama bisnis sesuai informasi yang ada")

    bisnis_yg_dipilih = None
    for business in bisnis_dalam_industri:
        if business['Nama Bisnis'].lower() == nama_bisnis_update.lower():
            bisnis_yg_dipilih = business
            break

    while True:
        print("\nPilih update yang ingin anda lakukan:")
        print("1. Update nama bisnis")
        print("2. Update nomor telpon")
        print("3. Update kode pos")
        print("4. Update alamat")
        print("5. Kembali ke menu utama")

        while True:
            update_choice = input("Masukkan pilihan anda (1-5): ")
            if update_choice.isdigit() and 1 <= int(update_choice) <= 5:
                break
            else:
                print("Input tidak valid. Masukkan angka 1-5.")

        if update_choice == '1':
            new_name = input("Masukkan nama bisnis baru: ")
            bisnis_yg_dipilih['Nama Bisnis'] = new_name
        elif update_choice == '2':
            while True:
                new_telephone = input("Masukkan nomor telpon baru: ") 
                if new_telephone.isdigit():
                    bisnis_yg_dipilih['No. Telp'] = new_telephone
                    break
                else:
                    print("Input tidak valid. Masukkan nomor telpon yang benar (numerik)")

        elif update_choice == '3':
            while True:
                new_kode_pos = input("Masukkan kode pos baru: ") 
                if new_kode_pos.isdigit ():
                    bisnis_yg_dipilih['Kode Pos'] = new_kode_pos
                    break
                else:
                    print("Input tidak valid. Masukkan kode pos yang benar (numerik")
                
        elif update_choice == '4':
            new_address = input("Masukkan alamat baru: ")
            bisnis_yg_dipilih['Alamat'] = new_address
        elif update_choice == '5':
            print("Kembali ke menu utama")
            break

        print("Update berhasil!\n")

        update_another = input("Apa anda ingin mengupdate info lain untuk bisnis ini? (y/n): ").lower()
        if update_another != 'y':
            print("Kembali ke menu utama")
            break


# MENU 5 HAPUS DATA
def hapus_semua_industri():
    print("\nMenu hapus seluruh industri dan bisnisnya")
    display_industry_code()

    while True:
        try:
            choice = input("Masukkan kode industri yang hendak dihapus atau '0' untuk membatalkan: ")
            if choice == '0':
                print("Penghapusan dibatalkan")
                break

            if validasi_industry_code(choice):
                industry_code = int(choice)
                industry_ketemu = False

               #cari index untuk dihapus
                index_to_remove = None
                for index in range(len(industries)): 
                    if industries[index]['Kode IND']== industry_code:
                        index_to_remove = index 
                        industry_ketemu = True
                        break

                 # menghapus index
                if industry_ketemu:
                    del industries[index_to_remove] #menghapus industri dengan index nya
                    
                # Update bisnis setelah dihapus
                    updated_businesses = []
                    for business in businesses:
                        if business['Kode IND'] != industry_code:
                            updated_businesses.append(business)
                    businesses[:] = updated_businesses
                    
                    print ("Industri dan bisnis nya berhasil dihapus!")
                    break

                else: #prevent any errors dalam bentuk apapun
                    print("Kode industri tidak valid, masukkan kode industri yang valid")
            else:
                print("Kode industri tidak valid, masukkan kode industri yang valid")
        except ValueError:
            print("Kode industri tidak valid, masukkan kode industri yang valid")

def hapus_a_business():
    print("\nMenu hapus sebuah bisnis dalam industri")
    display_industry_code()

    while True:  # masukkan kode industri dulu beserta cegahan error" nya
        try:
            industry_code = int(input("Masukkan kode industri: "))
            industry_ketemu = False
            for industry in industries:
                if industry['Kode IND'] == industry_code:
                    industry_ketemu = True
                    break
            if industry_ketemu:
                break
            else:
                print("Kode industri tidak valid, masukkan kode yang benar")
        except ValueError:
            print("Kode industri tidak valid, masukkan kode yang benar (numerik)")

    businesses_in_industry = []  #list industri dalam bisnis
    for business in businesses:
        if business['Kode IND'] == industry_code:
            businesses_in_industry.append(business)

    if not businesses_in_industry:
        print("Bisnis tidak ditemukkan di industri ini, tidak ada yang bisa dihapus")
        return

    print(f"\nBisnis dalam industri {industry_code}:")  # pilihan benar
    display_data(businesses_in_industry)

    while True:  # looping ke dua untuk delete bisnis yang dipilih
        business_name = input("Masukkan nama bisnis yang ingin dihapus: ")
        bisnis_ketemu = False
        for business in businesses_in_industry:
            if business['Nama Bisnis'].lower() == business_name.lower():
                bisnis_ketemu = True
                break

        if bisnis_ketemu:
            break
        else:
            print("Nama bisnis tidak ada, masukkan nama bisnis sesuai informasi yang ada")

    # buat integrasi ke menu utama
    updated_businesses = [] #inisialisasi
    for business in businesses:
        if not (business['Nama Bisnis'].lower() == business_name.lower() and business['Kode IND'] == industry_code): #validasi 
            updated_businesses.append(business) #append to updated list
    businesses[:] = updated_businesses #slicing untuk update semua data ke database awal

    print("Bisnis berhasil dihapus!")

def hapus_data():
    while True:
        print("\nOpsi Hapus Data:")
        print("1. Hapus seluruh industri dan bisnisnya")
        print("2. Hapus sebuah bisnis dalam industri")
        print("3. Kembali ke menu utama")
        choice = input("Masukkan pilihan anda (1-3): ")

        if choice == '1':
            hapus_semua_industri()
        elif choice == '2':
            hapus_a_business()
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 1 atau 2.")

        hapus_another = input("Apa anda ingin menghapus yang lain? (y/n): ").lower()
        if hapus_another != 'y':
            print("Kembali ke menu utama")
            break

################## MAIN MENU ####################
while True:
    print ('\nSelamat Datang di Yellow Page Interactive Interface!')
    print ('\nUntuk memulai silahkan pilih menu dibawah:')
    print ('1. Tampilkan Semua Data')
    print ('2. Cari Data')
    print ('3. Tambah Data')
    print ('4. Update Data Existing')
    print ('5. Hapus Data')
    print ('6. Keluar dari program')

    choice = input ('Masukkan angka menu yang dipilih: ')

    if choice == "1":
        display_data (businesses) 
    elif choice == "2" :
        cari_data ()
    elif choice == "3" :
        tambah_data ()
    elif choice == "4" :
        update_data ()
    elif choice == "5" :
        hapus_data ()
    elif choice == '6':
        print("Terima kasih telah menggunakan Yellow Page Interactive Interface. Selamat tinggal!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih nomor 1 sampai 6.")


