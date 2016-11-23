import reports

def main():
    
    year = int(input("Is there a game from (enter a year): "))
    
    print("\n", reports.get_genres("game_stat.txt"))
    genre = input("Number of games from (enter a genre): ")

    print("\n", reports.sort_abc("game_stat.txt"))
    title = input("Line number of (enter a title): ")

    genre_list = reports.get_genres("game_stat.txt")
    title_list = reports.sort_abc("game_stat.txt")

    report_dict = {
        "Game count: ": reports.count_games("game_stat.txt"),
        "Is there a game from " + str(year) + ": " : reports.decide("game_stat.txt", year),
        "Latest game: ": reports.get_latest("game_stat.txt"),
        "Number of " + genre + " games: ": reports.count_by_genre("game_stat.txt", genre),
        "Line number of " + title + ": ": reports.get_line_number_by_title("game_stat.txt", title),
        "Ordered titles: ": ("" .join( game + ", " for game in title_list if game != title_list[-1])) + title_list[-1],     # Adds a comma between each game title
        "Genres: ": ("" . join( genre + ", " for genre in genre_list if genre != genre_list[-1])) + genre_list[-1],         # Adds a comma between each genre
        "Release date of top-sold FPS: ": reports.when_was_top_sold_fps("game_stat.txt")}
    
    export_file = open("report-results.txt", mode="w")

    for key in report_dict:

        export_file.write(key)
        export_file.write(str(report_dict[key]))
        export_file.write("\n\n")


    export_file.close()


if __name__ == "__main__":
    main()
