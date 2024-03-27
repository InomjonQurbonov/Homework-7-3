from django.forms import ModelForm
from django import forms
from .models import News, Members, Users


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']


class MembersForm(ModelForm):
    class Meta:
        model = Members
        fields = ['member_name', 'about_member', 'add_date', 'member_image']


class DeleteConfirmationForm(forms.Form):
    confirm_delete = forms.BooleanField(label='Confirm deletion', required=True)

