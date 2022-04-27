from django.contrib.auth import authenticate
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from crm.accounts.models import Profile
from crm.web.forms import CreateCustomerForm, CreateContractForm, EditCustomerForm, CreateOfferForm, EditOfferForm, \
    CreateTaskForm, EditTaskForm, DeleteTaskForm
from crm.web.models import Customers, Contracts, Offers, Tasks


class HomeView(views.TemplateView):
    template_name = 'web/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # context['hide_additional_nav_items'] = True
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('show dashboard')
        return redirect('login user')


def show_dashboard(request):
    contracts = Contracts.objects.all()
    offers = Offers.objects.all()
    tasks = Tasks.objects.all()

    user_contacts = []
    for contract in contracts:
        if contract.contract_owner_id == request.user.pk:
            user_contacts.append(contract)
    contracts_count = len(user_contacts)
    contact_value_sum = 0
    contract_quantity_sum = 0

    for contract in user_contacts:
        contact_value_sum += int(contract.annual_consumption) * float(contract.price)
        contract_quantity_sum += int(contract.annual_consumption)
    if not contract_quantity_sum == 0:
        average_price = contact_value_sum / contract_quantity_sum
    else:
        average_price = '-'

    meetings = []
    calls = []
    user_tasks = []
    for task in tasks:
        if task.task_owner_id == request.user.pk:
            user_tasks.append(task)
    for task in user_tasks:
        if task.task_type == 'Meeting':
            meetings.append(task)
        elif task.task_type == 'Call':
            calls.append(task)
    meetings_count = len(meetings)
    calls_count = len(calls)
    user_offers = []
    for offer in offers:
        if offer.offer_owner_id == request.user.pk:
            user_offers.append(offer)
    offers_count = len(user_offers)
    offered_quantity = 0
    offers_value = 0
    for offer in user_offers:
        offered_quantity += int(offer.offered_quantity)
        offers_value += int(offer.offered_quantity) * float(offer.offer_price)
    if not offered_quantity == 0:
        average_offering_price = offers_value / offered_quantity
    else:
        average_offering_price = '-'
    context = {
        'contracts_count': contracts_count,
        'average_price': average_price,
        'meetings_count': meetings_count,
        'calls_count': calls_count,
        'offers_count': offers_count,
        'average_offering_price': average_offering_price,
        'offered_quantity': offered_quantity,

    }
    return render(request, 'web/dashboard.html', context)


class CreateCustomerView(views.CreateView):
    form_class = CreateCustomerForm
    template_name = 'web/customer-create.html'
    success_url = reverse_lazy('show dashboard')


def customers_details(request):
    if request.user.has_perm('web.view_customers'):
        account_customers = []
        customers = Customers.objects.all()
        for customer in customers:
            if customer.account_owner_id == request.user.pk:
                account_customers.append(customer)

        account_contracts = []
        contracts = Contracts.objects.all()
        for contract in contracts:
            if contract.contract_owner_id == request.user.pk:
                account_contracts.append(contract)

        context = {
            'account_customers': account_customers,
            'account_contracts': account_contracts,
        }
        return render(request, 'web/customers_details.html', context)
    return redirect('show dashboard')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


def customer_details(request, pk):
    customer = Customers.objects.get(pk=pk)
    context = {
        'customer': customer
    }
    return render(request, 'web/customer-details.html', context)


def edit_customer(request, pk):
    if request.user.has_perm('web.change_customers'):
        customer = Customers.objects.get(pk=pk)
        if request.method == 'POST':
            form = EditCustomerForm(request.POST, instance=customer)
            if form.is_valid():
                customer.save()
                return redirect('show dashboard')
        form = EditCustomerForm(instance=customer)
        context = {
            'form': form,
            'customer': customer,
        }

        return render(request, "web/customer-edit.html", context)
    return redirect('show dashboard')


class CreateContractView(views.CreateView):
    form_class = CreateContractForm
    success_url = reverse_lazy('show dashboard')
    template_name = 'web/contract-create.html'


def contracts_details(request):
    if request.user.has_perm('web.view_contracts'):
        account_customers = []
        customers = Customers.objects.all()
        for customer in customers:
            if customer.account_owner_id == request.user.pk:
                account_customers.append(customer)

        account_contracts = []
        contracts = Contracts.objects.all()
        for contract in contracts:
            if contract.contract_owner_id == request.user.pk:
                account_contracts.append(contract)

        context = {
            'account_customers': account_customers,
            'account_contracts': account_contracts,
        }
        return render(request, 'web/contracts_details.html', context)
    return redirect('show dashboard')


class CreateOfferView(views.CreateView):
    form_class = CreateOfferForm
    template_name = 'web/offer-create.html'
    success_url = reverse_lazy('show dashboard')


def edit_offer(request, pk):
    if request.user.has_perm('web.change_offers'):
        offer = Offers.objects.get(pk=pk)
        if request.method == "POST":
            form = EditOfferForm(request.POST, instance=offer)
            if form.is_valid():
                form.save()
                return redirect("show dashboard")

        form = EditOfferForm(instance=offer)
        context = {
            'form': form,
            'offer': offer,
        }
        return render(request, 'web/offer-edit.html', context)
    return redirect('show dashboard')


def offers_details(request):
    if request.user.has_perm('web.view_offers'):
        account_customers = []
        customers = Customers.objects.all()
        for customer in customers:
            if customer.account_owner_id == request.user.pk:
                account_customers.append(customer)

        account_offers = []
        offers = Offers.objects.all()
        for offer in offers:
            if offer.offer_owner.pk == request.user.id:
                account_offers.append(offer)

        context = {
            'account_customers': account_customers,
            'account_offers': account_offers,
        }
        return render(request, 'web/offers-details.html', context)
    return redirect('show dashboard')


class CreateTaskView(views.CreateView):
    form_class = CreateTaskForm
    template_name = 'web/task-create.html'
    success_url = reverse_lazy('show dashboard')


def tasks_details(request):
    if request.user.has_perm("web.view_tasks"):
        account_customers = []
        customers = Customers.objects.all()
        for customer in customers:
            if customer.account_owner_id == request.user.pk:
                account_customers.append(customer)

        account_tasks = []
        tasks = Tasks.objects.all()
        for task in tasks:
            if task.task_owner.pk == request.user.id:
                account_tasks.append(task)

        context = {
            'account_customers': account_customers,
            'account_tasks': account_tasks,
        }
        return render(request, 'web/tasks-details.html', context)
    return redirect('show dashboard')

def edit_task(request, pk):
    if request.user.has_perm('web.change_tasks'):
        task = Tasks.objects.get(pk=pk)
        if request.method == "POST":
            form = EditTaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("show dashboard")

        form = EditTaskForm(instance=task)
        context = {
            'form': form,
            'task': task,
        }
        return render(request, 'web/task-edit.html', context)
    return redirect('show dashboard')


def delete_task(request, pk):
    if request.user.has_perm('web.delete_tasks'):
        task = Tasks.objects.get(pk=pk)
        if request.method == "POST":
            form = DeleteTaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("show dashboard")

        form = DeleteTaskForm(instance=task)
        context = {
            'form': form,
            'task': task,
        }
        return render(request, 'web/task-delete.html', context)
    return redirect('show dashboard')
