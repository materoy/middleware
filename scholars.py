class Scholars():
    def __init__(self, name, field, achievement, picture_url) -> None:
        self.name = name
        self.field = field
        self.achevement = achievement
        self.picture_url = picture_url

    def __str__(self) -> str:
        return self.name

    def get_scholar(self, data):
        self.name = data[1]
        self.field = data[2]
        self.achevement = data[0]
        self.picture_url = data[3]