from django.forms import ModelForm

from .models import Article


class ArticleForm(ModelForm):
    """
    Форма для создания и редактирования статьи в блоге
    """
    class Meta:
        model = Article
        exclude = ["views_count"]

    def __init__(self, *args, **kwargs):
        """
        Стилизация формы при инициализации
        """
        super(ArticleForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Заголовок статьи"
        })
        self.fields["body"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Текст статьи",
            "rows": 8
        })
        self.fields["preview"].widget.attrs.update({
            "class": "form-control"
        })
        self.fields["is_published"].widget.attrs.update({
            "class": "form-check-input"
        })
