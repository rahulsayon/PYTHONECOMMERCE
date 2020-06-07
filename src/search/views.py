from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.views.generic import ListView
from products.models import Product

class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self,*args,**kwargs):
        context = super(SearchProductView,self).get_context_data(*args,**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        #SearchQuery.objects.create(query=query)
        return context


    def get_queryset(self,*args,**kwargs):
        request = self.request
        #return Product.objects.filter(title__icontains='Mi')
        print(request.GET)
        method_dict = request.GET
        query = method_dict.get('q',None)
        print(query)
        if query is not None:
            # lookups = Q(title__icontains=query ) | Q(description__icontains=query)
            return Product.objects.search(query)
            #return Product.objects.filter(title__iexact=query)
        return Product.objects.featured()
        '''
            __icontains = fields contain this
            __iexact =  fields is exactly this
        '''