from django.contrib import admin

# Register your models here.




from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_filter = ("title",)
    list_display = ("title", "ingredients",)
    prepopulated_fields = {"slug" : ("title",)}

admin.site.register(Recipe, RecipeAdmin)
