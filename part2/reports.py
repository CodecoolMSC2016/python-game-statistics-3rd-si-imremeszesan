
def get_most_played(file_name):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))

    most_played = game_list[0]
    for game in game_list:
        if float(game[1]) > float(most_played[1]):
            most_played = game
    return most_played[0]


def sum_sold(file_name):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))

    return round(sum(float(game[1]) for game in game_list), 2)


def get_selling_avg(file_name):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))

    # Removes duplicate games from the list before counting the avarage.
    for game_index1 in range(len(game_list)):
        for game_index2 in range(game_index1 + 1, len(game_list) - 1):
            if game_list[game_index1][0] == game_list[game_index2][0]:
                game_list.pop(game_index2)

    selling_sum = sum(float(game[1]) for game in game_list)
    return selling_sum / len(game_list)


def count_longest_title(file_name):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))

    return max(len(game[0]) for game in game_list)


def get_date_avg(file_name):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))

    date_sum = sum(int(game[2]) for game in game_list)
    return round(date_sum / len(game_list))


def get_game(file_name, title):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))

    title_index = [game[0] for game in game_list].index(title)
    game_list[title_index][1] = float(game_list[title_index][1])
    game_list[title_index][2] = int(game_list[title_index][2])

    return game_list[title_index]


def count_grouped_by_genre(file_name):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))

    genre_dict = {}
    for game in game_list:
        if game[3] not in genre_dict:
            genre_dict[game[3]] = 1
        else:
            genre_dict[game[3]] += 1
    return genre_dict


def get_date_ordered(file_name):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))

    # Searches for games that were released in the same year, swaps them in alphabetical order.
    for game_index1 in range(len(game_list)):
        for game_index2 in range(game_index1 + 1, len(game_list)):
            if game_list[game_index1][2] == game_list[game_index2][2]:
                if game_list[game_index1][0] > game_list[game_index2][0]:
                    game_list[game_index1], game_list[game_index2] = game_list[game_index2], game_list[game_index1]

    ordered_games = sorted(game_list, key=lambda game: game[2], reverse=True)
    return [game[0] for game in ordered_games]
