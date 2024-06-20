from django.urls import path
from .views import ProductViewSets, CategoryViewSets, CommentViewSets

urlpatterns = [
    path('', ProductViewSets.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', ProductViewSets.as_view({'get': 'retrieve',
                                               'put': 'update', 'delete': 'destroy'}), name='product_detail'),

    path('category/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve',
                                               'put': 'update', 'delete': 'destroy'}), name='category_detail'),

    path('comment/', CommentViewSets.as_view({'get': 'list', 'post': 'create'}), name='comment_list'),
    path('comment/<int:pk>/', CommentViewSets.as_view({'get': 'retrieve',
                                               'put': 'update', 'delete': 'destroy'}), name='comment_detail'),

]