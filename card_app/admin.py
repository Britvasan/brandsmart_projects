from django.contrib import admin
from .models import MagazineTable, NewsTable, SlidesTable, SocialmediaTable, OthersTable

# Register your models here.

admin.site.register(MagazineTable)
admin.site.register(NewsTable)
admin.site.register(SlidesTable)
admin.site.register(SocialmediaTable)
admin.site.register(OthersTable)
