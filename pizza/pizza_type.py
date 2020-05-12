from typing import Dict, NoReturn


class BasePizza:
    tomato_sauce = 200
    mozarella = 300

    def __init__(self, size: str) -> NoReturn:
        """
        Initialization of Base Pizza Recipe
        :param size:
        """
        self.size = size

    def dict(self) -> Dict[str, Dict[str, str]]:
        """

        :return:
        """
        return {
            self.__class__.__name__: {
                key: value for key, value in self.__dict__ if key != 'size'
            }
        }

    def __eq__(self, other):
        """

        :return:
        """
        pass


class Margherita(BasePizza):
    tomatoes = 100

    def __init__(self, size) -> NoReturn:
        """
        Initialization of Base Pizza Recipe
        :param size:
        """
        super().__init__(size)


class Pepperoni(BasePizza):
    pepperoni = 200

    def __init__(self, size) -> NoReturn:
        """
        Initialization of Base Pizza Recipe
        :param size:
        """
        super().__init__(size)


class Hawaiian(BasePizza):
    chicken = 250
    pineapples = 150

    def __init__(self, size) -> NoReturn:
        """
        Initialization of Base Pizza Recipe
        :param size:
        """
        super().__init__(size)

