from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CodeForm
import clues.models as cModels

def index(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code'].lower()
            if cModels.Clue.objects.filter(codeword_1=code).exists():
                print('Code {} found.'.format(code))
                c = cModels.Clue.objects.get(codeword_1=code)
                redirect = c.view_1
                c.viewed_1 = True
                c.save()
                return HttpResponseRedirect('/clues/{}'.format(redirect))
            elif cModels.Clue.objects.filter(codeword_2=code).exists():
                print('Code {} found.'.format(code))
                c = cModels.Clue.objects.get(codeword_2=code)
                redirect = c.view_2
                c.viewed_2 = True
                c.save()
                return HttpResponseRedirect('/clues/{}'.format(redirect))
            else:
                print('Code {} not found.'.format(code))
                return HttpResponseRedirect('/clues/thanks')
    else:
        form = CodeForm()

    return render(request, 'index.html', {'form': form})

def landing(request, page):
    return render(request, '{}.html'.format(page))