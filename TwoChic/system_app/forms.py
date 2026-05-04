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
        self.fields["material_quantity"].widget.attrs.update({"class": "form-control custom-input", "placeholder": "Enter quantity", "onfocus": "if(this.value=='0')this.value=''", "onkeydown": "return event.key !== 'e' && event.key !== 'E' && event.key !== '+' && event.key !== '-'"})
        self.fields["material_unitprice"].widget.attrs.update({"class": "form-control custom-input", "placeholder": "Enter Unit Price", "step": "0.01", "onfocus": "if(this.value=='0')this.value=''", "onkeydown": "return event.key !== 'e' && event.key !== 'E' && event.key !== '+' && event.key !== '-'"})
        self.fields["minimum_threshold"].widget.attrs.update({"class": "form-control custom-input", "placeholder": "Enter minimum threshold", "step": "0.01", "onfocus": "if(this.value=='0')this.value=''", "onkeydown": "return event.key !== 'e' && event.key !== 'E' && event.key !== '+' && event.key !== '-'"})

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

    def clean_material_name(self):
        name = self.cleaned_data.get('material_name', '').strip()
        if not name:
            raise forms.ValidationError("Material name cannot be empty.")
        if len(name) < 2:
            raise forms.ValidationError("Material name must be at least 2 characters.")
        if not all(c.isalpha() or c.isspace() or c in "-_()./'" for c in name):
            raise forms.ValidationError("Invalid material name. Only letters and special characters (- _ ( ) . / ') are allowed.")
        qs = RawMaterial.objects.filter(material_name__iexact=name)
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A material with this name already exists.")
        return name

    def clean_material_quantity(self):
        qty = self.cleaned_data.get('material_quantity')
        if qty is None or qty == '':
            raise forms.ValidationError("Quantity cannot be blank.")
        if qty < 0:
            raise forms.ValidationError("Quantity cannot be negative.")
        return qty

    def clean_material_unitprice(self):
        price = self.cleaned_data.get('material_unitprice')
        if price is None or price == '':
            raise forms.ValidationError("Unit price cannot be blank.")
        if price < 0:
            raise forms.ValidationError("Unit price cannot be negative.")
        return price

    def clean_minimum_threshold(self):
        threshold = self.cleaned_data.get('minimum_threshold')
        if threshold is None or threshold == '':
            raise forms.ValidationError("Minimum threshold cannot be blank.")
        if threshold < 0:
            raise forms.ValidationError("Minimum threshold cannot be negative.")
        return threshold

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('material_category')
        unit = cleaned_data.get('material_unit')

        if not category:
            raise forms.ValidationError("Please select a category.")
        if not unit:
            raise forms.ValidationError("Please select a unit.")
        return cleaned_data

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

    def clean_product_name(self):
        name = self.cleaned_data.get('product_name', '').strip()
        if not name:
            raise forms.ValidationError("Product name cannot be empty.")
        qs = Product.objects.filter(product_name__iexact=name)
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A product with this name already exists.")
        return name


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

    def clean_employee_name(self):
        name = self.cleaned_data.get('employee_name', '').strip()
        if not name:
            raise forms.ValidationError("Employee name cannot be empty.")
        if len(name) < 2:
            raise forms.ValidationError("Employee name must be at least 2 characters.")
        if not all(c.isalpha() or c.isspace() or c in ".-'" for c in name):
            raise forms.ValidationError("Employee name can only contain letters, spaces, hyphens, periods, and apostrophes.")
        role = self.data.get('employee_role')
        if role and Employee.objects.filter(employee_name__iexact=name, employee_role=role).exists():
            raise forms.ValidationError("An employee with this name already exists in this role.")
        return name


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