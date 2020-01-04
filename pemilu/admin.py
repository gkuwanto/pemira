from django.contrib import admin
from .models import Vote, Password, Candidate

# Register your models here.
admin.site.register(Vote)
admin.site.register(Password)
admin.site.register(Candidate)
