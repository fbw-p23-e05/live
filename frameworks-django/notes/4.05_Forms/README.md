# Django Forms

## Understanding Django Forms and its relationship to Views and Templates

Django Forms is a powerful tool that allows developers to create and handle HTML forms in a simple and effective way. A form can be defined as an interface between the user and the web application to collect data from the user. Django Forms provide a way to validate user input before sending it to the server. This helps to prevent common errors such as invalid data types, missing fields, and data that is outside of acceptable ranges.

Django Forms are typically used in conjunction with Views and Templates. The View is responsible for processing the user input and generating a response. The Template is responsible for rendering the HTML page that the user sees. Django Forms provides a convenient way to pass data between the View and the Template.

Example:
Let's create a simple form using Django Forms. Create a new Django app and add the following code to your `forms.py` file.

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

In this example, we have defined a form with three fields: `name`, `email`, and `message`. The `name` field is defined as a `CharField` with a maximum length of 100 characters. The `email` field is defined as an `EmailField`, which ensures that the user enters a valid email address. The `message` field is defined as a `CharField` with a `Textarea` widget, which provides a larger text input area.

To render this form in a template, we need to create a View. Create a new View in your `views.py` file and add the following code:

```python
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

In this example, we are using the `render` function to render a `contact.html` template and passing the `ContactForm` object to the template context.

Now, create a `contact.html` file in your templates directory and add the following code:

```django
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

In this example, we are rendering the form as a series of paragraphs using the `as_p` method. We are also including a CSRF token for security purposes.

When you visit the contact page in your browser, you should see a simple form with three fields: `name`, `email`, and `message`.

## Creating a Form from forms.Form and Rendering it in a Template

Creating a form using `forms.Form` in Django is a straightforward process. We create a new class that inherits from `forms.Form` and define the fields we want to include in the form as class attributes.

Example:
Let's create a new Django app and add the following code to your `forms.py` file.

```python
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
```

In this example, we have defined a `LoginForm` with two fields: `username` and `password`. The `username` field is defined as a `CharField` with a maximum length of 100 characters. The `password` field is defined as a `CharField` with a `PasswordInput` widget, which hides the password as it is being typed.

To render this form in a template, we need to create a View. Create a new View in your `views.py` file and add the following code:

```python
from django.shortcuts import render
from .forms import LoginForm

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})
```

In this example, we are using the `render` function to render a `login.html` template and passing the `LoginForm` object to the template context.

Now, create a `login.html` file in your templates directory and add the following code:

```django
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

In this example, we are rendering the form as a series of paragraphs using the `as_p` method. We are also including a CSRF token for security purposes.

When you visit the login page in your browser, you should see a simple form with two fields: `username` and `password`.

## Creating a Form from Models

Django Forms provides a convenient way to create a form based on a Django model. This allows us to easily create forms that are tied to our data models, reducing the amount of boilerplate code we need to write.

Example:
Let's create a new Django app and add the following code to your `models.py` file.

```python
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
```

In this example, we have defined a `Contact` model with three fields: `name`, `email`, and `message`.

Now, we can create a form based on this model by using Django's `ModelForm`. Create a new file `forms.py` in your app directory and add the following code:

```python
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
```

In this example, we are creating a `ContactForm` based on the `Contact` model. We specify which fields we want to include in the form using the `fields` attribute.

To render this form in a template, we need to create a View. Create a new View in your `views.py` file and add the following code:

```python
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

In this example, we are using the `render` function to render a `contact.html` template and passing the `ContactForm` object to the template context.

Now, create a `contact.html` file in your templates directory and add the following code:

```django
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

In this example, we are rendering the form as a series of paragraphs using the `as_p` method. We are also including a CSRF token for security purposes.

When you visit the contact page in your browser, you should see a simple form with three fields: `name`, `email`, and `message`.

## Rendering Forms in Templates and the Concept of Field Types and Widgets

Django Forms provides a wide variety of field types and widgets that can be used to collect different types of user input. Field types determine what type of data can be entered into a form field, while widgets control how the form field is displayed in the HTML.

Example:
Let's create a new Django app and add the following code to your `forms.py` file.

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    message = forms.CharField(label='Message', max_length=500, widget=forms.Textarea)
```

In the example above, we are defining a `ContactForm` class that inherits from `forms.Form`. We are then defining three fields: `name`, `email`, and `message`. The `CharField` and `EmailField` are field types that determine what type of data can be entered into the form fields. We are also using a `Textarea` widget for the `message` field, which controls how the field is displayed in the HTML.

To render this form in a template, we need to create a View. Create a new View in your `views.py` file and add the following code:

```python
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

In this example, we are using the `render` function to render a `contact.html` template and passing the `ContactForm` object to the template context.

Now, create a `contact.html` file in your templates directory and add the following code:

```django
<form method="post">
    {% csrf_token %}
    <div class="form-group">
        {{ form.name.label_tag }}
        {{ form.name }}
    </div>
    <div class="form-group">
        {{ form.email.label_tag }}
        {{ form.email }}
    </div>
    <div class="form-group">
        {{ form.message.label_tag }}
        {{ form.message }}
    </div>
    <button type="submit">Submit</button>
</form>
```

In this example, we are using the `label_tag` attribute to add labels to the form fields. We are also using Bootstrap classes to style the form fields. Note that we are rendering each form field separately, rather than using the `as_p` method.

When you visit the contact page in your browser, you should see a simple form with three fields: `name`, `email`, and `message`.

## Handling Data in a Form and Processing Received Data from a Form

When a user submits a form, Django automatically validates the data and puts it in a special data structure called `request.POST`. We can access the data in this structure and process it as needed.

Example:
Let's modify our `contact` view to handle form submissions. Modify your `views.py` file and add the following code:

```python
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Do something with the data
            return redirect('contact_thanks')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

In this example, we are checking if the request method is `POST`. If it is, we create a `ContactForm` object with the data in `request.POST`. We then check if the form is valid using the `is_valid` method. If the form is valid, we can access the data in the `form.cleaned_data` dictionary and process it as needed. We are then redirecting the user to a `contact_thanks` page.

If the request method is not `POST`, we create a new `ContactForm` object and pass it to the template context.

To create a `contact_thanks` page, create a new HTML template in your templates directory called `contact_thanks.html` and add the following code:

```django
<h1>Thank you for contacting us!</h1>
```

## Client-Side Data Validation in Forms Rendered in a Template

We can also perform client-side data validation using JavaScript. Client-side validation can provide instant feedback to the user and reduce the number of server requests.

Example:
Let's add client-side validation to our `ContactForm`. Modify your `contact.html` template and add the following code:

```django
<form method="post" id="contact-form">
    {% csrf_token %}
    <div class="form-group">
        {{ form.name.label_tag }}
        {{ form.name }}
        <div class="invalid-feedback"></div>
    </div>
    <div class="form-group">
        {{ form.email.label_tag }}
        {{ form.email }}
        <div class="invalid-feedback"></div>
    </div>
    <div class="form-group">
        {{ form.message.label_tag }}
        {{ form.message }}
        <div class="invalid-feedback"></div>
    </div>
    <button type="submit">Submit</button>
</form>

<script>
    var form = document.getElementById('contact-form');
    form.addEventListener('submit', function(event) {
        var name = document.getElementById('id_name');
        var email = document.getElementById('id_email');
        var message = document.getElementById('id_message');

        if (name.value.trim() === '') {
            name.classList.add('is-invalid');
            name.nextElementSibling.textContent = 'Name is required.';
            event.preventDefault();
        } else {
            name.classList.remove('is-invalid');
            name.nextElementSibling.textContent = '';
        }

        if (email.value.trim() === '') {
            email.classList.add('is-invalid');
            email.nextElementSibling.textContent = 'Email is required.';
            event.preventDefault();
        } else if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/i.test(email.value)) {
            email.classList.add('is-invalid');
            email.nextElementSibling.textContent = 'Invalid email address.';
            event.preventDefault();
        } else {
            email.classList.remove('is-invalid');
            email.nextElementSibling.textContent = '';
        }

        if (message.value.trim() === '') {
            message.classList.add('is-invalid');
            message.nextElementSibling.textContent = 'Message is required.';
            event.preventDefault();
        } else {
            message.classList.remove('is-invalid');
            message.nextElementSibling.textContent = '';
        }
    });
</script>
```

In this example, we are using JavaScript to listen for a `submit` event on the form. We are then accessing each form field by its ID and performing validation checks. If a field fails validation, we are adding the `is-invalid` class to the form group and displaying an error message in the `invalid-feedback` div. We are also preventing the form from submitting by calling the `preventDefault` method on the event object.

If all the fields pass validation, the form will be submitted normally.

Note that this is just one way to perform client-side validation. There are many libraries and frameworks available that can simplify this process.

## Handling Form Submission and Processing Received Data

After the form is submitted, the data needs to be processed on the server side. We can use Django's built-in form processing functions to handle form submission.

Example:
Let's modify our `views.py` file to handle form submission:

```python
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                'Contact Form Submission',
                'Name: {}\nEmail: {}\nMessage: {}'.format(name, email, message),
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            return render(request, 'contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
```

In this example, we are checking if the request method is `POST`. If it is, we create a new instance of our `ContactForm` and pass it the POST data. We then call the `is_valid` method on the form to check if the data is valid.

If the form data is valid, we can access the cleaned data using the `cleaned_data` attribute. In this example, we are using the `send_mail` function to send an email with the form data. We are also rendering a success template if the form submission is successful.

If the form data is invalid, we can simply return the form with errors to the user to correct the mistakes.

Note that in this example, we are using Django's built-in email sending function. In order to use this function, you need to configure your email settings in the `settings.py` file. You can also use a third-party email service or library to handle email sending.

## Conclusion:
Django forms provide a powerful way to handle user input in a web application. We can create forms using the `forms.Form` class or by linking a form to a model using the `forms.ModelForm` class. Forms can be rendered in templates using the `as_p`, `as_table`, or `as_ul` methods, and can be styled using CSS. We can also perform client-side validation using JavaScript. After the form is submitted, we can process the data on the server side using Django's built-in form processing functions.

