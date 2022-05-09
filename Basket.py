class Basket:

def __init__(self):
    """Класс, описывающий корзину"""
    self.product_in_basket = []






if __name__ == '__main__':

    class Basket:
        """
        Класс для описания корзины
        """

        def __init__(self, purchase: Product = None):
            self.product_in_basket = []
            if purchase is not None:
                self.add_to_cart(purchase)

        def __str__(self):
            items_string = '\t'  # синтаксис?
            for item in self.order_array:
                items_string += str(item) + '\n\t' #синтаксис
            return f"в корзине следующие товары: \n{items_string}" if self.order_array else "корзина пуста"

        def __repr__(self):
            return f"{self.__class__.__name__}({self._order_array[0]})" if self._order_array else f"{self.__class__.__name__}(None)"

        @property
        def order_array(self) -> list[Product]:
            return self._order_array

        def add_to_cart(self, product: Product):
            """
            установка значений для товаров из категории
            :param product: объект типа Product или list[Product]
            """
            Product._check_type(product, Product)
            self._order_array.append(product)