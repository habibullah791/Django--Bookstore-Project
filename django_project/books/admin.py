from django.contrib import admin

from .models import Book, Review


class ReviewLine(admin.TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewLine,
    ]
    list_display = (
        "title",
        "author",
        "price",
    )


admin.site.register(Book, BookAdmin)
