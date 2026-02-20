from django.db import models
from django.core.validators import MinValueValidator

class RawMaterial(models.Model):
    material_name = models.CharField(max_length=50)
    
    material_category_choices = [
        ('', 'Choose category'),
        ('fabrics', 'Fabrics'),
        ('trims', 'Trims'),
        ('accessories', 'Accessories')
    ] 
    material_category = models.CharField(max_length=11, 
                                     choices=material_category_choices)
    
    material_quantity = models.PositiveIntegerField(default=0)

    material_unit_choices = {
        'fabrics': [('meter', 'Meter'), ('yard', 'Yard')],
        'trims': [('piece', 'Piece'), ('roll', 'Roll')],
        'accessories': [('pack', 'Pack'), ('set', 'Set')],
    }
    material_unit = models.CharField(max_length=20, blank=True)

    material_unitprice = models.FloatField(default=0, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.material_name

