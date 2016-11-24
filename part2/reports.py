
"""
What is the title of the most played game?
Expected name of the function: get_most_played(file_name)
Expected output of the function: (string)
Other expectation:  if there is more than one, then return the first from the file 
"""
def get_most_played(file_name):

    game_list = []
    with open(file_name, mode="r", encoding="UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))

    max = game_list[0]
    for game in game_list:
        if float(game[1]) > float(max[1]):
            max = game

    return max[0]

"""
How many copies have been sold total?
Expected name of the function: sum_sold(file_name)
Expected output of the function: (number)
"""

def sum_sold(file_name):

    game_list = []
    with open(file_name, mode="r", encoding= "UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))

    return round(sum(float(game[1]) for game in game_list), 2)



"""
What is the average selling?
Expected name of the function: get_selling_avg(file_name)
Expected output of the function: (number)
Other expectation: if there is more than one, then return the first from the file
"""

def get_selling_avg(file_name):

    game_list = []
    with open(file_name, mode="r", encoding= "UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))

    
    # Removes duplicate games from the list before counting the avarage.
    for game_index1 in range(len(game_list)): 
        for game_index2 in range(game_index1+1, len(game_list)-1): 
            if game_list[game_index1][0] == game_list[game_index2][0]:
                game_list.pop(game_index2)

    return (sum(float(game[1]) for game in game_list) / len(game_list))


"""
How many characters long is the longest title?
Expected name of the function: count_longest_title(file_name)
Expected output of the function: (number)
"""
def count_longest_title(file_name):

    game_list = []
    with open(file_name, mode="r", encoding= "UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))
    
    return max(len(game[0]) for game in game_list)

"""
What is the average of the release dates?
Expected name of the function: get_date_avg(file_name)
Expected output of the function: average year (number)
Other expectation: the return value must be the rounded up average
"""
def get_date_avg(file_name):

    game_list = []
    with open(file_name, mode="r", encoding= "UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))
    
    return round(sum(int(game[2]) for game in game_list) / len(game_list))

"""
What properties has a game?
Expected name of the function: get_game(file_name, title) .
Expected output of the function: a list of all the properties of the game (a list of various type).
Details: the function get a parameter named game. This is the title of the game (string).
This is an existent game. The function return a list of the properties of this game including the title. An example return value: ["Minecraft", 23, 2009, "Survival game", Microsoft]. 
"""

def get_game(file_name, title):

    game_list = []
    with open(file_name, mode="r", encoding= "UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))

    try:
        title_index = [game[0] for game in game_list].index(title)
    except ValueError:
        print(title, "is not in the list of games.")

    game_list[title_index][1] = float(game_list[title_index][1])
    game_list[title_index][2] = int(game_list[title_index][2])

    return game_list[title_index]

"""
How many games are there grouped by genre?
Expected name of the function: count_grouped_by_genre(file_name)
Expected output of the function: a dictionary with this structure: { [genre] : [count] }
Detailed description: return a dictionary where each genre is associated with the count of the games of its genre
"""
def count_grouped_by_genre(file_name):

    game_list = []
    with open(file_name, mode="r", encoding= "UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))
    
    genre_dict = {}
    for game in game_list:

        if game[3] not in genre_dict:
            genre_dict[game[3]] = 1
        else:
            genre_dict[game[3]] += 1

    return genre_dict

"""
What is the date ordered list of the games? 
Expected name of the function: get_date_ordered(file_name)
Expected output of the function: the date ordered list of the titles (list of string)
Other expectation: The secondary ordering rule is the alphabetical ordering of the titles. So if there are titles from the same year, you need to order them alphabetically in ascending order.
"""

def get_date_ordered(file_name):

    game_list = []
    with open(file_name, mode="r", encoding= "UTF-8") as game_file:
        for line in game_file:
            game_list.append(line.strip().split("\t"))
    
    # Searches for games that were released in the same year, swaps them in alphabetical order.
    for game_index1 in range(len(game_list)):
        for game_index2 in range(game_index1, len(game_list)):
            if game_list[game_index1][2] == game_list[game_index2][2]:
                if game_list[game_index1][0] > game_list[game_index2][0]:
                    game_list[game_index1], game_list[game_index2] = game_list[game_index2], game_list[game_index1]
    
    return  [game[0] for game in sorted(game_list, key=lambda game: game[2], reverse= True)]







    
