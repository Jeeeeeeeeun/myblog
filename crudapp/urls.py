from django.urls import path
from . import views

urlpatterns = [
    path('show/<int:post_id>', views.show, name='show'),
    path('new', views.new, name='new'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('edit', views.edit, name='edit'),
    path('postupdate/<int:post_id>', views.postupdate, name='postupdate'),
    path('postdelete/<int:post_id>', views.postdelete, name='postdelete'),
    path('scrap/<int:post_id>', views.scrap, name='scrap'),
    path('like/<int:post_id>', views.like, name='like'),

]