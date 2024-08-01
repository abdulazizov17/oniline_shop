from django import forms
from online_shop.models import Comment,Order
class CommentModelForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'

class OrderModelForm(forms.ModelForm):

    class Meta:
        model = Order
        fields='__all__'