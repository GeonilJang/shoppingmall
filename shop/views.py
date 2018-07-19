from django.shortcuts import render
from django.views.generic import ListView
from .models import Item
# Create your views here

#
# def index(request):
#     pass


class ItemListView(ListView):
    model = Item
    paginate_by = 8
    queryset = Item.objects.filter(is_public=True)
    leng = int(len(queryset)/8)+1

    def get_queryset(self):
        self.q = self.request.GET.get('q','')

        qs = super().get_queryset()
        if self.q:
            qs = qs.filter(name__icontains = self.q)
        return qs

    def get_context_data(self, **kwards):
        context = super().get_context_data(**kwards)
        context['q']= self.q
        context['leg']= self.leng
        return context

index = ItemListView.as_view()
