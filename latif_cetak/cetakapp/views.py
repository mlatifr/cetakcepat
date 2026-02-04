from django.shortcuts import render
from .models import Produk


def product_list(request):
    # Get status filter from query parameter
    status_filter = request.GET.get("status", "all")

    # Fetch all products, including related kategori and status objects
    products = Produk.objects.select_related("kategori", "status").all()

    # Apply filtering based on status
    if status_filter == "bisa":
        products = products.filter(status__nama_status="bisa dijual")
    elif status_filter == "tidak":
        products = products.filter(status__nama_status="tidak bisa dijual")

    context = {"products": products, "current_status": status_filter}

    return render(request, "cetakapp/product_list.html", context)
