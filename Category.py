class Category:
    list_of_categories = []

    def __init__(self, category_name=None):
        """
        Создание атрибутов класса Категория
        :param category_name: параметр, описывает имя категории
        :param: list_of_categories: параметр, содержит список категорий
        выбранной категории
        """
        self._category_name = category_name
        self.list_of_categories.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._category_name})'


if __name__ == '__main__':