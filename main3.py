from game import *

stryyska_1 = Street('Stryyska')
kozelnytska_2 = Street('Kozelnytska')
franka_3 = Street('Franka')
shevchenka_4 = Street('Shevchenka')
krakivska_5 = Street('Krakivska')
shevchenka_6 = Street('Shevchenka')
franka_7 = Street('Franka')
kozelnytska_8 = Street('Kozelnytska')
stryyska_9 = Street('Stryyska')


route = [stryyska_1,
         kozelnytska_2,
         franka_3,
         shevchenka_4,
         krakivska_5,
         shevchenka_6,
         franka_7,
         kozelnytska_8,
         stryyska_9]

lotary = random.choice([True, False])
separator = '>>>'
player = Player(input('Hi, player! Please enter your name: '))
print(separator)
message = "Hi {}. Welcome to the Lviv traveling game. " \
          "You have {} in your bag. Let's start.".format(player.name, player.bag)
print(message)
print(separator)
iter = 0
while not iter < 8 or player.health > 0:
    player.location = route[iter]
    if lotary:
        print('You are lucky at this moment. You found {}. Congrats!'.format(player.location.item))
        player.bag.append(player.location.item)
        print('Now in you bag you have {}.'.format(player.bag))
    print(separator)
    print('Now you are on {} street. There you met a {}.\n'
          'He tells you: "{}"'.format(player.location.name.upper(), player.location.character.name,
                                      player.location.character.answer()))

    print(separator)
    if player.location.character.name in ['Lort', 'Zbuy', 'Batyar']:
        if player.location.character.weaknes in player.bag:
            print('You say: "Say it again to my {}. '
                  'Go away or you will have big problem. '
                  'Quickly!"'.format(player.location.character.weaknes))
            print(separator)
        elif player.location.character.item in player.bag:
            command = input('You have {} in your bag. '
                            'You can got it to him. Want you? Y/n: '.format(player.location.character.item))
            if command.lower() == 'y':
                print('Now you don\'t have {}. That was dangerous. But you still whole and healthy.\n'
                      'Let\'s go to the next street.'.format(player.location.character.item))
                player.bag.remove(player.location.character.item)
                print('Now in you bag you have {}.'.format(player.bag))
            else:
                player.health -= 1
                print(
                    'Oh, no! {} hit you. You have {} lives left'.format(player.location.character.name, player.health))
                print(separator)
        else:
            print('The {} beating you. You have a bad day.'.format(player.location.character.name))
    else:
        player.health += 1
        print('Now you have a nice mitting with new friend - {}. He takes you {} lives'.format(player.location.character.name, player.health))
        print(separator)
    iter += 1
    if player.location == stryyska_9:
        print('CONGRATULATIONS, YOU WON !!!')
        break
    elif player.health == 0:
        print('SORRY, BUT YOU LOSE. Lviv is dengerous city sametimes.')
        break
    else:
        input('Press [ENTER] to walk to the next street:')
        print(separator)