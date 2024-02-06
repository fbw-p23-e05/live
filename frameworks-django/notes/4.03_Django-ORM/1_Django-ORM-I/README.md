# Django ORM I

## What is ORM?
ORM stands for Object-Relational Mapping. It's a technique of mapping data between a relational database and an object-oriented programming language. With ORM, you can interact with a database by using object-oriented programming constructs like classes, objects, and methods instead of writing raw SQL queries.

ORM solves many problems, including:
- Minimizing the amount of code you need to write to interact with a database.
- Improving code readability and maintainability by using object-oriented programming concepts.
- Automatically mapping database tables to classes, and database columns to class attributes.

## Pros and Cons of using ORM:
Pros:
- Simplifies the process of writing database queries.
- Helps in reducing the amount of boilerplate code required to interact with a database.
- Increases code readability by using object-oriented programming concepts.
- Abstracts away the low-level details of database interaction.

Cons:
- Can be slower than writing raw SQL queries.
- Can sometimes generate suboptimal SQL queries.
- Requires an understanding of the ORM framework.

## Basics of the Django ORM framework:
Django is a popular web development framework that provides a powerful ORM system. The Django ORM provides an intuitive and easy-to-use API for querying the database. Here's an example:

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
```

This example defines a Person model, with three fields: first_name, last_name, and email. The `__str__` method is used to display a human-readable representation of the model.

## Writing simple Django ORM models and synchronizing them with a PostgreSQL database:
To write a simple Django ORM model, you need to create a new Django app using the command `python manage.py startapp <app_name>`. Then, you can define your models in the `models.py` file inside the app directory.

Once you've defined your models, you can synchronize them with a PostgreSQL database by running the command `python manage.py makemigrations <app_name>`, followed by `python manage.py migrate`.

## Converting existing tables in a database to Django ORM Models:
If you have an existing database and want to use Django ORM to interact with it, you can create Django models that correspond to the database tables. You can do this by defining a Django model for each table, and specifying the table name using the `Meta` class. Here's an example:

```python
from django.db import models

class Person(models.Model):
    class Meta:
        db_table = 'person'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
```

In this example, we're defining a Person model that corresponds to a `person` table in the database.

## Using `sqlmigrate` command to see SQL code for migrations:
Django's migration system allows you to generate SQL code to apply or reverse migrations. You can use the `sqlmigrate` command to see the SQL code for a specific migration. Here's an example:

```
python manage.py sqlmigrate app_name migration_name
```

This command will display the SQL code for the specified migration.

