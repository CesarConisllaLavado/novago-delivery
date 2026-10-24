from django.shortcuts import get_object_or_404, render

from .forms import ProductFilterForm
from .models import Product


def product_list(request):
    form = ProductFilterForm(request.GET)

    products = (
        Product.objects.filter(is_active=True)
        .select_related("category")
        .order_by("name", "pk")
    )

    if form.is_valid():
        filters = form.cleaned_data

        if filters["category"] is not None:
            products = products.filter(
                category=filters["category"]
            )

        if filters["min_price"] is not None:
            products = products.filter(
                price__gte=filters["min_price"]
            )

        if filters["max_price"] is not None:
            products = products.filter(
                price__lte=filters["max_price"]
            )

    else:
        products = products.none()

    return render(
        request,
        "products/product_list.html",
        {
            "products": products,
            "form": form,
        },
    )


def product_detail(request, pk):
    product = get_object_or_404(
        Product,
        pk=pk,
        is_active=True,
    )

    return render(
        request,
        "products/product_detail.html",
        {"product": product},
    )