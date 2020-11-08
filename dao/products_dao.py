import MySQLdb
from model.product_model import Product


class ProductDao:
    connection = MySQLdb.connect(host='localhost', database='testetsp', user='root', passwd='')
    cursor = connection.cursor()

    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM products WHERE id={id}")
        return self.cursor.fetchone()

    def get_by_name(self, product: Product):
        self.cursor.execute(f"SELECT * FROM products WHERE name like '{product}%'")
        return self.cursor.fetchall()

    def get_by_description(self, product: Product):
        self.cursor.execute(f"SELECT * FROM products WHERE description like '{product}%'")
        return self.cursor.fetchall()

    def get_by_value(self, product: Product):
        self.cursor.execute(f"SELECT * FROM products WHERE value like '{product}%'")
        return self.cursor.fetchall()

    def get_by_categories(self):
        self.cursor.execute('SELECT * FROM products AS p INNER JOIN categories AS c ON p.categories = c.id')
        return self.cursor.fetchall()

    def create(self, product: Product):
        self.cursor.execute(f"INSERT into products (NAME,DESCRIPTION,VALUE,CATEGORIES) VALUES ('{product.name}',"
                            f"'{product.description}','{product.value}','{product.categories}')")
        self.connection.commit()
        return self.cursor.lastrowid

    def update(self, product: Product, id):
        self.cursor.execute(f"UPDATE products SET NAME='{product.name}',DESCRIPTION='{product.description}',"
                            f"VALUE={product.value},CATEGORIES='{product.categories}' WHERE ID={id}")
        return self.connection.commit()

    def delete(self, id):
        self.cursor.execute(f'DELETE FROM products WHERE ID={id}')
        return self.connection.commit()
