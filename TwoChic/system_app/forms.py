from django import forms
from .models import RawMaterial, MaterialUnit, MaterialCategory

class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = [
            "material_category",
            "material_name",
            "material_unit",
            "material_quantity",
            "material_unitprice",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set custom placeholder for category (use MaterialCategory.choices to avoid separator)
        self.fields["material_category"].choices = [("", "Choose Category")] + list(MaterialCategory.choices)

        # add your modal classes
        self.fields["material_category"].widget.attrs.update({"class": "form-select custom-input", "id": "id_material_category"})
        self.fields["material_name"].widget.attrs.update({"class": "form-control custom-input", "placeholder": "Enter Material Name"})
        self.fields["material_unit"].widget.attrs.update({"class": "form-select custom-input", "id": "id_material_unit"})
        self.fields["material_quantity"].widget.attrs.update({"class": "form-control custom-input", "placeholder": "Enter quantity"})
        self.fields["material_unitprice"].widget.attrs.update({"class": "form-control custom-input", "placeholder": "Enter Unit Price", "step": "0.01"})

        # default: none until category known
        self.fields["material_unit"].queryset = MaterialUnit.objects.none()

        if "material_category" in self.data:
            category = self.data.get("material_category")
            if category:
                self.fields["material_unit"].queryset = MaterialUnit.objects.filter(
                    category=category
                ).order_by("unit_name")

        elif self.instance and self.instance.pk:
            self.fields["material_unit"].queryset = MaterialUnit.objects.filter(
                category=self.instance.material_category
            ).order_by("unit_name")
from .models import Product, ProductCategory, ProductCollection

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_category', 'product_collection']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control custom-input',
            'placeholder': 'Enter Product Name',
        })
        self.fields['product_category'].choices = [('', 'Select Category')] + list(ProductCategory.choices)
        self.fields['product_category'].widget.attrs.update({
            'class': 'form-select custom-input',
        })
        self.fields['product_collection'].choices = [('', 'Select Collection')] + list(ProductCollection.choices)
        self.fields['product_collection'].widget.attrs.update({
            'class': 'form-select custom-input',
        })
