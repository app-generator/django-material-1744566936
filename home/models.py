# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Project(models.Model):

    #__Project_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Project_FIELDS__END

    class Meta:
        verbose_name        = _("Project")
        verbose_name_plural = _("Project")


class Sysreqtype(models.Model):

    #__Sysreqtype_FIELDS__
    type = models.CharField(max_length=255, null=True, blank=True)

    #__Sysreqtype_FIELDS__END

    class Meta:
        verbose_name        = _("Sysreqtype")
        verbose_name_plural = _("Sysreqtype")


class Sysreq(models.Model):

    #__Sysreq_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(SysReqType, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    #__Sysreq_FIELDS__END

    class Meta:
        verbose_name        = _("Sysreq")
        verbose_name_plural = _("Sysreq")



#__MODELS__END
