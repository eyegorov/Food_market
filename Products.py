import random


class Product:


    def __init__(self, category: Category, product_name: str, price: int):
        """Класс Product описывает отдельно взятый товар и его характеристики
           :param product_name: наименование товара
           :param price: цена товара
           :param rating: рейтинг товара"""
        self.category = None
        self._product_name = product_name
        self._price = price
        self._rating = random.randint(0, 11)


        self._cat_name = category_name

    def __repr__(self):
        return f'{self.__class__.__name__},{self.category_name}, {self._product_name}'

    def __str__(self):
        return f'Выбранна категория товаров: {self.category_name}, включаящая в себя товар {self._product_name}.'


if __name__ == '__main__':
    Oil_1 = Product("Масло", "Масло оливковое", 300)
    print(Oil_1)
    Oil_2 = Product("Масло", "Масло льняное", 100)
    print(Oil_2)
    Oil_3 = Product("Масло", "Масло подсолнечное", 150)
    print(Oil_3)

    Paste_1 = Product("Паста", "Паста кокосовая", 100)
    print(Paste_1)
    Paste_2 = Product("Сало", "Паста арахисовая", 80)
    print(Paste_2)
