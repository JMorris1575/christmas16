from django.db import models
from django.conf import settings

from model_mixins import AuthorMixin as AuthorMixin


class StoryLine(models.Model, AuthorMixin):
    entry = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    previous_entry = models.IntegerField()

    def __str__(self):
        if len(self.entry) > 80:
            return self.entry[0:79] + '...'
        else:
            return self.entry

    def display(self):
        return self.entry

    def get_author(self):
        return self.author_name(self.author)


class Branch(models.Model):
    branch_number = models.IntegerField(unique=True, default=1)
    sequence = models.TextField()

    def __str__(self):
        return self.sequence

    def as_list(self):
        str_list = self.sequence.split()
        num_list = []
        for num_str in str_list:
            num_list.append(int(num_str))
        return num_list

    def check_entry(self, previous):
        if self.as_list()[-1] == previous:
            return True
        else:
            return False

