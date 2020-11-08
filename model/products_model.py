from model.categories_model import Category


class Product:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.description = ''
        self.value = 0
        self.categories = Category()

    def __str__(self):
        return f'{self.id};{self.name};{self.description};{self.value};{self.categories}'
