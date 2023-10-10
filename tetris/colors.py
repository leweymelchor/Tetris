class Colors:
    dark_grey = (42, 47, 79)
    green = (158, 179, 132)
    red = (255, 135, 135)
    orange = (255, 133, 81)
    yellow = (246, 186, 111)
    purple = (77, 60, 119)
    cyan = (155, 205, 210)
    blue = (150, 182, 197)

    dark_blue = (145, 127, 179)
    light_blue = (229, 190, 236)
    white = (253, 226, 243)
    black = (0, 0, 0)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange,
                 cls.yellow, cls.purple, cls.cyan, cls.blue]
