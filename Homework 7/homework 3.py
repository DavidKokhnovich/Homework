game_rules = {
'камень': 'ножницы',
'ножницы': 'бумага',
'бумага': 'камень'
}

def game(player1, player2):
    if game_rules[player1] == player2:
        return 'Игрок 1 победил!'
    elif game_rules[player2] == player1:
        return 'Игрок 2 победил!'
    else:
        return 'Ничья!'

player_1 = input('Выберите камень, ножницы или бумагу : ')
player_2 = input('Выберите камень, ножницы или бумагу : ')

print(game(player_1, player_2))
