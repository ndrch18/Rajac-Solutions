from django import forms
from .models import RawMaterial, MaterialUnit

class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = '__all__'

    def _init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'material_category' in self.data:
            category = self.data.get('material_category')
            self.fields['material_unit'].queryset = (
                MaterialUnit.objects.filter(category=category)
            )
        elif self.instance.pk:
            self.fields['material_unit'].queryset=(
                MaterialUnit.objects.filter(
                    category=self.instance.material_category
                )
            )
        else:
            self.fields['material_unit'].queryset = MaterialUnit.objects.none()