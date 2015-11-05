from django.db import models
from django.utils.translation import ugettext_lazy as _


class TruncatingCharField(models.CharField):
    def get_prep_value(self, value):
        value = super(TruncatingCharField,self).get_prep_value(value)
        if value:
            return value[:self.max_length]
        return value


class LogEntry(models.Model):
    class Meta:
        verbose_name = _("Log entry")
        verbose_name_plural = _("Log entries")
        app_label = "admin_watchdog"

    when = models.DateTimeField(
        _("When"),
        auto_now_add=True,
        editable=False,
    )
    levelname = models.CharField(
        _("Level name"),
        max_length=20,
        editable=False,
    )
    shortmessage = TruncatingCharField(
        _("Short message"),
        max_length=256,
        editable=False,
    )
    message = models.TextField(
        _("Message"),
        editable=False,
    )
    request_repr = models.TextField(
        _("Request representation"),
        editable=False,
    )
