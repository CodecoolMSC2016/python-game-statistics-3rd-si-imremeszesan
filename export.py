import reports


def main():
    year = int(input("Is there a game from (enter a year) or <press enter to skip>: ") or 1999)

    print("\n", reports.get_genres("game_stat.txt"))
    genre = input("Number of games from (enter a genre) or <press enter to skip>: ") or "RPG"

    print("\n", reports.sort_abc("game_stat.txt"))
    title = input("Line number of (enter a title) or <press enter to skip>: ") or "Minecraft"

    genre_list = reports.get_genres("game_stat.txt")
    title_list = reports.sort_abc("game_stat.txt")

    with open("report-results.txt", mode="w", encoding="UTF-8") as export_file:

        export_file.write("Game count: " + str(reports.count_games("game_stat.txt")) + "\n\n")
        export_file.write("Is there a game from " + str(year) + ": "
                          + str(reports.decide("game_stat.txt", year)) + "\n\n")
        export_file.write("Latest game: " + str(reports.get_latest("game_stat.txt")) + "\n\n")
        export_file.write("Number of " + genre + " games: "
                          + str(reports.count_by_genre("game_stat.txt", genre)) + "\n\n")
        export_file.write("Line number of " + title + ": "
                          + str(reports.get_line_number_by_title("game_stat.txt", title)) + "\n\n")
        export_file.write("Ordered titles: \n" + ("" .join(game +
                                                           ", " for game in title_list if game != title_list[-1])) + title_list[-1] + "\n\n")
        export_file.write("Genres: " + ("" . join(genre + ", " for genre in genre_list if genre !=
                                                  genre_list[-1])) + genre_list[-1] + "\n\n")
        export_file.write("Release date of top-sold FPS: " +
                          str(reports.when_was_top_sold_fps("game_stat.txt")) + "\n\n")

if __name__ == "__main__":
    main()
