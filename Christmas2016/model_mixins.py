class AuthorMixin():

    def author_name(self, user):
        name = user.first_name
        if name == 'Brian':
            name += ' ' + user.last_name
        return name

