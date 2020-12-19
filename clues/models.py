from django.db import models

class Clue(models.Model):
    codeword_1 = models.CharField(max_length=255, default=None, null=True)
    codeword_2 = models.CharField(max_length=255, default=None, null=True)
    viewed_1 = models.BooleanField(default=False, null=True)
    viewed_2 = models.BooleanField(default=False, null=True)
    is_view = models.BooleanField(default=None, null=True)
    view_1 = models.CharField(max_length=255, default=None, null=True)
    view_2 = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return 'Codeword 1: {}  Codeword 2: {} '.format(self.codeword_1, self.codeword_2)