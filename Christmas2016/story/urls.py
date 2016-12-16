from django.conf.urls import url
from django.urls import reverse
from .views import (StoryDisplay, StoryAdd, StoryCheck)
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(
        url='story/1/display')),
    url(r'^(?P<branch_number>[0-9]+)/display/$',
        StoryDisplay.as_view(), name='display_story' ),
    url(r'^(?P<branch_number>[0-9]+)/add/(?P<previous>[0-9]+)/$',
        StoryAdd.as_view(), name='story_add'),
    url(r'^(?P<branch_number>[0-9]+)/check/(?P<previous>[0-9]+)/$',
        StoryCheck.as_view(), name='story_check'),
]
