from django.test import TestCase
from store.forms import AuthorForm, ContactForm, BookForm
from django import forms


class TestContactForm(TestCase):
    
    def test_message_field_widget(self):
        form = ContactForm()
        widget = form.fields['message'].widget
        self.assertIsInstance(widget, forms.Textarea)
        
    def test_phone_number_label(self):
        form = ContactForm()
        expected_label = form.fields['phone_number'].label
        self.assertEqual(expected_label, 'Phone number')
