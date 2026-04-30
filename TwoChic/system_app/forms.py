from django import forms
from .models import RawMaterial, MaterialUnit, MaterialCategory, Product, ProductCategory, ProductCollection, Employee, EmployeeRole

class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = [
            "material_category",
            "material_name",
            "material_unit",
            "material_quantity",
            "material_unitprice",
            "minimum_threshold",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["material_category"].choices = [("", "Choose Category")] + list(MaterialCategory.choices)

        self.fields["material_category"].widget.attrs.update({"class": "form-select custom-input", "id": "id_material_category"})
        self.fields["material_name"].widget.attrs.update({"class": "form-control custom-input", "placeholder": "Enter Material Name"})
        self.fields["material_unit"].widget.attrs.update({"class": "form-select custom-input", "id": "id_material_unit"})
        self.fields["material_quantity"].widget.attrs.update({"class": "form-control custom-input", "placeholder": "Enter quantity", "onfocus": "if(this.value=='0')this.value=''"})
        self.fields["material_unitprice"].widget.attrs.update({"class": "form-control custom-input", "placeholder": "Enter Unit Price", "step": "0.01", "onfocus": "if(this.value=='0')this.value=''"})
        self.fields["minimum_threshold"].widget.attrs.update({"class": "form-control custom-input", "placeholder": "Enter minimum threshold", "step": "0.01", "onfocus": "if(this.value=='0')this.value=''"})

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


class AddEmployeeForm(forms.Form):
    employee_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control custom-input',
            'placeholder': 'Enter Employee Name',
        })
    )
    employee_role = forms.ChoiceField(
        choices=[('', 'Select Role')] + list(EmployeeRole.choices),
        widget=forms.Select(attrs={
            'class': 'form-select custom-input',
        })
    )

class EditEmployeeNameForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee_name'].widget.attrs.update({
            'class': 'form-control custom-input',
            'placeholder': 'Enter Employee Name',
        })
