from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import PermissionDenied

from story.models import Story, Branch
from user.models import UserProfile
from user.decorators import class_login_required

import utils


@class_login_required
class StoryDisplay(View):
    template_name = 'story/story_display.html'

    def get(self, request, branch_number=None):
        try:
            branch = Branch.objects.get(branch_number=branch_number)
        except:
            raise PermissionDenied
        entry_list = branch.as_list()
        entries = Story.objects.filter(pk__in=entry_list)

        return render(request, self.template_name,
                      { 'display_memory': utils.get_memory,
                        'all_branches': Branch.objects.all(),
                        'entries': entries,})


@class_login_required
class StoryAdd(View):
    template_name = 'story/story_add.html'

    def get(self, request, branch_number=None, previous=None):
        return render(request, self.template_name,
                      { 'display_memory': utils.get_memory})

    def post(self, request):
        return redirect('story_check')


@class_login_required
class StoryCheck(View):
    template_name = 'story/story_check.html'

    def get(self, request, branch_number=None, previous=None):
        return render(request, self.template_name,
                      {'branch_number': branch_number,
                       'previous': previous,
                       'display_memory': utils.get_memory})

    def post(self, request, entry_number=None):
        # make changes in database if this is the right user
        return redirect('story_display')