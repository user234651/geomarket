# orders/forms.py
from django import forms

class OrderForm(forms.Form):
    BANK_CHOICES = [
        ('sber', 'Сбер'),
        ('tinkoff', 'Т-Банк'),
        ('alfa', 'Альфа Банк'),
    ]

    full_name = forms.CharField(label="ФИО", max_length=100)
    email = forms.EmailField(label="Email")
    card_number = forms.CharField(label="Номер карты", max_length=20)
    bank = forms.ChoiceField(label="Банк", choices=BANK_CHOICES)
    expiry_date = forms.DateField(
        label="Срок действия (мм/гг)",
        widget=forms.DateInput(attrs={
            'type': 'month',
        }),
        input_formats=['%Y-%m']
    )
    cvc = forms.CharField(
        label="CVC2/CVV2",
        max_length=4,
        widget=forms.PasswordInput(render_value=False),
    )
