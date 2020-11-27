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
  - lalu kita buat x =  input untuk memasukkan pilihan tadi<br>
     ![pilih.png](Pic/pilih.png)<br>
  - Lalu jika kita run syntaxnya maka akan muncul seperti berikut ini<br>
     ![output_pilih.png](Pic/output_pilih.png) 


2. Syntax untuk keluar dari program<br>
Keterangan :
  - Kita akan menggunakan if untuk mengeksekusi code/syntax jika kondisi bernilai benar/True<br>
  - lalu gunanya x.lower adalah lower di gunakan untuk mengubah atau mengkonversi huruf - huruf yang ada pada kalimat supaya menjadi berhuruf kecil, sementara x adalah data pilihan yang kita pilih sebelumnya<br>
  - Lalu kita tulis kata - kata untuk menunjukan bahwa anda sudah benar - benar keluar<br>
  - Lalu kita gunakan fungsi break untuk keluar dari program<br>
    ![keluar.png](Pic/keluar.png)<br>
  - Lalu jika kita run maka hasilnya akan seperti berikut<br>
    ![output_keluar.png](Pic/output_keluar.png)


3. Syntax untuk melihat data dictionary/data siswa<br>
Keterangan :
  - Kita gunakan funsgi if untuk mencetak/print data siswa yang sudah di inputkan makanya kita menggunakan data.items()<br>
  - Lalu kita gunakan print untuk membuat table agar terlihat lebih rapih 
  
