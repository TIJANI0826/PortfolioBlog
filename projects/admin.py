from django.contrib import admin


from projects.models import Projects

class ProjectsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Projects, ProjectsAdmin)
