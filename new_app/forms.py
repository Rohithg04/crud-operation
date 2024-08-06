from django import forms

from new_app.models import WaterLand


class WaterLand(forms.ModelForm):
    class Meta:
        model = WaterLand
        fields = ("__all__")
