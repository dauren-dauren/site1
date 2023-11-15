from .models import Post
from django.forms import ModelForm, TextInput, NumberInput, BooleanField
from random import randint

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['recipient', 'order', 'left','country','city', 'code']

		widgets = {
			"recipient": TextInput(attrs ={
				"class" : "from-control",
				"placeholder" : "Заказ для"
			}),

			"order": TextInput(attrs ={
				"class" : "from-control",
				"placeholder" : "Товар"
			}),

			"left": TextInput(attrs ={
				"class" : "from-control",
				"placeholder" : "Покинул страну"
			}),

			"country": TextInput(attrs ={
				"class" : "from-control",
				"placeholder" : "Страна прибытия"
			}),

			"city": TextInput(attrs ={
				"class" : "from-control",
				"placeholder" : "Город прибытия"
			}),
			"code": NumberInput(attrs ={
				"class" : "from-control",
				"placeholder" : "Код товара",
				"value" : randint(111111, 999999)
			}),
		}
class EditForm(ModelForm):
	class Meta:
		model = Post
		fields = ['left_boolean', 'country_boolean', 'city_boolean','delivered_boolean']

		widgets = {

			"left_boolean": BooleanField(),

			"country_boolean": BooleanField(),

			"city_boolean": BooleanField(),

			"delivered_boolean": BooleanField(),
		}
