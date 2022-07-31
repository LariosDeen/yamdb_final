from django.contrib import admin

from .models import User, Category, Genre, Title, GenreTitle, Review, Comment


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'username', 'is_superuser', 'role', 'confirmation_code',
        'password'
    )
    exclude = ('bio',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description', 'category')
    search_fields = ('name',)


class GenreTitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title_id', 'genre_id')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title_id', 'text', 'author', 'score', 'pub_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'text', 'author', 'pub_date')


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(GenreTitle, GenreTitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
