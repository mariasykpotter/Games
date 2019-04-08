import game

kitchen = game.Room('Kitchen')
kitchen.set_description('My favourite room with frige and food.')
dining_room = game.Room('Dining Room')
dining_room.set_description('Small room with big table.')
bathroom = game.Room('Bathroom')
bathroom.set_description('Toilet and shower. Thats all.')
kitchen.room_location(dining_room, 'south')
dining_room.room_location(kitchen, 'north')
dining_room.room_location(bathroom, 'west')
bathroom.room_location(dining_room, 'east')
zombie = game.Enemy('Ted', 'A stuped zombie')
zombie.set_conversation('Aaaaaaaarrrr!')
zombie.set_weakness('sword')
dining_room.set_character(zombie)
spider = game.Enemy('Spidy', 'A small spider but so terrible.')
spider.set_conversation('Now I living here. I must leave.')
spider.set_weakness('magazine')
bathroom.set_character(spider)
sword = game.Item('sword')
sword.set_description('A long acute sword.')
bathroom.set_item(sword)
magazine = game.Item('magazine')
magazine.set_description('A boring magazine.')
dining_room.set_item(magazine)
current_room = kitchen
bag = []
dead = False

if __name__ == '__main__':
    while dead == False:

        print('\n')
        current_room.get_details()

        neighbor = current_room.get_character()
        if neighbor is not None:
            neighbor.describe()

        item = current_room.get_item()
        if item is not None:
            item.describe()

        command = input('>>> Please, choose next direction: ')

        if command.lower() in ['north', 'south', 'east', 'west']:
            current_room = current_room.move(command)
        elif command == 'speak':
            if neighbor is not None:
                neighbor.talk()
        elif command == 'fight':
            if neighbor is not None:
                print('Want you to fight with?')
                fight_with = input()
                if fight_with in bag:
                    if neighbor.fight(fight_with) == True:
                        print('Congratulation, you won this combat!')
                        current_room.character = None
                        if neighbor.get_defeated() == 2:
                            print('Congratulations, you have magic victory!')
                            dead = True
                    else:
                        print('Oh dear, you lost.')
                        print('That is over of the game')
                        dead = True
                else:
                    print('You don\'t have a ' + fight_with)
            else:
                print('You don\'t have opponent here')
        elif command == 'take':
            if item is not None:
                print('You put the ' + item.get_name() + ' in your bag')
                bag.append(item.get_name())
                current_room.set_item(None)
            else:
                print('At this room nothing to take!')
        else:
            print('I don\'t know how to ' + command)
