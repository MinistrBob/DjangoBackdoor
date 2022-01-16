from django.db import models


class Ssh(models.Model):
    """Ssh connections"""
    ip = models.CharField("IP address", max_length=15, default='')
    hostname = models.CharField("Hostname", max_length=32, default='')
    username = models.CharField("Username", max_length=32, default='')
    password = models.CharField("Password", max_length=32, default='')
    description = models.CharField("Description", max_length=250, default='')

    def __str__(self):
        return f"{self.ip}({self.username})"

    class Meta:
        verbose_name = "SSH connection"
        verbose_name_plural = "SSH connections"
