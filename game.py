import random

items = ['wine', 'coffee', 'money', 'apple', 'weapon', 'knife', 'watch', 'shocker']


class Character:
    """
    Class for representing the Street object
    """

    def __init__(self, name, weaknes, item):
        """
         (Character, str, str, str) -> None
         Initialization object with specific properties
         :returns None
        """
        self.name = name
        self.weaknes = weaknes
        self.item = item

    def answer(self):
        """
        (Character) -> str
        :returns characters answer to player
        """
        if self.name in ['Batyar', 'Zbuy', 'Lort']:
            return 'Hi, I want {}. Give me it or I will hit you!'.format(self.item)
        if self.name in ['Gentleman', 'Student']:
            return 'Hi, how are you? Taste the Lviv {}. It is delicious.'.format(self.item)


class Street():
    """
    Class for representing the Street object
    """

    characters = [Character('Lort', 'knife', 'watch'),
                  Character('Zbuy', 'weapon', 'money'),
                  Character('Gentleman', None, 'coffee'),
                  Character('Student', None, 'apple'),
                  Character('Batyar', 'shocker', 'wine')]

    def __init__(self, street_name):
        """
         (Street, str) -> None
         Initialization object with specific properties
         :returns None
        """
        self.name = street_name
        self.character = random.choice(self.characters)
        self.item = random.choice(items)


class Player:
    """
    Class for representing the Street object
    """

    def __init__(self, name, health=3):
        """
         (Player, str, int) -> None
         Initialization object with specific properties
         :returns None
        """
        self.name = name
        self.health = health
        self.location = None
        self.bag = random.sample(items, 3)
