import math
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

    

    for game_index1 in range(len(game_list)): 
        for game_index2 in range(game_index1+1, len(game_list)-1): 
            if game_list[game_index1][0] == game_list[game_index2][0]:
                game_list.pop(game_index2)

    return round((sum(float(game[1]) for game in game_list) / len(game_list)), 2)


"""
How many characters long is the longest title?
Expected name of the function: count_longest_title(file_name)
Expected output of the function: (number)
"""

"""
What is the average of the release dates?
Expected name of the function: get_date_avg(file_name)
Expected output of the function: average year (number)
Other expectation: the return value must be the rounded up average
"""

"""
What properties has a game?
Expected name of the function: get_game(file_name, title) .
Expected output of the function: a list of all the properties of the game (a list of various type).
Details: the function get a parameter named game. This is the title of the game (string).
This is an existent game. The function return a list of the properties of this game including the title. An example return value: ["Minecraft", 23, 2009, "Survival game", Microsoft]. 
"""
