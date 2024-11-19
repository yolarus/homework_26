from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Category, ContactData, Product


# Create your views here.
class IndexListView(ListView):
    """
    Класс-представление страницы "Главная"
    """
    model = Product
    template_name = "apple_shop/index.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-updated_at")


class CatalogListView(ListView):
    """
    Класс-представление страницы "Каталог"
    """
    model = Category
    template_name = "apple_shop/catalog.html"
    context_object_name = "categories"


# def catalog(request: HttpRequest) -> HttpResponse:
#     """
#     Рендер страницы "Каталог" приложения
#     """
#     categories = Category.objects.all()
#     context = {"categories": categories}
#     return render(request, "apple_shop/catalog.html", context=context)


def categories(request: HttpRequest) -> HttpResponse:
    """
    Рендер страницы "Категории" приложения
    """
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {"categories": categories,
               "products": products}
    return render(request, "apple_shop/categories.html", context=context)


def category_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Рендер страницы категории в интернет-магазине
    """
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    context = {"category": category,
               "products": products}
    return render(request, "apple_shop/category_detail.html", context=context)


def product_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Рендер страницы товара в интернет-магазине
    """
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "apple_shop/product_detail.html", context=context)


def contacts(request: HttpRequest) -> HttpResponse:
    """
    Рендер страницы "Контакты" приложения
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Получено сообщение '{message}' от пользователя {name} ({email})")
        return HttpResponse("Ваше сообщение успешно отправлено!")

    contact = ContactData.objects.get(id=1)
    context = {"contact": contact}

    return render(request, "apple_shop/contacts.html", context=context)


def owner(request: HttpRequest) -> HttpResponse:
    """
    Рендер страницы "Владелец" приложения
    """
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price_per_unit = request.POST.get("price_per_unit")
        category = request.POST.get("category")
        photo = request.FILES.get("photo")
        Product.objects.create(
            name=name,
            description=description,
            price_per_unit=price_per_unit,
            category=Category.objects.get(name=category),
            photo=photo
        )
        return HttpResponse("Новый товар успешно добавлен!")

    contact = ContactData.objects.get(id=1)
    context = {"contact": contact}

    return render(request, "apple_shop/owner.html", context=context)
