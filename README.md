# TUGAS PRAKTIKUM 5 - PERTEMUAN 9

Nama        : Bangkit Akbar Anggara<br>
NIM        : 312010148<br>
Kelas        : TI.20.B.1<br>

# TUGAS

Pada pertemuan ke-9 saya diberi tugas oleh dosen saya untuk membuat program sederhana seperti gambar dibawah ini:<br>
  ![tugas_5.png](Pic/tugas_5.png)

Ketika kita belum memasukkan data siswa maka akan muncul seperti gambar di bawah ini:
  ![tugas_tidak_ada_data.png](Pic/tugas_tidak_ada_data.png)
  
Lalu setelah memasukkan data siswa maka outputnya harus seperti ini:
  ![tugas_menambahkan_data.png](Pic/tugas_menambahkan_data.png)
  
Oke mari kita mulai mengerjakan tugasnya, untuk source code/syntax yang saya gunakan silahkan kalian lihat disini [Click Here](tugas_praktikum_5.py)

Oke setelah kalian lihat saya akan menjelaskan fungsi - fungsinya :

1. Syntax untuk membuat pilihan menambah data, melihat data, menhapus data, mencari data atau keluar dari program<br>
Keterangan:
    - Pertama kita buat dictionary kosong dulu yap kita tulis data:{} dictionary hampir sama dengan list hanya saja bedanya list menggunakan tanda kurung siku[], sementara dictionary menggunakan tanda kurung kurawal {}<br>
    - Setelah membuat data dictionary kosong kita akan menggunakan perulangan while True dan membuat sebuah inputan pilihan apakah kita ingin menambah data, melihat data, menhapus data, mencari data atau keluar dari program<br>
    - Lalu kita buat x =  input untuk memasukkan pilihan tadi<br>
      ![pilih.png](Pic/pilih.png)
 


2. Syntax untuk keluar dari program<br>
Keterangan :
    - Kita akan menggunakan if untuk mengeksekusi code/syntax jika kondisi bernilai benar/True<br>
    - Lalu gunanya x.lower adalah lower di gunakan untuk mengubah atau mengkonversi huruf - huruf yang ada pada kalimat supaya menjadi berhuruf kecil, sementara x adalah data pilihan yang kita pilih sebelumnya<br>
    - Lalu kita tulis kata - kata untuk menunjukan bahwa anda sudah benar - benar keluar<br>
    - Lalu kita gunakan fungsi break untuk keluar dari program<br>
      ![keluar.png](Pic/keluar.png)


3. Syntax untuk melihat data dictionary/data siswa<br>
Keterangan :
    - Disini kita menggunakan elif untuk menyeleksi data dan elif merupakan lanjutan/percabangan dari logika if
    - Kita gunakan fungsi if untuk mencetak/print data siswa yang sudah di inputkan makanya kita menggunakan data.items()<br>
    - Lalu kita gunakan print untuk membuat table agar terlihat lebih rapih<br>
    - Lalu gunanya for untuk melakukakan perulangan nomor dan juga data siswa yang kita inputkan nanti<br>
    - Lalu kita buat lagi di bawahnya else agar ketika kita belom menginputkan data siswa akan muncul tidak ada data / tidak ada daftar nilai
      ![lihat.png](Pic/lihat.png)

4. Syntax untuk menambah data siswa<br>
Keterangan:
    - Disini kita akan menggunakan inputan data seperti biasa Nama, NIM, Hasil Tugas, Hasil UTS, Hasil UAS, dan juga Hasil Akhir<br>
    - Untuk nama kita cukup ketikan input di python 3 raw_input dengan input sama saja karena sudah di satukan dan kita menggunakan integer untuk bagian NIM dan juga Hasil Tugas, UTS, UAS, dan Hasil Akhir<br>
    - Lalu kita akan menghitung Hasil Akhir dengan cara menambahkan semua Hasil Tugas, UTS, dan UAS tentu saja kita menggunakan 30/100 dan 35/100 karena di dalam tugasnya seperti itu<br>
      ![tambah.png](Pic/tambah.png)
      
      
5. Syntax untuk mengubah data siswa<br>
Keterangan:
    - Disini kita menggunakan elif untuk menyeleksi data dan elif merupakan lanjutan/percabangan dari logika if
    - Kita gunakan input untuk memasukkan nama siswa yang ingin data nilainya kita ubah<br>
    - Disini kita akan mengubah fungsi if lagi untuk mengeksekusi syntax di data.keys<br>
    - Lalu kita masukkan NIM dan juga tugas yang sudah diperbarui/diperbaiki<br>
    - Lalu else di gunakan jika kita belom menginputkan data mahasiswa sama sekali sehingga akan muncul tampilan data(nama siswa yang ingin di ubah nilainya)tidak ada<br>
      ![ubah.png](Pic/ubah.png)
      
      
6. Syntax untuk menghapus data siswa<br>
Keterangan:
    - Disini kita menggunakan elif untuk menyeleksi data dan elif merupakan lanjutan/percabangan dari logika if
    - Kita gunakan input untuk memasukkan nama siswa yang ingin datanya kita hapus<br>
    - Lalu kita gunakan if lagi dan data.keys<br>
    - Lalu del data[nama] untuk menghapus data siswa tersebut<br>
    - Lalu kita gunakan else jika kita belom menginputkan data sama sekali sehingga muncul tampilan data(nama siswa yang ingin di hapus)tidak ada<br>
      ![hapus.png](Pic/hapus.png)
      
     
7. Syntax untuk mencari data siswa<br>
Keterangan:
    - Disini kita menggunakan elif untuk menyeleksi data dan elif merupakan lanjutan/percabangan dari logika if
    - Kita gunakan input untuk mencari data siswa dengan namanya<br>
    - Lalu kita gunakan if lagi untuk mengeksekusi data siswa<br>
    - Lalu print menggunakan table agar terlihat lebih rapih<br>
    - Lalu else di gunakan jika kita belom menginputkan data sehingga muncul tampilan data dari(nama siswa yang di cari)tidak ada<br>
      ![cari.png](Pic/cari.png)
      
      
8. Syntax jika kita tidak memilih salah satu pada pilihan menu<br>
Keterangan:
    - Disini kita menggunakan else untuk mengeksekusi code/syntax jika bernilai False<br>
    - Kita disuruh memilih ingin menambahkan data, melihat data, mengubah data, mencari data, atau keluar dari program<br>
    - Jadi ketika kita tidak memilih pilihan apapun maka akan muncul tulisan pilih menu yang tersedia<br>
      ![memilih.png](Pic/memilih.png)
      

Oke itu adalah penjelasan dari masing -  masing syntax dan fungsinya, maka jika kita jalankan atau run syntaxnya makan akan muncul seperti ini:

1. Pilihan untuk menambahkan, mengubah, mencari, melihat, menghapus, dan keluar<br>
    ![output_pilih.png](Pic/output_pilih.png)
    
 
2. Keluar dari program<br>
    ![output_keluar.png](Pic/output_keluar.png)


3. Melihat dictionary jika kita belom menginputkan data siswa<br>
    ![output_tidak_ada_data.pnt](Pic/output_tidak_ada_data.png)
 

4. Menambah data siswa dan melihat data siswa tersebut
    ![tambah_dan_lihat.png](Pic/tambah_dan_lihat.png)
    
    
5. Mengubah data siswa dan melihat hasil perubahan data nilai siswa tersebut<br>
    ![ubah_dan_lihat.png](Pic/ubah_dan_lihat.png)
    
 
6. Menghapus data siswa dan melihat data siswa apakah sudah terhapus atau belum<br>
    ![hapus_dan_lihat.png](Pic/hapus_dan_lihat.png)
    
  
7. Mencari data siswa dengan namanya<br>
    ![output_cari.png](Pic/output_cari.png)
    
   
8. Jika kita tidak memilih pilihan tambah, hapus, cari, ubah, atau keluar
    ![output_memilih.png](Pic/output_memilih.png)
    
    
Oke dengan begini selesai sudah tugas pada pertemuan ke-9 sampai jumpa

by:
# == Bangkit Akbar Anggara ==
# == 312010148 ==
# == TI.20.B.1 ==
