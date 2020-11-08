import sys
from controller.products_controller import ProductController
from model.products_model import Product

sys.path.append('D:/Marcela/teste')


def menu():
    print('***********************************')
    print('* 1 - Get products by name        *')
    print('* 2 - Get products by description *')
    print('* 3 - Get products by value       *')
    print('* 4 - Get products by category    *')
    print('* 5 - Register a new product      *')
    print('* 6 - Update a product            *')
    print('* 7 - Delete a product            *')
    print('***********************************')
    return int(input('Select an option: '))


controller = ProductController()
product = Product()
op = menu()

if op == 1:
    print('Get products by name')
    name = str(input('Write the product name: '))
    print(controller.get_by_name(name))

elif op == 2:
    print('Get products by description')
    description = str(input('Write the product description: '))
    print(controller.get_by_description(description))

elif op == 3:
    print('Get products by value')
    value = float(input('Write the product value: '))
    print(controller.get_by_value(value))

elif op == 4:
    print('Get products by category')
    category = int(input('Write the product category: '))
    print(controller.get_by_categories())

elif op == 5:
    print('Register a new product')
    product.name = str(input('Write the name of the product: '))
    product.description = str(input('Write the description of the product: '))
    product.value = float(input('Write the value of the product: '))
    product.categories = int(input('Write the category of the product: '))

    saved_categories = controller.get_by_categories()
    saved_id = controller.create(product)
    print(controller.get_by_id(saved_id))

elif op == 6:
    print('Update a product')
    id = int(input('Write the id of the product that you want to update:'))
    saved_id = controller.get_by_id(id)
    print(saved_id)

    product.name = str(input('Write the name of the product: '))
    product.description = str(input('Write the description of the product: '))
    product.value = float(input('Write the value of the product: '))
    product.categories = int(input('Write the category of the product: '))

    controller.update(product, id)
    saved_id = controller.get_by_id(id)
    print(saved_id)

elif op == 7:
    print('Delete a product')
    id = int(input('Write the id of the product that you want to delete: '))
    print(controller.get_by_id(id))
    controller.delete(id)
    print('Register deleted')
    print(controller.get_by_categories())

else:
    print("This option don´t exist")
