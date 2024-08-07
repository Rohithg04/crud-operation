from django import forms

from new_app.models import WaterLand


class Water_Land(forms.ModelForm):
    class Meta:
        model = WaterLand
        fields = ("__all__")
