class Categories:
    """Класс, определяющий категории продуктов питания растительного происхождения
    Атрибуты класса условно сгруппированны в отдельные списки
    :param Oil: Атрибут, содержащий спикок из различных видов масла
    :param Paste: Атрибут, содержащий спискок различных видов пасты
    :param Nuts: Атрибут, содержащий спискок различных видов орехов
    :param Super_food: Атрибут, содержащий список продукты категории "Super Food" """

    __Food_categories = {
        "Oil": ["Масло льняное", "Масло подсолнечное", "Масло кунжутное", "Масло горчичное", "Масло оливковое"],
        "Paste": ["Паста кунжутная", "Паста кокосовая", "Паста арахисовая", "Паста шоколадная"],
        "Nuts": ["Кешью, Арахис, Грецкий орех, Фундук, Макадамия"],
        "Super_food": ["Гречка", "Нут", "Семена чиа"]}

    def __init__(self, food_category: str):
        self.food_category = food_category

        @property
        def food_category(self):
            return self.food_category

        @property.setter
        def category(self, food_category: str):
            """
            Выбор категории товаров, содержащих продукты
            :param food_category: желаемая категория товаров
            """
            if not isinstance(food_category, str):
                raise TypeError('Категория товара задается строковым значением')

            if not (food_category in self.__Food_categories):
                raise ValueError('Категория товара выбрана не корректно')
            self._cat = food_category


if __name__ == '__main__':
    purchase_1 = Categories("Масло")
    purchase_2 = Categories("Paste")

    print(purchase_1)
    print(purchase_2)
