from django.shortcuts import render

# Create your views here.
def taskList(request):
    return render(request, 'tasks/list.html')

def conteudo(request):
    return render(request, 'tasks/conteudo.html')