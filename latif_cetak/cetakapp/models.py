from django.db import models


class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_kategori


class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    nama_status = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_status


class Produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=12, decimal_places=2)
    kategori = models.ForeignKey(
        Kategori, on_delete=models.CASCADE, related_name="produk"
    )
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="produk")

    def __str__(self):
        return self.nama_produk
