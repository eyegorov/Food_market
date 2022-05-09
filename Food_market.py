import re


class Product:

    def __init__(self, name: str, price: int, rating: int):
        """Класс Product описывает отдельно взятый товар и его характеристики
           :param name: наименование товара
           :param price: цена товара
           :param rating: рейтинг товара"""
        self.name = name
        self._price = price
        self._rating = rating

    def __repr__(self):
        return f'({self.name}, {self._price}, {self._rating}'

    def __str__(self):
        return f'({self.name}, цена:{self._price}, рейтинг: {self._rating})'


class Category:

    def __init__(self, name: str, category_list: list[Product]):
        """
        Создание атрибутов класса Категория
        :param name: параметр, описывает имя категории
        :param: category_list: параметр, содержит товаров категории
        """
        self.name = name
        self.category_list = category_list

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.category_list})'

    def __str__(self):
        return f'Выбранна категория товаров: {self.name}, включаящая в себя следующие товары: {self.category_list}.'


class Basket:

    def __init__(self, product: Product = None):
        """
        Класс, описывающий корзину покупателя интренрет-магазина
        :param product: атрибут, содержащий список товаров, содержащихся в корзине
        """
        self.product_in_basket = []
        if product is not None:
            self.add_product_to_basket(product)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.product_in_basket}'

    def __str__(self):
        return f'Товаров в корзине: {self.product_in_basket}'

    @property
    def product_in_basket(self) -> list[Product]:
        return self.product_in_basket

    def add_product_to_basket(self, product: Product):
        self.product_in_basket.append(product)


class User:

    def __init__(self, user_name: str, password_: str, user_basket: Basket = None):
        """
            Класс пользователя описывает личные данные пользователя интренет-магазина
            :param: user_name: имя пользователя или логин
            :param: password: пароль пользователя, для установки пароля должны быть соблюдены некоторые требования
            к надежности
            :param: user_basket параметр корзины отельно взятого пользователя User

            """
        self.user_name = user_name
        self.password = password_
        self.basket = user_basket

        if len(password_) < 8:
            raise TypeError("Пароль должен содержать минимум 8 символов")
        elif re.search('[0-9]', password_) is None:
            raise TypeError("Пароль должен содержать буквы и цифры")
        elif re.search('[A-Z]', password_) is None:
            raise TypeError("Пароль должен содержать заглавные буквы")
        elif re.search('[@#%&!£$^*:?]', password_) is None:
            raise TypeError("Пароль должен содержать специальные символы")
        else:
            print(f'Пароль для пользователя {user_name} установлен.')
            self.password = password_

    def add_product_to_basket(self, product: Product) -> None:
        if not self.user_name:
            self.user_name = None
        """Добавление товара в корзину текущего пользователя"""
        self.user_name.basket.add_product_to_basket(product)

    def __repr__(self):
        return f'{self.__class__.__name__},({self.user_name},{self.basket})'

    def __str__(self):
        return f'Пользователь {self.user_name} авторизирован, в корзине пользователя товаров: {self.basket}'


if __name__ == '__main__':
    new_user_1 = User("Anna", "778899W90QQ£", )

    """Создание продуктов категорий"""
    oil_product_1 = Product("Масло оливковое хол. отжима", 500, 7)
    oil_product_2 = Product("Масло льняное хол. отжима", 200, 8)
    oil_product_3 = Product("Масло кунжутное хол. отжима", 400, 7)
    paste_product_1 = Product("Паста арахисовая", 200, 6)
    paste_product_2 = Product("Паста кокосовая", 200, 10)
    paste_product_3 = Product("Паста арахисовая", 500, 10)
    nut_product_1 = Product("Грецкий орех", 390, 8)
    nut_product_2 = Product("Кешью", 490, 8)
    nut_product_3 = Product("Арахис", 200, 7)
    """Создание категорий товаров"""
    oil_category = Category("Oil", [oil_product_1, oil_product_2, oil_product_3])
    paste_category = Category("Паста", [paste_product_1, paste_product_2, paste_product_3])
    nut_category = Category("Орехи", [nut_product_1, nut_product_2, nut_product_3])
    Basket.add_product_to_basket(Product("Арахис", 200, 7))
   