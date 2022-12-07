from django.urls import path
from web.views import HomepageView, DetailView, ReviewView, SearchResultsView, OrderView, EmailView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('detail/<int:pk>/', DetailView.as_view(), name='products_detail_view'),
    path('review/<int:pk>/', ReviewView.as_view(), name='products_review_view'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search1/', EmailView.as_view(), name='search_results1'),
    path('create/<int:pk>/', OrderView.as_view(), name='order_create'),
]
