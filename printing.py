import reports
import export


def main():

    print("Every genre: ", reports.get_genres("game_stat.txt"))
    print("Number of genres: ", reports.count_by_genre("game_stat.txt", input("\nEnter a genre: ")), "\n")
    print("Number of games: ", reports.count_games("game_stat.txt"))
    print("Was a game released this year? ", reports.decide("game_stat.txt", input("\nEnter a year: ")), "\n")
    print("Every genre: \n", reports.get_genres("game_stat.txt"))
    print("\nLatest game: \n", reports.get_latest("game_stat.txt"))
    print("Line number of given title: ", reports.get_line_number_by_title(
        "game_stat.txt", input("\nEnter a title: ")), "\n")
    print("Games sorted by title: ", reports.sort_abc("game_stat.txt"))
    print("\nRelease date of top sold FPS: \n", reports.when_was_top_sold_fps("game_stat.txt"))

if __name__ == "__main__":
    main()
