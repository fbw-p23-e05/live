# Django Views and Templates II

## What are Templates and their Objectives in a Django Project?

In Django, templates are the presentation layer of a web application. They are responsible for rendering HTML, CSS, and JavaScript code that are sent to the client's browser. Templates allow developers to separate the presentation logic from the business logic of a web application.

Templates serve several objectives in a Django project, such as:

1. Providing a consistent look and feel to the web application.
2. Enabling reusability of the presentation layer.
3. Making it easier to maintain and update the presentation layer.
4. Facilitating the creation of dynamic web pages.

Example:
Let's consider a simple example where we want to display a list of products on a web page. We could create an HTML file for the presentation layer, but that would be a static page. By using Django templates, we can create a dynamic page that can display different products based on the user's request. 

## Understanding the Relationship between Views and Templates and how Data is Shared between them via "Context"

In a Django project, views and templates work together to create the presentation layer of a web application. The view receives a request from the client, retrieves data from the database, processes it, and then passes the data to the template. The template, in turn, uses the data to create an HTML document that is returned to the client's browser.

The view passes data to the template using a context dictionary. The context is a dictionary of key-value pairs where the keys are the variable names used in the template, and the values are the data that will be displayed in the template.

Example:
Let's consider the same example from the previous topic, where we want to display a list of products on a web page. We would create a view that retrieves the list of products from the database and passes it to the template using a context dictionary. 

```python
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)
```

In the above code, we retrieve all the products from the database and store them in the `products` variable. We then create a context dictionary where the key is `products`, and the value is the `products` variable. Finally, we pass the context dictionary to the `render` function along with the name of the template file.

## How to Render the Template and Return it to the Client

To render a template and return it to the client, we use the `render` function provided by Django. The `render` function takes three arguments: the `request` object, the name of the template file, and the context dictionary.

Example:
Let's consider the same example from the previous topic. We have a view that retrieves the list of products from the database and passes it to the template using a context dictionary. Now, we need to render the template and return it to the client.

```python
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)
```

In the above code, we use the `render` function to render the `product_list.html` template and pass the `context` dictionary to it. The `render` function returns an `HttpResponse` object, which contains the HTML code of the template. This HTML code is sent to the client's browser as a response to the request.

## How to use the TemplateView Class to Create Template-based Views

The `TemplateView` class is a built-in class provided by Django that allows us to create views based on templates

To use the `TemplateView` class, we need to define a new class that inherits from it and specifies the template name. The `TemplateView` class takes care of rendering the template and passing the context to it.

Example:
Let's consider the same example of displaying a list of products. We can create a `ProductListView` class that inherits from `TemplateView` and specify the name of the template file.

```python
from django.views.generic import TemplateView
from .models import Product

class ProductListView(TemplateView):
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context
```

In the above code, we create a new class `ProductListView` that inherits from `TemplateView` and specifies the name of the template file as `product_list.html`. We also override the `get_context_data` method to pass the context dictionary to the template. The `get_context_data` method retrieves all the products from the database and adds them to the context dictionary.

## How to create Templates using Tags and Interpolation

In Django templates, we can use tags and interpolation to create dynamic content. Tags are special keywords that perform specific actions, while interpolation allows us to insert variables into the template.

Example:
Let's consider an example where we want to display the details of a product on a web page. We can use tags and interpolation to create a dynamic page.

```django
<h1>{{ product.name }}</h1>
<p>{{ product.description }}</p>
<p>Price: ${{ product.price }}</p>
```

In the above code, we use interpolation to display the name, description, and price of the product. The double curly braces (`{{ }}`) indicate that we are inserting a variable into the template. We also use tags to format the output. 

## How to use `for` and `if` Tags in a Template

In Django templates, we can use `for` and `if` tags to create loops and conditional statements.

Example:
Let's consider an example where we want to display a list of products on a web page. We can use a `for` loop to iterate over the list of products and display their details.

```django
{% for product in products %}
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
{% endfor %}
```

In the above code, we use a `for` loop to iterate over the list of products and display their name, description, and price. We use the `endfor` tag to indicate the end of the loop.

We can also use an `if` statement to display only certain products that meet a condition.

```django
{% for product in products %}
    {% if product.price > 50 %}
        <h1>{{ product.name }}</h1>
        <p>{{ product.description }}</p>
        <p>Price: ${{ product.price }}</p>
    {% endif %}
{% endfor %}
```

In the above code, we use an `if` statement to display only the products whose price is greater than 50. We use the `endif` tag to indicate the end of the statement.

## How to use Template Filters

Template filters are functions that can be used to modify the output of a variable in a template.

Example:
Let's consider an example where we want to display the date a product was added to the database. We can use the `date` filter to format the date.

```django
<p>Added on: {{ product.date_added|date:"F j, Y" }}</p>
```

In the above code, we use the `date` filter to format the `date_added` field of the `product` object. The `date` filter takes a string argument that specifies the date format. In this case, we use the `"F j, Y"` format, which displays the date in the format of `Month Day, Year`.

We can also chain multiple filters together to modify the output even further.

```django
<p>Price: ${{ product.price|floatformat:2|add:"-5.00" }}</p>
```

In the above code, we use the `floatformat` filter to round the `price` field of the `product` object to two decimal places, and then we use the `add` filter to subtract 5.00 from the result.

## How to create Custom Template Tags and Filters

We can create custom template tags and filters to extend the functionality of Django templates.

Example:
Let's consider an example where we want to create a custom template tag to display the average rating of a product. We can define a custom template tag in a separate Python module.

```python
from django import template
from django.db.models import Avg
from ..models import Rating

register = template.Library()

@register.simple_tag(takes_context=True)
def average_rating(context, product_id):
    rating = Rating.objects.filter(product_id=product_id).aggregate(Avg('value'))['value__avg']
    return round(rating, 1) if rating else None
```

In the above code, we define a new function called `average_rating` that takes the `product_id` as an argument. The function retrieves all the ratings for the given product and calculates their average. The `register` object is a `template.Library` instance that we use to register our custom tag.

To use the custom tag in a template, we need to load the tag library first.

```django
{% load mytags %}
<p>Average Rating: {% average_rating product.id %}</p>
```

In the above code, we load the `mytags` tag library that contains the `average_rating` tag. We pass the `product.id` as an argument to the tag to retrieve the average rating for the product.

Similarly, we can define custom template filters using the `@register.filter` decorator. The process is similar to defining custom tags, and we can use them in the templates by loading the filter library first.

```python
@register.filter
def currency(value):
    return '${:,.2f}'.format(value)
```

In the above code, we define a `currency` filter that takes a value and formats it as a currency string. We can use the filter in a template by loading the filter library and applying the filter to a variable.

```django
{% load myfilters %}
<p>Price: {{ product.price|currency }}</p>
```

## How to use TemplateView class to create template-based views

Django provides a class-based view called `TemplateView` that makes it easy to create views that render templates. 

Example:

Let's consider an example where we want to create a view that renders a template called `home.html`.

```python
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
```

In the above code, we define a new class called `HomeView` that inherits from `TemplateView`. We set the `template_name` attribute to the name of the template that we want to render.

To use the `HomeView` class in a URL pattern, we need to map it to a URL.

```python
from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
```

In the above code, we create a URL pattern that maps the root URL to the `HomeView` class. We use the `as_view()` method to convert the class into a callable view function.

## How to create templates using Tags and interpolation

Django templates support a variety of tags and interpolation techniques that allow us to create dynamic HTML pages.

Example:

Let's consider an example where we want to create a template that displays a list of products.

```django
<ul>
{% for product in products %}
    <li>
        <a href="{% url 'product_detail' product.id %}">{{ product.name }}</a>
        <p>Price: ${{ product.price }}</p>
    </li>
{% empty %}
    <li>No products found.</li>
{% endfor %}
</ul>
```

In the above code, we use the `for` tag to iterate over the `products` list and generate an HTML list. We use the `url` tag to generate a URL for each product that links to the product detail page. We use the `{{ product.name }}` and `{{ product.price }}` notation for interpolation to display the name and price of each product.

The `empty` block is executed when the `products` list is empty. It displays a message indicating that no products were found.

## How to use `for` and `if` tags in a template

We can use the `for` and `if` tags in a template to control the flow of execution and display data conditionally.

Example:

Let's consider an example where we want to create a template that displays the products in a category and highlights the products that are on sale.

```django
<h1>{{ category.name }}</h1>
{% for product in products %}
    <div class="product{% if product.on_sale %} on-sale{% endif %}">
        <a href="{% url 'product_detail' product.id %}">
            <img src="{{ product.image.url }}" alt="{{ product.name }}">
        </a>
        <p>{{ product.name }}</p>
        {% if product.on_sale %}
            <p class="price sale">${{ product.price }} ({{ product.discount }}% off)</p>
        {% else %}
            <p class="price">${{ product.price }}</p>
        {% endif %}
    </div>
{% empty %}
    <p>No products found.</p>
{% endfor %}
```

In the above code, we use the `for` tag to iterate over the `products` list and generate a product display block. We use the `if` tag to conditionally apply the `on-sale` class to the product display block and to display the sale price and discount for products that are on sale.

The `empty` block is executed when the `products` list is empty. It displays a message indicating that no products

## How to use template filters

Django provides a set of built-in filters that allow us to transform and format data in a template.

Example:

Let's consider an example where we want to create a template that displays a date in a specific format.

```django
<p>Published on {{ post.pub_date|date:'F j, Y' }}</p>
```

In the above code, we use the `date` filter to format the `pub_date` attribute of the `post` object. The `date` filter takes a format string as an argument. In this case, we use the `F j, Y` format, which produces a string like "January 1, 2022".

We can also chain filters together to perform multiple transformations on a value.

Example:

Let's consider an example where we want to create a template that displays the first few words of a post excerpt.

```django
<p>{{ post.excerpt|truncatewords:30|linebreaksbr }}</p>
```

In the above code, we use the `truncatewords` filter to limit the `excerpt` attribute of the `post` object to the first 30 words. We then use the `linebreaksbr` filter to replace line breaks with HTML line break tags. The resulting HTML is displayed in a paragraph tag.

## How to create custom template tags and filters

Django allows us to define our own custom template tags and filters to extend the functionality of the template system.

Example:

Let's consider an example where we want to create a custom filter that formats a number as a currency amount.

```python
from django import template
from django.utils import formats

register = template.Library()

@register.filter
def currency(value):
    return formats.currency(value)
```

In the above code, we define a new filter called `currency` that uses the `formats.currency()` function to format a number as a currency amount. We register the filter with the template system using the `register.filter` decorator.

To use the `currency` filter in a template, we simply apply it to a numeric value.

```django
<p>Price: {{ product.price|currency }}</p>
```

In the above code, we use the `currency` filter to format the `price` attribute of the `product` object as a currency amount.

Example:

Let's consider an example where we want to create a custom tag that displays a random quote.

```python
import random
from django import template

register = template.Library()

QUOTES = [
    "The best way to predict the future is to invent it.",
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "If you want to go fast, go alone. If you want to go far, go together.",
]

@register.simple_tag
def random_quote():
    return random.choice(QUOTES)
```

In the above code, we define a new tag called `random_quote` that uses the `random.choice()` function to select a random quote from a list of quotes. We register the tag with the template system using the `register.simple_tag` decorator.

To use the `random_quote` tag in a template, we call it like any other function.

```django
<blockquote>
    <p>{{ random_quote }}</p>
</blockquote>
```

In the above code, we use the `random_quote` tag to display a random quote in a blockquote element. The tag generates the quote text dynamically each time the template is rendered.

Custom tags and filters can be very powerful tools for extending the functionality of the Django template system. However, they should be used judiciously to avoid overly complex or difficult-to-maintain templates.


## Best practices for using templates in a Django project

When working with templates in a Django project, there are several best practices that can help ensure clean, maintainable, and efficient code.

1. Use template inheritance: Template inheritance allows us to create a base template that defines the overall structure of a page, and then define child templates that inherit from the base template and add or override content as necessary. This approach can help reduce redundancy and make it easier to maintain a consistent look and feel across an entire site.

2. Use context variables sparingly: Context variables are used to pass data from a view to a template. While they can be useful for providing dynamic content, they should be used sparingly to avoid cluttering the template with too much logic. Instead, consider defining custom template tags and filters or using inheritance to factor out common logic.

3. Keep templates simple: Templates should be focused on presentation logic, and should not contain complex business logic or database queries. If a template requires a lot of data processing, consider moving the logic into the view or creating a custom template tag or filter.

4. Cache templates and static assets: Caching can help reduce the load on the server and improve performance for frequently accessed pages. Consider using Django's built-in caching framework to cache templates and static assets like images, stylesheets, and JavaScript files.

5. Use debugging tools: When debugging a template, it can be helpful to use Django's built-in template debugging tools. These tools can help identify errors and provide more detailed information about the rendering process.

By following these best practices, you can create clean, efficient, and maintainable templates for your Django project.

