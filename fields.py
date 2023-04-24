
class field():
    def __str__(self):
        return f"<field object align={self.align}  value={self.value}>"

    def __init__(self,value: str,align:str="LEFT"):
        align = align.upper()
        self.value = value
        if align in ["LEFT","RIGHT","CENTER"]:
            self.align = align
        else:
            raise TypeError("Invalid alignment, only 'LEFT' , 'RIGHT' or 'CENTER' allowed (not case sensitive)")

@staticmethod
def concat_fields(arr, align="LEFT"):
    fields = []
    for str in arr:
        fields.append(field(str,align))
    return fields




