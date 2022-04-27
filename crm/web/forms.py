from django import forms

from crm.web.models import Customers, CUSTOMER_NAME_MAX_LEN, EIC_MAX_LEN, Contracts, Offers, Tasks


class CreateCustomerForm(forms.ModelForm):
    customer_name = forms.CharField(
        max_length=CUSTOMER_NAME_MAX_LEN,
    )
    eic = forms.CharField(
        max_length=EIC_MAX_LEN,
    )
    representative_first_name = forms.CharField(
        max_length=Customers.REPR_FIRST_NAME_MAX_LEN,
    )
    representative_last_name = forms.CharField(
        max_length=Customers.REPR_LAST_NAME_MAX_LEN,
    )
    address = forms.TextInput()
    email = forms.EmailField()
    mobile = forms.CharField(
        max_length=Customers.MOBILE_MAX_LEN,
    )
    description = forms.TextInput()

    class Meta:
        model = Customers
        fields = '__all__'


class CreateContractForm(forms.ModelForm):
    contract_date = forms.DateField()
    annual_consumption = forms.IntegerField()
    price = forms.FloatField()
    contract_expiration = forms.DateField()

    class Meta:
        model = Contracts
        fields = ('customer', 'contract_date', 'contract_expiration', 'annual_consumption', 'price', 'contract_owner')


class EditCustomerForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.save()
            return self.instance

    class Meta:
        model = Customers
        fields = '__all__'


class CreateOfferForm(forms.ModelForm):
    offered_quantity = forms.IntegerField()
    offer_price = forms.FloatField()
    offer_validity = forms.DateField()

    class Meta:
        model = Offers
        fields = ('customer', 'offer_owner', 'offered_quantity', 'offer_price', 'offer_validity',)


class EditOfferForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.save()
            return self.instance

    class Meta:
        model = Offers
        fields = ('offer_validity', 'offered_quantity', 'offer_price',)


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'


class EditTaskForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.save()
            return self.instance

    class Meta:
        model = Tasks
        fields = '__all__'


class DeleteTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance

    class Meta:
        model = Tasks
        fields = '__all__'
