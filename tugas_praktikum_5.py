data = {}
while True:
    print("")
    x = input("(L)ihat, (T)ambah, (U)bah, (H)apus,(C)ari, (K)eluar: ")
    if x.lower() == "k":
        print("\n== Anda sudah keluar dari program ini ==")
        break
    elif x.lower() == "l":
        if data.items():
            print("\n================================== Daftar Nilai ======================================")
            print("======================================================================================")
            print("|  NO. |      NAMA     |     NIM    |    TUGAS   |   UTS   |   UAS   |  NILAI AKHIR  |")
            print("======================================================================================")
            i = 0
            for x in data.items():
                i += 1
                print("| {6:4} | {0:13s} | {1:13} | {2:8d} |  {3:6d} | {4:7d} | {5:12.2f} | " 
                      .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("======================================================================================")
        else:
            print("\n===================================== Daftar Nilai ===================================")
            print("======================================================================================")
            print("|  NO. |      NAMA     |      NIM      |   TUGAS  |   UTS   |   UAS   | NILAI AKHIR  |")
            print("======================================================================================")
            print("|                                 TIDAK ADA DAFTAR NILAI                             |")
            print("======================================================================================")
    elif x.lower() == "t":
        print("\n== Tambah Data Mahasiswa\t: ==")
        nama = input("Nama\t\t: ")
        nim = int(input("NIM\t\t: "))
        tugas = int(input("NIlai Tugas\t: "))
        uts = int(input("Nilai UTS\t: "))
        uas = int(input("Nilai UAS\t: "))
        nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
    elif x.lower() == "u":
        print("\n== Edit Data Nilai Mahasiswa ==")
        nama = input("Masukan Nama Mahasiswa\t: ")
        if nama in data.keys():
            nim = input("NIM\t\t\t: ")
            tugas = int(input("Nilai Tugas Baru\t: "))
            uts = int(input("Nilai UTS Baru\t\t: "))
            uas = int(input("Nilai UAS Baru\t\t: "))
            nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
            data[nama] = nim, tugas, uts, uas, nilaiakhir
        else:
            print("Data nilai{0} tidak ada ".format(nama))
    elif x.lower() == "h":
        print("\n== Hapus Data Nilai Mahasiswa ==")
        nama = input("Masukan Nama Mahasiswa\t: ")
        if nama in data.keys():
            del data[nama]
        else:
            print("\nData {0} tidak ada".format(nama))
    elif x.lower() == "c":
        print("\n== Cari Data Nilai Mahasiswa ==")
        nama = input("Masukan Nama Mahasiswa\t: ")
        if nama in data.keys():
            print("\n=============== Daftar Nilai ==================")
            print("===============================================")
            print("|NAMA | NIM | TUGAS | UTS | UAS | NILAI AKHIR |")
            print("| {0} | {1} |\t".format(nama, data[nama]))
            print("===============================================")
        else:
            print("\nData dari {0} tidak ada ".format(nama))
    else:
        print("\n== Pilih Menu Yang Tersedia ==")
