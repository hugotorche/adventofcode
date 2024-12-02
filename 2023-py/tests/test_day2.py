from runs.day2 import total_game_ids, total_game_powers

game1 = [["""Game 65: 4 green, 1 blue, 2 red; 3 blue, 3 green, 11 red; 6 green, 3 blue,
         3 red; 5 red, 4 blue; 8 red, 5 blue, 2 green"""]]
game2 = [["""Game 66: 10 green, 13 red; 1 blue, 2 red, 4 green; 7 red, 7 green;
          19 green, 9 red, 1 blue; 16 green, 16 red, 2 blue; 10 red, 11 green"""]]


def test_total_game_ids():
    assert total_game_ids(game1) == 65
    assert total_game_ids(game2) == 0


def test_total_game_powers():
    assert total_game_powers(game1) == 330
    assert total_game_powers(game2) == 608
