from django.shortcuts import render
from .models import Produk


def product_list(request):
    # Fetch all products, including related kategori and status objects
    products = Produk.objects.select_related("kategori", "status").all()

    # Filter by status 'bisa dijual' if needed, or let the template handle it
    # For now, let's just pass all products.

    return render(request, "cetakapp/product_list.html", {"products": products})
