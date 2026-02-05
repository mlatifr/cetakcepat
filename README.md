CARA INSTALL PERTAMA KALI

1 clone repo. menggunakna django 4.2
2 bikin DB latif_cetak pada Xampp/phpmyadmin
3 python3 manage.py migrate
4 cd latif_cetak
5 pipenv install pymsql
6 python3 manage.py fetch_api (untuk insert auto dari API ke database MySql)

struktur folder:
1 kode untuk insert data dari API 
cetakcepat/latif_cetak/cetakapp/management/commands/fetch_api.py


2 database untuk migrate
/Users/ryancahyafirdaus/Documents/LOKER/FASPRINT/cetak_cepat/cetakcepat/latif_cetak/cetakapp/models.py

3 template all data: product_list.html
4 template delete modal
5 template add & edit: product_form.html

alur
1 filter status
        product_list.html menampilkan tombol filter status & list product.
        list product dan logika filter status ada di views.py
        product yang ditampilkan sesuai filter dari fungsi product_list
2 hapus
        POST id & nama product_list.html pada showDeleteModal
        _delete_modal.html untuk html modal nya
        modal.js menyimpan ID produk dengan Global variable. 
        kemudian klik hapus, akan trigger listener fetch Hapus.
        di views.py ada handling POST delete.
3 add product
        add_product views.py bagian else
        masuk halaman from produk.html
        kirim post. masuk lagi ke add_product views.py
        validasi form. syarat nya ada di models.py.
        jika valid, simpan ke DB.
4 edit product
        dari list html klik edit
        kemudian urls.py akan mengarahkna ke views.py edit_product bagian else
        cari id produt, masuk ke halaman product_form.html
        klik simpan, masuk ke edit_product views.py
        cek validasi di models.py
        jika valid, update ke DB.



        
