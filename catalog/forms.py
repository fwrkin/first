from django.forms import ModelForm, forms

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите описание продукта'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Прикрепите фото продукта'})
        self.fields['category'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Выберите категорию продукта'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену продукта'})

    forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    def clean_name(self):
        name = self.cleaned_data.get('name')

        for word in self.forbidden_words:
            if word.lower() in name.lower():
                raise forms.ValidationError('Данное слово нельзя использовать в названии продукта')

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')

        for word in self.forbidden_words:
            if word.lower() in description.lower():
                raise forms.ValidationError('Данное слово нельзя использовать в описании продукта')

        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0:
            raise forms.ValidationError('Цена не может быть меньше 0!')

        return price


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ['publication_status']