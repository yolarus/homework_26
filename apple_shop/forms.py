from django.core.exceptions import ValidationError
from django.forms import ImageField, ModelForm

from .models import Product

BAD_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(ModelForm):
    """
    Форма для создания и редактирования товара интернет-магазина
    """
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Стилизация формы при инициализации
        """
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Название товара"
        })
        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Описание товара",
            "rows": 4
        })
        self.fields["photo"].widget.attrs.update({
            "class": "form-control"
        })
        self.fields["category"].widget.attrs.update({
            "class": "form-select"
        })
        self.fields["price_per_unit"].widget.attrs.update({
            "class": "form-control"
        })

    def clean_price_per_unit(self):
        """
        Проверка, что цена товара неотрицательна
        """
        price_per_unit = self.cleaned_data["price_per_unit"]
        if price_per_unit < 0:
            raise ValidationError("Цена товара не может быть меньше нуля")
        return price_per_unit

    def clean_name(self):
        """
        Проверка наличия нецензурных слов в полях name и description
        """
        name = self.cleaned_data["name"]
        return self.check_bad_words("name", name)

    def clean_description(self):
        """
        Проверка наличия нецензурных слов в полях name и description
        """
        description = self.cleaned_data["description"]
        return self.check_bad_words("description", description)

    def check_bad_words(self, field: str, data: str):
        """
        Проверка наличия нецензурных слов в переданном поле
        :param field: Имя поля формы
        :param data: Значение, введенное в поле формы
        :return: Значение, введенное в поле формы
        """
        for word in BAD_WORDS:
            if word in data.lower():
                self.add_error(field, f"В данном поле не может содержаться слово '{word}'")
        return data

    def clean_photo(self):
        """
        Проверка веса и формата загружаемой фотографии
        """
        photo = self.files.get("photo")
        max_size = 5 * 1024 ** 2
        if photo:
            if photo.size > max_size:
                raise ValidationError("Размер изображения не должен превышать 5 Мб")
            elif photo.content_type not in ["image/jpeg", "image/jpg", "image/png"]:
                raise ValidationError("Можно загрузить файлы только форматов JPEG, JPG, PNG")
            return photo
        else:
            return False
