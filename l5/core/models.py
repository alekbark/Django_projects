from django.db import models
from django.core.exceptions import ValidationError

# валидатор по заданию из HW7
def validate_positive(value):
    if value < 0:
        raise ValidationError('Только положительные числа или 0')

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[validate_positive]) # применили валидатор HW7

    # метод по заданию из HW7 (1)
    def get_info(self):
        return f'{self.id} - {self.name}'

    def __str__(self):
        return self.name

class Employee(Person):
    hire_date = models.DateField()

    def __str__(self):
        return f'{self.name} (Employee)'

class Manager(Employee):
    EDUCATION_CHOICES = [
        ('sc', 'Среднее'),
        ('sp', 'Среднее специальное'),
        ('he', 'Высшее')
    ]

    education = models.CharField(
        max_length=2,
        choices=EDUCATION_CHOICES,
        default='he'
    )

    grade = models.IntegerField(
        validators=[validate_positive],
        default=1
    )

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[validate_positive]) # применили валидатор HW7
    favorite_icecream = models.ForeignKey('IceCream', on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey(Person, on_delete=models.CASCADE) # связь по заданию из HW6

    # метод по заданию из HW7 (1)
    def get_info(self):
        return f'{self.id} - {self.name}'

    # метод по заданию из HW7 (1)
    def age_plus_parent(self):
        return self.age + self.parent.age # сумма значений (возрастов) из HW7

    def __str__(self):
        return self.name

class IceCream(models.Model):
    name = models.CharField(max_length=100)
    recommended_price = models.IntegerField(validators=[validate_positive]) # применили валидатор HW7
    created_at = models.DateTimeField(auto_now_add=True, null=True) # это поле не отображается в forms HW25

    # создаем поле со списком для HW9
    ICECREAM_KINDS = [
        ('ge', 'Gelato'),
        ('fc', 'Frozen Custard'),
        ('ss', 'Soft Serve'),
        ('fy', 'Frozen Yogurt'),
        ('sh', 'Sherbet'),
        ('ri', 'Rolled Ice Cream')
    ]
    kind = models.CharField(max_length=2, choices=ICECREAM_KINDS, default='ss')

    # обновил метод отображения для HW9 с помощью get_<имя_поля>_display()
    # для методов с choises (со списком для выбора)
    def __str__(self):
        return f'{self.name} ({self.get_kind_display()})'

class Kiosk(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    icecreams = models.ManyToManyField( # связь по заданию из HW6
        IceCream,
        through='KioskIceCream'         # many-to-many через through-model для HW29
    )

    def __str__(self):
        return self.name

class KioskIceCream(models.Model):
    kiosk = models.ForeignKey(Kiosk, on_delete=models.CASCADE)
    icecream = models.ForeignKey(IceCream, on_delete=models.CASCADE)

    purchase_price = models.DecimalField(max_digits=5, decimal_places=2)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2)

    quantity = models.IntegerField(default=0)

    is_available = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.kiosk} - {self.icecream}'