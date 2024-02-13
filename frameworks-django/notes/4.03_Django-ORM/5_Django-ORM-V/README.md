# Django ORM V

## Django ORM Relationships:
Django provides a powerful Object-Relational Mapping (ORM) system that allows developers to create and interact with databases using Python classes and objects. When working with databases, relationships between tables are an essential aspect of the design. Django provides support for three types of relationships: one-to-one, one-to-many, and many-to-many.

### One-to-One Relationship:
In a one-to-one relationship, each record in the first table is associated with one and only one record in the second table. For example, consider a scenario where you have two tables, Employee and EmployeeProfile, where each employee has one EmployeeProfile. You can create a one-to-one relationship between the Employee and EmployeeProfile models in Django as follows:

    ```python
    class Employee(models.Model):
        name = models.CharField(max_length=50)

    class EmployeeProfile(models.Model):
        employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
        bio = models.TextField()
        location = models.CharField(max_length=50)
    ```

### One-to-Many Relationship:
In a one-to-many relationship, each record in the first table can be associated with multiple records in the second table. For example, consider a scenario where you have two tables, Author and Book, where each author can have multiple books. You can create a one-to-many relationship between the Author and Book models in Django as follows:

    ```python
    class Author(models.Model):
        name = models.CharField(max_length=50)

    class Book(models.Model):
        title = models.CharField(max_length=50)
        author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    ```

### Many-to-Many Relationship:
In a many-to-many relationship, each record in the first table can be associated with multiple records in the second table, and vice versa. For example, consider a scenario where you have two tables, Student and Course, where each student can take multiple courses, and each course can be taken by multiple students. You can create a many-to-many relationship between the Student and Course models in Django as follows:

    ```python
    class Student(models.Model):
        name = models.CharField(max_length=50)
        courses = models.ManyToManyField(Course)

    class Course(models.Model):
        name = models.CharField(max_length=50)
    ```

## QuerySet with queries involving relationships:
Django's QuerySet API allows you to write complex database queries using a simple and intuitive syntax. You can use the QuerySet API to retrieve records from the database that match certain criteria, filter records based on relationships, and perform aggregate operations.

For example, to retrieve all the books written by an author named "John Doe," you can use the following query:

    ```python
    books = Book.objects.filter(author__name='John Doe')
    ```

In this example, the double underscore notation ('__') is used to specify a lookup that involves a related model. The 'author__name' lookup means that we want to filter the Book records by the name of the author associated with each book.

## Related Manager:
In Django, a Related Manager is a manager object that allows you to interact with related objects. When you define a relationship between two models, Django automatically creates a related manager for the related model. The related manager allows you to retrieve, create, and update related objects.

For example, consider the one-to-many relationship between the Author and Book models we defined earlier. If you have an instance of the Author model, you can use the 'books' attribute to retrieve all the books written by that author:

    ```python
    author = Author.objects.get(name='John Doe')
    books = author.books.all()
    ```

In this example, the 'books' attribute is a Related Manager that allows you to retrieve all the books written by the author. You can also use the Related Manager to create new books and associate them with the author:

    ```python
    author = Author.objects.get(name='John Doe')
    book = Book.objects.create(title='New Book', author=author)
    ```

In this example, we create a new book with the title 'New Book' and associate it with the author using the 'author' attribute of the Book model. The 'author' attribute is a foreign key field that references the Author model, and it is used to establish the one-to-many relationship between the two models.

In summary, understanding how to model relationships using Django ORM, using QuerySet with queries involving relationships, and working with Related Managers is essential when building complex applications that require interaction with a database. By mastering these concepts, you can build powerful and efficient applications that can scale to handle large amounts of data.

