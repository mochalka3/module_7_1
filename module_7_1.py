class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.file_name = 'products.txt'

    def get_products(self):
        lines = []
        f = open(self.file_name, 'r')
        products = f.read()
        f.close()
        return products

    def add(self, *products):
        existing_products = self.get_products()
        new_products = list(filter(lambda x: str (x) not in existing_products, products))
        for product in products:
            if str (product) in existing_products:
                print(f"Продукт {product} уже есть в магазине")
            return

        with open(self.file_name, 'a+') as f:
            for product in new_products:
                f.write(f"{product}\n")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
