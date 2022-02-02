import re


class User:
    """Класс пользователя описывает личные данные пользователя интренет-магазина
    :param: user_name: имя пользователя или логин
    :param: password: пароль пользователя"""

    def __init__(self, user_name=None, password=None):
        self._user_name = user_name
        self._password = password

    @classmethod
    def create_new_user(cls, username: str, password: str):
        while True:
            username = input("Введите имя пользователя:")
            email = input("Введите Ваш email")
            phone_number = int("Введите Ваш номер телефона")
            password = input("Введите Ваш пароль:")
            if len(password) < 8:
                print("Пароль должен содержать минимум 8 символов")
            elif re.search('[0-9]', password) is None:
                print("Пароль должен содержать буквы и цифры")

            elif re.search('[A-Z]', password) is None:
                print("Пароль должен содержать заглавные буквы")
            elif re.search('[@#%&!£$^*:?]', password) is None:
                print("Пароль должен содержать специальные символы")
            else:
                print(f'Пароль для пользователя {username}  установлен.')
            break
