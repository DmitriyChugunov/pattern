from django.shortcuts import render

from .forms import RegisterForm


def RegisterView(request):
    form = RegisterForm()
    return render(request, 'pattern/form.html', context={'form': form})
def ContactsView(request):
    contacts = {
        'number': 79803328307,
        'VK': 'Дмитрий Чугунов, https://vk.com/crazyangelo4ek',
        'Telegram': 'Дмитрий Чугунов, @JluTui',
        'address': 'г.Брянск ул.Новозыбковская д.16 кв.15'
    }
    return render(request, 'pattern/contacts.html', {'contacts': contacts})


def IndexView(request):
    form = RegisterForm()
    return render(request, 'pattern/index.html', context={'form': form})


def AboutView(request):
    return render(request, 'pattern/about.html')
