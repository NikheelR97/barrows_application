from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from .models import Client
from .forms import ClientForm

@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

@login_required
def save_client_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            clients = Client.objects.all()
            data['html_client_list'] = render_to_string('clients/includes/partial_client_list.html', {
                'clients': clients
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
    else:
        form = ClientForm()
    return save_client_form(request, form, 'clients/includes/partial_clients_create.html')

@login_required
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
    else:
        form = ClientForm(instance=client)
    return save_client_form(request, form, 'clients/includes/partial_clients_update.html')

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    data = dict()
    if request.method == 'POST':
        #client.delete()
        data['form_is_valid'] = True
        clients = Client.objects.all()
        data['html_client_list'] = render_to_string('clients/includes/partial_clients_list.html', {
            'clients': clients
        })
    else:
        context = {'clients': clients}
        data['html_form'] = render_to_string('clients/includes/partial_client_delete.html', context, request=request)
    return JsonResponse(data)
