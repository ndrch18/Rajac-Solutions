from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Account(models.Model):
    employee_id = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

class MaterialCategory(models.TextChoices):
    FABRICS = 'fabrics', 'Fabrics'
    TRIMS = 'trims', 'Trims'
    ACCESSORIES = 'accessories', 'Accessories'

class MaterialUnit(models.Model):
    unit_name = models.CharField(max_length=20)
    category = models.CharField(
        max_length=15,
        choices=MaterialCategory.choices
    )

    def __str__(self):
        return f"{self.unit_name} ({self.category})"

class RawMaterial(models.Model):
    material_name = models.CharField(max_length=50)

    material_category = models.CharField(
        max_length=15,
        choices=MaterialCategory.choices
    )

    material_unit = models.ForeignKey(
        MaterialUnit,
        on_delete=models.PROTECT
    )

    material_quantity = models.PositiveIntegerField(default=0)

    material_unitprice = models.FloatField(
        default=0,
        validators=[MinValueValidator(0.0)]
    )

    def clean(self):
        if self.material_unit.category != self.material_category:
            raise ValidationError("Selected unit does not match material category.")
    
    def __str__(self):
        return self.material_name
    
class EmployeeRole(models.TextChoices):
    PRODUCTION_MANAGER = 'production_manager', 'Production Manager'
    PRODUCTION_EMPLOYEE = 'production_employee', 'Production Employee'

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True, editable=False)
    employee_name = models.CharField(max_length=100)
    employee_role = models.CharField(
        max_length=30,
        choices=EmployeeRole.choices,
    )

    def __str__(self):
        return f"{self.employee_id} – {self.employee_name}"

class ProductCategory(models.TextChoices):
    TOPS = 'tops', 'Tops'
    BOTTOMS = 'bottoms', 'Bottoms'
    DRESSES = 'dresses', 'Dresses'
    OUTERWEAR = 'outerwear', 'Outerwear'
    SETS = 'sets', 'Sets'

class ProductCollection(models.TextChoices):
    SUMMER = 'summer', 'Summer'
    RESORT = 'resort', 'Resort'
    HOLIDAY = 'holiday', 'Holiday'
    SPRING = 'spring', 'Spring'
    FALL = 'fall', 'Fall'

class Product(models.Model):
    product_id = models.CharField(max_length=10, unique=True, editable=False)
    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=20, choices=ProductCategory.choices)
    product_collection = models.CharField(max_length=20, choices=ProductCollection.choices)

    def save(self, *args, **kwargs):
        if not self.product_id:
            last = Product.objects.order_by('-id').first()
            next_num = (last.id + 1) if last else 1
            self.product_id = f'#{next_num:05d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_id} – {self.product_name}"

