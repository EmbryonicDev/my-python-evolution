class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        self.ratings.append(rating)

    def __str__(self):
        ratings = len(self.ratings)
        if ratings > 0:
            average = sum(self.ratings) / ratings
            print_ratings = f"{ratings} ratings, average {average:.1f} points"
        else:
            print_ratings = 'no ratings'
        return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\n{print_ratings}"


def minimum_grade(rating: float, series_list: list):
    results = []
    for show in series_list:
        for show_rating in show.ratings:
            if show_rating >= rating:
                results.append(show)
    return results


def includes_genre(genre: str, series_list: list):
    results = []
    for show in series_list:
        if genre in show.genres:
            results.append(show)
    return results


if __name__ == '__main__':

    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
