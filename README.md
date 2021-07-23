# peminjaman_buku
requirement 
python 3.6
django==3.0
django-rest-framework==3.10.2
django-redis==2019.2
mysql-client

Alasan patern project
Peminjaman buku memiliki foreign_key yang memiliki relasi one to many, yaitu dengan table buku dan table anggota. Saya menggunakan scema tersebut karena lebih simple dan mengaksesnya tidak teralu rumit Ketika diterapkan pada “view.py: (controller) django
