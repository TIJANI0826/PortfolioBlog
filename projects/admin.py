from django.contrib import admin


from projects.models import Projects,Participant

class ProjectsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Participant)