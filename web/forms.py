import django.forms

from web.models import Review, Order


class ReviewForm(django.forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class OrderCreateForm(django.forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
