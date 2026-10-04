# Minpro-2-DDP-Sistempengelolaandatamahasiswa

## Nama: Dheystrin Gloria Nafisya
## NIM : 2609116063

### Penjelasan
Program lanjutan dari minpro 1 hanya menambahkan beberapa hal seperti, 
1. Library yaitu PrettyTable, os, dan time
2. Menambahkan Dictionary & Function
3. Membedakan menu role admin dan user, role admin memiliki akses CRUD lengkap sedangkan role user hanya 2 yaitu tampilkan data dan keluar.

### Flowchart
<img width="1977" height="1830" alt="minpro2 drawio (4)" src="https://github.com/user-attachments/assets/5d7ce8a6-7244-4876-86bd-9a810e50813f" />
1. Alur flowchart pertama kita memasukkan username & password, jika username & password valid program lanjut mengecek role namun jika tidak valid program akan menampilkan "username atau password salah" dan kembali ke masukkan username & password
<br>2. role "admin" program menampilkan 5 menu yaitu tambah, tampilkan, ubah, hapus data dan keluar, admin memasukkan pilihan 1-5 saat admin memilih pilihan 5 maka program selesai/berhenti
<br>3. Jika role "user" program menampilkan 2 menu yaitu tampilkan data dan keluar

### Program dan Output
<img width="233" height="202" alt="Screenshot 2026-10-04 212945" src="https://github.com/user-attachments/assets/dcbfeb0b-1476-4e38-8be3-fe364f4e3e3f" />
<br>Program library dan dictionary role yaitu dictionary bersarang (nested dictionary) 
<br><img width="321" height="209" alt="Screenshot 2026-10-04 213009" src="https://github.com/user-attachments/assets/97897ca6-901e-43a1-a976-e3e24e8ed2dc" />
<br> funcition yaitu def login saat username dan password yang dimasukkan sesuai dengan role yang dipilih program akan melanjutkan
<br><img width="378" height="380" alt="Screenshot 2026-10-04 213024" src="https://github.com/user-attachments/assets/70632b5d-e709-43ae-9f5b-46e42b75d8aa" />
<br> def tampilkan data untuk tablenya kita memakai library PrettyTable agar data mahasiswa terlihat lebih rapi, lalu def tambah data menambahkan data baru yaitu nama, jurusan, dan nilai selain itu diakhir saya menambahkan library time untuk menjeda beberapa detik sebelum program melanjutkan
<br><img width="421" height="279" alt="Screenshot 2026-10-04 213047" src="https://github.com/user-attachments/assets/3d4b3454-68e0-4d6f-9edc-86296a273cd6" />
<br> def ubah data untuk mengubah data yang kita inginkan di bagian ini saya juga menambahkan library time untuk menjeda beberapa detik sebelum program melanjutkan
<br><img width="397" height="225" alt="Screenshot 2026-10-04 213113" src="https://github.com/user-attachments/assets/b3fbdfef-4038-4d63-b1aa-92afe7d82791" />
<br> def hapus data untuk menghapus data yang kita mau lalu dibagian akhir saya juga menambahkan library time untuk menjeda beberapa detik sebelum program melanjutkan
<br><img width="368" height="63" alt="Screenshot 2026-10-04 213149" src="https://github.com/user-attachments/assets/236a7609-f27a-41ef-871d-5faa97038533" />
dibagian ini saya menambakan library os untuk membuat tampilan terminal bersih
<br><img width="315" height="415" alt="Screenshot 2026-10-04 213219" src="https://github.com/user-attachments/assets/e34bd882-ca20-47c3-a0f4-f607eec372b8" />
<br> menampilkan menu 1-5, menu 1-4 dipanggil menggunakan function tambah data, tampilkan data, ubah data, hapus data lalu menu 5 menggunakan break untuk mengakhiri program
<br><img width="352" height="293" alt="Screenshot 2026-10-04 213231" src="https://github.com/user-attachments/assets/11e15a3e-305b-4941-9547-18f051e3adeb" />
<br> selanjutnya menu user hanya ada 2 pilihan yaitu tampilkan data dan keluar

#### outputnya
<img width="110" height="44" alt="Screenshot 2026-10-04 212740" src="https://github.com/user-attachments/assets/83c85de6-2316-40d8-9865-181f0e314215" />
<br><img width="269" height="401" alt="Screenshot 2026-10-04 212558" src="https://github.com/user-attachments/assets/67643771-cdc8-438f-b734-ffc3dc8b4747" />
<br> saat memasukkan username dan password lalu menekan enter program akan membersihkan tampilan, pilihan 1 menambahkan data baru lalu pilihan 2 menampilkan tabel data mahasiswa
<br><img width="239" height="265" alt="Screenshot 2026-10-04 212633" src="https://github.com/user-attachments/assets/dc75f83c-41e8-473c-8b80-8c66d273bd33" />
<br> pilihan 3 untuk mengubah data dan akan jeda beberapa detik sebelum program kembali ke menu
<br><img width="343" height="352" alt="Screenshot 2026-10-04 212654" src="https://github.com/user-attachments/assets/34a865bb-261b-492a-be89-b9d4f22880aa" />
<br> pilihan 4 untuk menghapus data yang kita inginkan dan pilihan 5 untuk mengakhiri program
<br><img width="338" height="264" alt="Screenshot 2026-10-04 212843" src="https://github.com/user-attachments/assets/d5de3400-2230-40f4-bcad-f467929648e1" />
<br> output role user yang memiliki 2 menu yaitu tampilkan data dan keluar

### penjelasan nilai tambah
saya menambahkan 3 library yaitu PrettyTable, os, dan time seperti yang sudah saya jelaskan pada program dan outpun diatas
<img width="233" height="47" alt="Screenshot 2026-10-04 212945" src="https://github.com/user-attachments/assets/7da64fec-5fad-4058-b323-9e866cf289e2" />



