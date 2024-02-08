
from shop.models import Product


def create_product(n, p, q, c):
    return Product.objects.create(name=n, price=p, quantity=q, condition=c)


# p = Product.objects.create(name='Keyboard', price=22.22, quantity=10, condition='Used')

# create_product('Monitor', 444.44, 3, 'New')
# create_product('Mouse', 11.11, 30, 'Used')
# create_product('iPad', 555.55, 20, 'New')
# create_product('Bike', 7777.77, 2, 'Used')



### Field Lookups in Querying

# <Field_name>__<Lookup_key> = <Lookup_value>

# range(20, 300)
# q = Product.objects.filter(name__icontains = 'tor')

# q = Product.objects.filter(name__in = ['iPad', 'Keyboard', 'Laptop'])

# q = Product.objects.filter(price__range = (20,500), name='Headphone')


# print(q.values())


### Complex Conditional Statements using QuerySet


# q = Product.objects.filter(Q(name='Monitorrrr') | Q(price=444.44))


# q = Product.objects.filter(~Q(name='Headphone'))


# print(q.values())


### Chaining QuerySets


# q = Product.objects.filter(~Q(name='Headphone')).filter(condition='New').filter(price__gte=1000)

# q2 = q.filter(name='Bike').......



# print(q2.values())

# & | ~


### Object Annotation in Django ORM


from django.db.models import Q, Value, F, FloatField, ExpressionWrapper, IntegerField, Count, DecimalField


# q = Product.objects.filter(price__gte=1000).annotate(description=Value('Discout 30%'))

q = Product.objects.annotate(total_price = ExpressionWrapper((F('price') * F('quantity')), output_field=IntegerField()))

from django.db.models.functions import Cast, Round

q = Product.objects.annotate(total_price = Round(ExpressionWrapper((F('price') * F('quantity')), output_field=FloatField()),2))

q = Product.objects.annotate(total_price = Round(Cast(F('price') * F('quantity'), FloatField()),2))


print(q.values())


### Aggregation, Counting, and Ordering using QuerySets

# q = Product.objects.filter(name='Bike').annotate(amount=Count('name'))

# q = Product.objects.values('name')

# q2 = q.annotate(amount=Count('name')).order_by('-quantity')

# q = Product.objects.values('quantity').order_by('quantity')

# q2 = q.annotate(amount=Count('name'))

# print(q.values())

