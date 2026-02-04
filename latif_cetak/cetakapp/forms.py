from django import forms
from .models import Produk


class ProductForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ["nama_produk", "harga", "kategori", "status"]
        widgets = {
            "nama_produk": forms.TextInput(
                attrs={"class": "form-control", "required": "required"}
            ),
            "harga": forms.NumberInput(
                attrs={"class": "form-control", "required": "required"}
            ),
            "kategori": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            "nama_produk": "Nama Produk",
            "harga": "Harga",
            "kategori": "Kategori",
            "status": "Status",
        }
