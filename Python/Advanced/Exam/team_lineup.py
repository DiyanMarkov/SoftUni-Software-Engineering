def team_lineup(*args):

    countries = {}

    for arg in args:
        name = arg[0]
        country = arg[1]

        if country not in countries:
            countries[country] = []

        countries[country].append(name)

    sorted_countries = sorted(countries.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for country, players in sorted_countries:
        result += f"{country}:\n"

        for player in players:
            result += f"  -{player}\n"

    return result

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))


