from dao.products_dao import ProductDao
from model.products_model import Product


class ProductController:
    dao = ProductDao()

    def get_by_id(self, id):
        return self.dao.get_by_id(id)

    def get_by_name(self, product: Product):
        return self.dao.get_by_name(product)

    def get_by_description(self, product: Product):
        return self.dao.get_by_description(product)

    def get_by_value(self, product: Product):
        return self.dao.get_by_value(product)

    def get_by_categories(self):
        return self.dao.get_by_categories()

    def create(self, product: Product):
        return self.dao.create(product)

    def update(self, product: Product, id):
        return self.dao.update(product, id)

    def delete(self, id):
        return self.dao.delete(id)
