def get_rainfall():
    rainfall = {}

    while True:
        city = input("Which city you want to add:\n")
        if not city:
            break

        rain_drop = input(f'Give rain drops for {city}: ')
        rainfall[city] = rainfall.get(city, 0) + int(rain_drop)

    for city, rain_drop in rainfall.items():
        print(f'{city}: {rain_drop}')


get_rainfall()
