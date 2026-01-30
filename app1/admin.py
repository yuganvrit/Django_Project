from django.contrib import admin
from .models import Student,Author,Book

# Register your models here.

admin.site.register(Student)
admin.site.register(Author)
admin.site.register(Book)


#modify the color of admin panel from default to black
admin.site.site_header = "SkillShikshya Admin Panel"
admin.site.site_title = "SkillShikshya Admin Portal"
admin.site.index_title = "Welcome to SkillShikshya Admin Panel"
admin.site.site_url = None  # Disable the "View Site" link
admin.site.enable_nav_sidebar = False  # Disable the sidebar navigation

# To change the admin panel theme to dark mode, we can override the admin CSS.


