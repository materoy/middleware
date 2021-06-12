class Scholar():
    def __init__(self, scholar_data) -> None:
        self.name = ""
        self.field = ""
        self.achevement  = ""
        self.picture_url  =  ""
        self.get_scholar(scholar_data)

    def __str__(self) -> str:
        return self.name

    def get_scholar(self, data):
        self.name = data[1]
        self.field = data[2]
        self.achevement = data[0]
        self.picture_url = data[3]