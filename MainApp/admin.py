from django.contrib import admin
from MainApp.models import Snippet, Comment

# Register your models here.
# 1 variant
# admin.site.register([Snippet, Comment])

# 2 variant

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ["author", "text"]
    readonly_fields = ["creation_date", "text"]
    can_delete = False
    max_num = 1
    extra = 1
    show_change_link = True

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ["name", "lang", "creation_date", "public", "code"]
    list_filter = ["lang", "creation_date"]
    ordering = ["creation_date"]
    search_fields = ["name", "code"]
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["text"]
    search_fields = ["text"]