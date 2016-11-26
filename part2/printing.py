from reports import *

def main():
    print("Most played game: ", get_most_played("game_stat.txt"))
    print("\nCopies sold total: ", sum_sold("game_stat.txt"))
    print("\nSellling avarage: ", get_selling_avg("game_stat.txt"))
    print("\nLongest title: ", count_longest_title("game_stat.txt"))
    print("\nAvarage release date: ", get_date_avg("game_stat.txt"))
    print("\nProperties of x game: \n", get_game("game_stat.txt", "Minecraft"))
    print("\nGames in a genre: \n", count_grouped_by_genre("game_stat.txt"))
    print("\nDate ordered list of games: \n", get_date_ordered("game_stat.txt"))

if __name__ == "__main__":
    main()