class Room():
    """
    Class for representing the Room object
    """

    def __init__(self, room_name):
        """
         (Room, str) -> None
         Initialization object with specific properties
         :returns None
        """
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_character(self, new_character):
        """
        (Room, Character) -> None
        Setter for initializaztion new character in the room
        :returns None
        """
        self.character = new_character

    def get_character(self):
        """
        (Room) -> Character
        :returns current character in the room
        """
        return self.character

    def set_description(self, room_description):
        """
        (Room, str) -> None
        Add room description
        :returns None
        """
        self.description = room_description

    def get_description(self):
        """
        (Room) -> str
        :returns description of current room
        """
        return self.description

    def get_name(self):
        """
        (Room) -> str
        :returns the room name
        """
        return self.name

    def get_item(self):
        """
        (Room) -> Item
        :returns item object in current room
        """
        return self.item

    def set_item(self, item_name):
        """
        (Room, Item) -> None
        Add new item object to the current room
        :returns None
        """
        self.item = item_name

    def describe(self):
        """
        (Room) -> None
        Just print description of item in current room
        :returns None
        """
        print(self.description)

    def room_location(self, room_to_link, direction):
        """
        (Room, Room, str) -> None
        Setting room near current room
        :returns None
        """
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        """
        (Room) -> None
        Displaying opportunities of your ways
        :returns None
        """
        print(self.name)
        print('>>>')
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print('The ' + room.get_name() + ' is ' + direction)

    def move(self, direction):
        """
        (Room, str) -> Room
        Change current room
        :returns Room
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print('You can\'t go that way')
            return self


class Character():
    """
    Class for representing the Character object
    """

    def __init__(self, char_name, char_description):
        """
        (Character, str, str) -> None
         Initialization object with specific properties
         :returns None
        """
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """
        (Room) -> None
        Just print description of character in current room
        :returns None
        """
        print(self.name + ' is here!')
        print(self.description)

    def set_conversation(self, conversation):
        """
        (Character, str)
        Add phrase for current character
        :returns None
        """
        self.conversation = conversation

    def talk(self):
        """
        (Character) -> None
        Just print answer from current character
        :returns None
        """
        if self.conversation is not None:
            print('[' + self.name + ' says]: ' + self.conversation)
        else:
            print(self.name + ' doesn\'t want to talk to you')

    def fight(self):
        """
        (Character) -> False
        Start combat process
        :returns False
        """
        print(self.name + ' doesn\'t want to fight with you')
        return False


class Enemy(Character):
    """
    Child class for representing the Enemy Character object
    """
    enemies_defeated = 0

    def __init__(self, char_name, char_description):
        """
        (Enemy, str, str) -> None
        Initialization object with specific properties
        :returns None
        """
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        """
        (Enemy, str) -> None
         Setting weakness for current Enemy character
        :returns None
        """
        self.weakness = item_weakness

    def get_defeated(self):
        """
        (Enemy) -> int
        :returns quantity of player victories
        """
        return Enemy.enemies_defeated


class Item():
    """
    Class for representing the Item object
    """

    def __init__(self, item_name):
        """
        (Item, str) -> None
        Initialization object with specific properties
        :returns None
        """
        self.name = item_name
        self.description = None

    def set_name(self, item_name):
        """
        (Item, str) -> None
        Add name of item
        :returns None
        """
        self.name = item_name

    def set_description(self, item_description):
        """
        (Item, str) -> None
        Add description of item
        :returns None
        """
        self.description = item_description

    def describe(self):
        """
        (Item) -> None
        Just print item which is in current room
        :returns None
        """
        print('The [' + self.name + '] is here - ' + self.description)
