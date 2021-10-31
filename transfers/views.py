from django.views import generic
from .models import *


class HomeView(generic.ListView):
    template_name = "transfers/home.html"
    context_object_name = 'home'
    model = Staff

#search on the home page
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = self.model.objects.filter(name__contains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class StaffView(generic.DetailView):
    model = Staff
    template_name = "transfers/staff.html"
    context_object_name = 'staff'


class TransfersView(generic.ListView):
    model = TransferHistory
    template_name = "transfers/staff.html"
    context_object_name = 'transfers'

    def get_queryset(self):
        pk = self.kwargs['staff_id']
        return TransferHistory.objects.filter(id=pk)