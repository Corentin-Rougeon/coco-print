

class Frame():
    fields = []

    def __init__(self, title="", fields: list['Fields.field'] = [], width=10, height=0):
        self.title = title
        self.fields = fields
        self.width = width
        self.height = height
        self.__detect_size()


    def __detect_size(self):
        max_width = 0
        max_height = len(self.fields)
        for field in self.fields:
            if max_width < len(field.value):
                max_width = len(field.value)
        if max_width < len(self.title):
            max_width = len(self.title)

        if self.width < max_width:
            self.width = max_width

        if self.height < max_height:
            self.height = max_height


    def add_fields(self, fields: list['Fields.field']):
        for field in fields:
            self.fields.append(field)

        self.__detect_size()


    def __str__(self):

        str = f"┌{self.title:─^{self.width}}┐\n"

        for field in self.fields:
            if field.align == "CENTER":
                str += f"│{field.value:^{self.width}}│\n"
            elif field.align == "LEFT":
                str += f"│{field.value:<{self.width}}│\n"
            elif field.align == "RIGHT":
                str += f"│{field.value:>{self.width}}│\n"

        str += f"└{'─'*self.width}┘\n"

        return str

