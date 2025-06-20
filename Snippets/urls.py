from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='snippets-add'),
    path('snippets/list', views.snippets_page, name='snippets-list'),
    path('snippets/my', views.my_snippets, name='my-snippets'),
    path('snippets/<int:snippet_id>', views.snippet_detail, name='snippet-detail'),
    path('snippets/<int:snippet_id>/delete', views.snippet_delete, name='snippet-delete'),
    path('snippets/<int:snippet_id>/edit', views.snippet_edit, name='snippet-edit'),
    path('snippets/search', views.snippet_search, name='snippet-search'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.create_user, name='register'),
    path('comment/add', views.create_comment, name="comment_add"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)