def count_games(file_name):
    counter = 0
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for lines in game_file:
            counter += 1
    return counter


def decide(file_name, year):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for lines in game_file:
            game_list.append(lines.strip().split("\t"))

    for game in game_list:
        if int(game[2]) == year:
            return True
    return False


def get_latest(file_name):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for lines in game_file:
            game_list.append(lines.strip().split("\t"))

    latest_year = game_list[0][2]
    for game in game_list:
        if game[2] > latest_year:
            latest_year = game[2]

    result = []
    for game in game_list:
        if game[2] == latest_year:
            return game[0]


def count_by_genre(file_name, genre):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for lines in game_file:
            game_list.append(lines.strip().split("\t"))

    counter = 0
    for game in game_list:
        if game[3] == genre:
            counter += 1
    return counter


def get_line_number_by_title(file_name, title):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for lines in game_file:
            game_list.append(lines.strip().split("\t"))

    for game_index in range(len(game_list)):
        if game_list[game_index][0] == title:
            return game_index + 1
    raise ValueError("Game title doesn't exist.")


def sort_abc(file_name):
    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for lines in game_file:
            game_list.append(lines.strip().split("\t"))

    title_list = [game[0] for game in game_list]
    sorted_titles = []

    while title_list:
        max = title_list[0]
        for title in title_list:
            if title < max:
                max = title
        sorted_titles.append(max)
        title_list.remove(max)
    return sorted_titles


def get_genres(file_name):

    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for lines in game_file:
            game_list.append(lines.strip().split("\t"))

    return sorted(set([game[3] for game in game_list]), key=lambda genre: genre.lower())


def when_was_top_sold_fps(file_name):

    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for lines in game_file:
            game_list.append(lines.strip().split("\t"))

    for game in game_list:
        if game[3] == "First-person shooter":
            top_sold = game
            break

    for game in game_list:
        if game[3] == "First-person shooter":
            if float(game[1]) > float(top_sold[1]):
                top_sold = game
    return int(top_sold[2])
