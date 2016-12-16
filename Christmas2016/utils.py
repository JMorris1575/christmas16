import random

from memory.models import Memory
from story.models import Branch

def get_memory():
    return random.choice(Memory.objects.all())

def create_branch(base_branch_key):
    sequence = Branch.objects.get(pk=base_branch_key).sequence
    new_branch = Branch(sequence=sequence)
    new_branch.save()


