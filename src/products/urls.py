
from django.urls import path
from products.views import (ProductListView,product_list_view,ProductDetailsView,product_details_view,
                            ProductFeatureListView,ProductFeatureDetailsView,ProductSlugDetailsView )


urlpatterns = [

    path("",ProductListView.as_view() , name="list"),
    # path("products/<int:id>/",ProductDetailsView.as_view()),
    # path("feature/",ProductFeatureListView.as_view()),
    # path("feature/<int:pk>/",ProductFeatureDetailsView.as_view()),
    path("<slug:slug>/",ProductSlugDetailsView.as_view() , name="detail")


]

