from django.urls import path

from crm.web.views import HomeView, CreateCustomerView, CreateContractView, \
    customers_details, contracts_details, customer_details, edit_customer, CreateOfferView, edit_offer, offers_details, \
    CreateTaskView, tasks_details, edit_task, delete_task, show_dashboard

urlpatterns = (
    path('', HomeView.as_view(), name='show home'),

    path('dashboard/', show_dashboard, name='show dashboard'),

    path('create-customer/', CreateCustomerView.as_view(), name='create customer'),
    path('customers/details', customers_details, name='customers details'),
    path('customer/details/<pk>', customer_details, name='customer details'),
    path('edit-customer/<pk>', edit_customer, name='edit customer'),

    path('create-contract/', CreateContractView.as_view(), name='create contract'),
    path('contract/details/', contracts_details, name='contracts details'),

    path('offer/create/', CreateOfferView.as_view(), name='create offer'),
    path('offers/details', offers_details, name='offers details'),
    path('offer/edit/<pk>', edit_offer, name='edit offer'),

    path('task/create/', CreateTaskView.as_view(), name='create task'),
    path('task/edit/<pk>', edit_task, name='edit task'),
    path('task/delete/<pk>', delete_task, name='delete task'),
    path('tasks/details/', tasks_details, name='tasks details'),


)
