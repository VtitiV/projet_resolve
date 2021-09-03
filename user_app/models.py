from django.utils.translation import gettext as _

from django.db import models

class Utilisateurs (models.Model):

    Surname = models.CharField(_("nom"),max_length=255)
