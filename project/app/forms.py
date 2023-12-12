from django import forms


class RegisterForm(forms.Form):
    fio = forms.CharField(min_length=3, label='ФИО')
    email = forms.EmailField(label='Email')
    mg = forms.ChoiceField(choices=((1,'Мужской'), (2, 'Женский')))

