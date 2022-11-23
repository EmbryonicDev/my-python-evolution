import math


def read_file(filename: str):
    file_list = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            parts = line.split(';')
            if parts[0] != 'Longitude':
                file_list.append(parts)
    return file_list


def get_station_data(filename: str):
    data = read_file(filename)
    station_data = {}
    for station in data:
        station_data[station[3]] = float(station[0]), float(station[1])
    return station_data


def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km


if __name__ == "__main__":
    # part 1
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
