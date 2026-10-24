from django import forms
from .models import Category


class ProductFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        label="Categoría",
        queryset=Category.objects.order_by("name"),
        required=False,
        empty_label="Todas las categorías",
        error_messages={
            "invalid_choice": "Selecciona una categoría válida."
        },
    )

    min_price = forms.DecimalField(
        label="Precio mínimo (S/)",
        required=False,
        min_value=0,
        max_digits=8,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={"step": "0.01", "placeholder": "0.00"}
        ),
    )

    max_price = forms.DecimalField(
        label="Precio máximo (S/)",
        required=False,
        min_value=0,
        max_digits=8,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={"step": "0.01", "placeholder": "Sin límite"}
        ),
    )

    def clean(self):
        data = super().clean()

        minimum = data.get("min_price")
        maximum = data.get("max_price")

        if minimum is not None and maximum is not None:
            if minimum > maximum:
                raise forms.ValidationError(
                    "El precio mínimo no puede ser mayor "
                    "que el precio máximo."
                )

        return data