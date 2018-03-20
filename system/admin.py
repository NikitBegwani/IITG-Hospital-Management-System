from django.contrib import admin

from .models import Medicine, CRequest,Registration,Post, Doctor,AmbulanceBooking,AmbulanceSchedule, Reception,Patient, Prescription, FollowUp, Complaint

admin.site.register(Medicine)
admin.site.register(CRequest)
admin.site.register(Doctor)
admin.site.register(Reception)
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(AmbulanceBooking)
admin.site.register(AmbulanceSchedule)
admin.site.register(Post)
admin.site.register(Registration)
admin.site.register(FollowUp)
admin.site.register(Complaint)


# Register your models here.
