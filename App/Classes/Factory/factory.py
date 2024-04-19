from App.Constants.Cells.cells import EMPTY


class Factory:
    def __init__(self, img, button_img, width, height):
        self.img = img
        self.button_img = button_img

        self.width = width
        self.height = height

    def can_build(self, j, i, matrix):
        for row in range(j, j + self.width):
            for col in range(i, i + self.height):
                if matrix.matrix[row][col] != EMPTY:
                    return False
                
        return True