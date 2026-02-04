from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Produk


@ensure_csrf_cookie
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


@require_POST
def delete_product(request, product_id):
    """Delete a product from the database."""
    try:
        product = get_object_or_404(Produk, id_produk=product_id)
        product_name = product.nama_produk
        product.delete()
        return JsonResponse(
            {"success": True, "message": f"Produk '{product_name}' berhasil dihapus."}
        )
    except Exception as e:
        return JsonResponse(
            {"success": False, "message": f"Gagal menghapus produk: {str(e)}"},
            status=500,
        )
