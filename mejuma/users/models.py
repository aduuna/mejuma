from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CharField,
    BooleanField,
    IntegerField,
    TextField
)
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    location = CharField(_("Address"), blank=True, max_length=255)
    is_available = BooleanField(default=True)
    call_number = IntegerField(_("Default Call/SMS No."), blank=True, default=0)
    whatsapp_number = CharField("WhatsApp No.", max_length=14, blank=True)
    bio = TextField(_("Short Statement"), max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
