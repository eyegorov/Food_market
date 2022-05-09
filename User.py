import re
import random


class User:
    """
    Класс пользователя описывает личные данные пользователя интренет-магазина
    :param: user_name: имя пользователя или логин
    :param: password: пароль пользователя, для установки пароля должны быть соблюдены некоторые требования к надежности"""

    def __init__(self, user_name: str, password_: str):
        self.user_name = user_name
        self.password = password_

        if len(password_) < 8:  # Немного похардкодил с password, но все-таки код заработал, жалко было бросать.
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

    def __repr__(self):
        return f'{self.__class__.__name__},({self.user_name}'

    def __str__(self):
        return f'Пользователь {self.user_name} авторизирован'


if __name__ == '__main__':
    new_user_1 = User("Anna", "778899W90QQ£")
    print(new_user_1)
    new_user_2 = User("Andrey", "1234QwerTy@")
    print(new_user_2)
    new_user_3 = User("Anton", "3221HnOasO&")
    print(new_user_3)
