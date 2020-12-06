import user


class Employees(user.User):

    def __init__(self, acceptedWork, username, password, name, gender, address, phone):
        super.__init__(username, password, name, gender, address)
        self.acceptedWork = acceptedWork
