from django.contrib import admin
from django.urls import path
from books.views import main, author_list, book_list, author_detail, book_detail
# from book_details.views import recipe_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('author_list/',author_list, name='author_list' ),
    path('<int:author_id>/',author_detail, name='author_detail' ),
    path('book_list/',book_list, name='book_list' ),
    path('<int:book_id>/',book_detail, name='book_detail' ),
    # path('recipe_details', recipe_detail, name="recipe_details") 
]