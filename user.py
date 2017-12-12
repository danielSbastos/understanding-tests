class User():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return "%s %s, %s" % (self.first_name, self.last_name, self.age)

    def email(self):
        return "%s_%s@email.com" % (
            self.first_name.lower(), self.last_name.lower()
        )

    def username(self):
        return self.age + self.first_name.capitalize()
