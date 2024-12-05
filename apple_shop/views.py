from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ProductForm
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


class CategoryListView(ListView):
    """
    Класс-представление страницы "Категории"
    """
    model = Category
    template_name = "apple_shop/category_list.html"
    context_object_name = "categories"

    @staticmethod
    def get_products():
        """
        Получение всех товаров для вывода на страницу
        """
        return Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["products"] = self.get_products()
        return context


class CategoryDetailView(DetailView):
    """
    Класс-представление страницы "Категория"
    """
    model = Category
    template_name = "apple_shop/category_detail.html"
    context_object_name = "category"

    def get_products_in_category(self):
        """
        Получение товаров категории для вывода на страницу
        """
        return Product.objects.filter(category=super().get_object())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["products"] = self.get_products_in_category()
        return context


class ProductDetailView(DetailView):
    """
    Класс-представление страницы "Товар"
    """
    model = Product
    template_name = "apple_shop/product_detail.html"
    context_object_name = "product"


class ContactsDetailView(DetailView):
    """
    Класс-представление страницы "Контакты"
    """
    model = ContactData
    template_name = "apple_shop/contacts.html"
    context_object_name = "contact"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Получено сообщение '{message}' от пользователя {name} ({email})")
        return HttpResponse("Ваше сообщение успешно отправлено!")


class ProductCreateView(CreateView):
    """
    Класс-представление страницы "Владелец"
    """
    model = Product
    form_class = ProductForm
    template_name = "apple_shop/owner.html"
    success_url = reverse_lazy("apple_shop:index")


class ProductUpdateView(UpdateView):
    """
    Класс-представление страницы "Владелец"
    """
    model = Product
    form_class = ProductForm
    template_name = "apple_shop/owner.html"
    success_url = reverse_lazy("apple_shop:index")

    def get_success_url(self):
        """
        Перенаправление на страницу товара
        """
        return reverse("apple_shop:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    """
    Класс-представление страницы "Владелец"
    """
    model = Product
    template_name = "apple_shop/product_confirm_delete.html"
    success_url = reverse_lazy("apple_shop:index")
