import reports

def main():
    title = input("Enter a title <press enter to skip>: ") or "Minecraft"
    method_dict = {"get_most_played": "Most played game: ","sum_sold": "Copies sold total:","get_selling_avg": "Sellling avarage: " ,
                    "count_longest_title": "Longest title:","get_date_avg": "Avarage release date: ","get_game": "Properties of " + title + ": ",
                    "count_grouped_by_genre": "Games in a genre:","get_date_ordered": "Date ordered list of games: "}


    with open("reports.txt", mode="w", encoding="UTF-8") as export_file:
        for method in dir(reports):
            if not method.startswith('__'):
                try:
                    export_file.write(method_dict[method] + "\n" + str(eval('reports.' + method + '("game_stat.txt")')) + '\n\n')
                except TypeError:
                    export_file.write(method_dict[method] + "\n" + str(eval('reports.' + method + '("game_stat.txt"'+ ', "' + title + '")')) + '\n\n')

if __name__ == "__main__":
    main()
