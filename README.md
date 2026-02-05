# Cetak Cepat – Django Project

Project ini adalah aplikasi **Django 4.2** untuk manajemen produk (list, filter, tambah, edit, hapus) dengan data awal yang dapat di-*fetch* otomatis dari API dan disimpan ke database **MySQL**.

---

## 🛠️ Tech Stack

* Python 3
* Django 4.2
* MySQL (XAMPP / phpMyAdmin)
* Pipenv

---

## 🚀 Cara Install Pertama Kali

1. **Clone repository**

   ```bash
   git clone https://github.com/mlatifr/cetakcepat
   cd cetakcepat
   ```

2. **Buat database**

   * Jalankan XAMPP
   * Buka phpMyAdmin
   * Buat database dengan nama:

     ```text
     latif_cetak
     ```

3. **Aktifkan environment & install dependency**

   ```bash
   pipenv install
   pipenv shell
   pipenv install pymysql
   ```

4. **Migrasi database**

   ```bash
   cd latif_cetak
   python3 manage.py migrate
   ```

5. **Fetch data dari API (insert otomatis ke MySQL)**

   ```bash
   python3 manage.py fetch_api
   ```

6. **Jalankan server**

   ```bash
   python3 manage.py runserver
   ```

---

## 📂 Struktur Folder Penting

### 1️⃣ Fetch & Insert Data dari API

Digunakan untuk mengambil data dari API dan menyimpannya ke database.

```text
cetakcepat/
└── latif_cetak/
    └── cetakapp/
        └── management/
            └── commands/
                └── fetch_api.py
```

### 2️⃣ Database & Model

Digunakan untuk definisi tabel dan validasi data.

```text
cetakapp/models.py
```

### 3️⃣ Template

* **List & Filter Data**

  ```text
  product_list.html
  ```
* **Modal Delete**

  ```text
  _delete_modal.html
  ```
* **Form Add & Edit Product**

  ```text
  product_form.html
  ```

---

## 🔄 Alur Aplikasi

### 1️⃣ Filter Status Produk

* `product_list.html`

  * Menampilkan tombol filter status
  * Menampilkan list produk
* Logika filter ada di `views.py`
* Data yang ditampilkan menyesuaikan filter dari fungsi `product_list`

---

### 2️⃣ Hapus Produk

* Dari `product_list.html`

  * Kirim **POST** berupa `id` dan `nama produk`
  * Trigger fungsi `showDeleteModal`
* `_delete_modal.html`

  * Berisi tampilan modal konfirmasi hapus
* `modal.js`

  * Menyimpan **ID produk** dalam global variable
  * Tombol *Hapus* akan memicu request `fetch` delete
* `views.py`

  * Menangani request **POST delete** dan menghapus data dari database

---

### 3️⃣ Tambah Produk

* Masuk ke `add_product` di `views.py` (branch `else`)
* Redirect ke halaman:

  ```text
  product_form.html
  ```
* Submit form (POST)
* Kembali ke `add_product` di `views.py`
* Validasi data berdasarkan aturan di `models.py`
* Jika valid → data disimpan ke database

---

### 4️⃣ Edit Produk

* Dari `product_list.html` klik **Edit**
* `urls.py` mengarahkan ke `edit_product` di `views.py`
* Ambil data produk berdasarkan `id`
* Tampilkan di:

  ```text
  product_form.html
  ```
* Klik **Simpan**
* Masuk kembali ke `edit_product` di `views.py`
* Validasi data di `models.py`
* Jika valid → data di-*update* ke database

---

## ✅ Catatan

* Pastikan konfigurasi database di `settings.py` sesuai dengan MySQL lokal
* Jalankan `fetch_api` hanya jika ingin mengisi data awal dari API

---

📌 **Author**: Aldi
