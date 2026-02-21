from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

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
    

