from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView ,DetailView
from django.http import Http404
# Create your views here.
from . models import Product
from carts.models import Cart


class ProductFeatureListView(ListView):
    #queryset = Product.objects.featured()
    template_name = "products/list.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.featured()


class ProductFeatureDetailsView(DetailView):
    #queryset = Product.objects.featured()
    template_name = "products/detail.html"

   
    
    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.featured()

class ProductSlugDetailsView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"
    
    def get_context_data(self,*args,**kwargs):
        context = super(ProductSlugDetailsView,self).get_context_data(*args,**kwargs)
        cart_obj , new_obj = Cart.objects.new_or_get(self.request)
        context['cart']= cart_obj
        print("context",context)
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get("slug")
        #instance =  Product.objects.filter(slug=slug)
        try:
            instance = Product.objects.get(slug=slug,active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Product Not6 FOund")
        return instance
    

      


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all()

def product_list_view(request):
    queryset  = Product.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request,"products/list.html",context)

class ProductDetailsView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    # def get_context_data(self,*args,**kwargs):
    #     context = super(ProductDetailsView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context
    
    def get_object(self,*args,**kwargs):
        request = self.request
        id = self.kwargs.get("id")
        instance =  Product.objects.get_by_id(id)
        print("insinstance" , instance)
        if instance is None:
            raise Http404("Product does not exists");
        return instance
        


def product_details_view(request,id=None,*args,**kwargs):
    #queryset  = Product.objects.get(id=id)
    #queryset = get_object_or_404(Product,id=id)
    # try:
    #     queryset  = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     print("no product found")
    #     raise Http404("Product does not exist")
    # except:
    #     print("Error")
    #qs = Product.objects.filter(id=id)
    instance = Product.objects.get_by_id(id)
    if instance is None:
        raise Http404("Product Not Found")
    # print("qssssss" , qs)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product does not exist")
    

    context = {
        "object" : instance
    }
    return render(request,"products/detail.html",context)