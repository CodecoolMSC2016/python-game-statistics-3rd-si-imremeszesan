import reports

title = input("Enter a title: ")
with open("reports.txt", mode="w", encoding="UTF-8") as export_file:
    for method in dir(reports):
        if not method.startswith('__'):
            try:
                export_file.write(str(eval('reports.' + method + '("game_stat.txt")')) + '\n')
            except TypeError:
                export_file.write(str(eval('reports.' + method + '("game_stat.txt"'+ ', "' + title + '")')) + '\n')

