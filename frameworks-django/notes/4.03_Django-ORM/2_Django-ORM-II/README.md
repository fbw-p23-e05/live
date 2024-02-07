# Django ORM II

## Identifying and using the Django ORM Model Manager:
The Model Manager is a class that provides an interface to the database for a particular model. It's responsible for creating, retrieving, updating, and deleting records in the database. By default, each model has a Model Manager assigned to it, which can be accessed using the `objects` attribute. Here's an example:

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
```

In this example, `Person.objects` is the Model Manager for the `Person` model.

## Creating database records using the Model Manager:
To create a new record in the database using the Model Manager, you can call the `create` method on the Manager instance. Here's an example:

```python
person = Person.objects.create(first_name='John', last_name='Doe', email='johndoe@example.com')
```

This code creates a new `Person` object and saves it to the database.

## Querying the database using the Model Manager and understanding QuerySet:
A QuerySet is a collection of database records that match a particular set of criteria. You can obtain a QuerySet by calling methods on the Model Manager. Here's an example:

```python
people = Person.objects.all()
```

This code retrieves all `Person` objects from the database.

## Using the `filter` method of a QuerySet:
The `filter` method is used to retrieve a subset of records from a QuerySet based on certain criteria. Here's an example:

```python
people = Person.objects.filter(last_name='Doe')
```

This code retrieves all `Person` objects from the database whose last name is 'Doe'.

## Deleting and updating records in the database:
To delete a record from the database, you can call the `delete` method on a model instance or a QuerySet. Here's an example:

```python
person = Person.objects.get(id=1)
person.delete()
```

This code deletes the `Person` object with ID 1 from the database.

To update a record in the database, you can modify the attributes of a model instance and then call the `save` method. Here's an example:

```python
person = Person.objects.get(id=1)
person.email = 'newemail@example.com'
person.save()
```

This code updates the email address of the `Person` object with ID 1 in the database.

