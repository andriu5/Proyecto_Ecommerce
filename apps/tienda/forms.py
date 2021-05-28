from django import forms
from apps.productos.models import Producto
from .models import Orden
from .models import OrdenProducto,Direccion
from django.contrib.auth import get_user_model

User = get_user_model()

class AddressForm(forms.Form):
    shipping_address_line_1 = forms.CharField(required=False)
    shipping_address_line_2 = forms.CharField(required=False)
    shipping_zip_code = forms.CharField(required=False)
    shipping_city = forms.CharField(required=False)

    billing_address_line_1 = forms.CharField(required=False)
    billing_address_line_2 = forms.CharField(required=False)
    billing_zip_code = forms.CharField(required=False)
    billing_city = forms.CharField(required=False)

    selected_shipping_address = forms.ModelChoiceField(
        Direccion.objects.none(), required=False
    )

    selected_billing_address = forms.ModelChoiceField(
        Direccion.objects.none(), required=False
    )
    

    # def __init__(self, *args, **kwargs):
    #     user_id = kwargs.pop('user_id')
    #     super().__init__(*args, **kwargs)

    #     user = User.objects.get(id=user_id)

    #     shipping_address_qs = Direccion.objects.filter(
    #         user=user,
    #         address_type='S'
    #     )

    #     billing_address_qs = Direccion.objects.filter(
    #         user=user,
    #         address_type='B'
    #     )

    #     self.fields['selected_shipping_address'].queryset = shipping_address_qs
    #     self.fields['selected_billing_address'].queryset = billing_address_qs


    # def clean(self):
    #     data = self.cleaned_data

    #     selected_shipping_address = data.get('selected_shipping_address', None)
    #     if selected_shipping_address is None:
    #         if not data.get('shipping_address_line_1', None):
    #             self.add_error("shipping_address_line_1", "Please fill in this field")
    #         if not data.get('shipping_address_line_2', None):
    #             self.add_error("shipping_address_line_2", "Please fill in this field")
    #         if not data.get('shipping_zip_code', None):
    #             self.add_error("shipping_zip_code", "Please fill in this field")
    #         if not data.get('shipping_city', None):
    #             self.add_error("shipping_city", "Please fill in this field")

    #     selected_billing_address = data.get('selected_billing_address', None)
    #     if selected_billing_address is None:
    #         if not data.get('billing_address_line_1', None):
    #             self.add_error("billing_address_line_1", "Please fill in this field")
    #         if not data.get('billing_address_line_2', None):
    #             self.add_error("billing_address_line_2", "Please fill in this field")
    #         if not data.get('billing_zip_code', None):
    #             self.add_error("billing_zip_code", "Please fill in this field")
    #         if not data.get('billing_city', None):
    #             self.add_error("billing_city", "Please fill in this field")

class AddToCartForm(forms.ModelForm):
    # password = forms.CharField(widget = forms.TextInput(attrs={"type": "hidden"}))

    cantidad = forms.IntegerField(min_value=1,required=False, label="Añadir al Carro")
    # cantidad.widget = forms.IntegerField(
    #     attrs= {
    #         "class":"form-control"
    #     }
    # )
    class Meta:
        model = OrdenProducto
        # creo que por ahora solo podriamos usar la cantidad para el carro!
        fields = ['cantidad']

    # def __init__(self, *args, **kwargs):
    #     self.product_id = kwargs.pop('producto_id')
    #     producto = Producto.objects.get(id=self.producto_id)
    #     super().__init__(*args, **kwargs)

    # def clean(self):
    #     product_id = self.product_id
    #     producto = Producto.objects.get(id=self.product_id)
    #     cantidad = self.cleaned_data['cantidad']

    #     if producto.inventario < cantidad:
    #         raise forms.ValidationError(f"The maximum stock is {producto.inventario}")



# class AddressForm(forms.Form):
    
#     shipping_address_line_1 = forms.CharField(required=False)
#     shipping_address_line_2 = forms.CharField(required=False)
#     shipping_zip_code = forms.CharField(required=False)
#     shipping_city = forms.CharField(required=False)

#     billing_address_line_1 = forms.CharField(required=False)
#     billing_address_line_2 = forms.CharField(required=False)
#     billing_zip_code = forms.CharField(required=False)
#     billing_city = forms.CharField(required=False)

#     selected_shipping_address = forms.ModelChoiceField(
#         Direccion.objects.none(), required=False
#     )

#     selected_billing_address = forms.ModelChoiceField(
#         Direccion.objects.none(), required=False
#     )

#     def __init__(self, *args, **kwargs):
#         user_id = kwargs.pop('user_id')
#         super().__init__(*args, **kwargs)

#         user = User.objects.get(id=user_id)

#         shipping_address_qs = Direccion.objects.filter(
#             user=user,
#             address_type='S'
#         )

#         billing_address_qs = Direccion.objects.filter(
#             user=user,
#             address_type='B'
#         )

#         self.fields['selected_shipping_address'].queryset = shipping_address_qs
#         self.fields['selected_billing_address'].queryset = billing_address_qs


#     def clean(self):
#         data = self.cleaned_data

#         selected_shipping_address = data.get('selected_shipping_address', None)
#         if selected_shipping_address is None:
#             if not data.get('shipping_address_line_1', None):
#                 self.add_error("shipping_address_line_1", "Please fill in this field")
#             if not data.get('shipping_address_line_2', None):
#                 self.add_error("shipping_address_line_2", "Please fill in this field")
#             if not data.get('shipping_zip_code', None):
#                 self.add_error("shipping_zip_code", "Please fill in this field")
#             if not data.get('shipping_city', None):
#                 self.add_error("shipping_city", "Please fill in this field")

#         selected_billing_address = data.get('selected_billing_address', None)
#         if selected_billing_address is None:
#             if not data.get('billing_address_line_1', None):
#                 self.add_error("billing_address_line_1", "Please fill in this field")
#             if not data.get('billing_address_line_2', None):
#                 self.add_error("billing_address_line_2", "Please fill in this field")
#             if not data.get('billing_zip_code', None):
#                 self.add_error("billing_zip_code", "Please fill in this field")
#             if not data.get('billing_city', None):
#                 self.add_error("billing_city", "Please fill in this field")
