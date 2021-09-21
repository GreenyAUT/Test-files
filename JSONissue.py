import json

response = {'lat': 47.6228, 'lon': 14.3469, 'timezone': 'Europe/Vienna', 'timezone_offset': 7200, 'hourly': [{'dt': 1632240000, 'temp': 3.87, 'feels_like': 3.87, 'pressure': 1028, 'humidity': 91, 'dew_point': 2.54, 'uvi': 0.14, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 1, 'wind_gust': 1.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0}, {'dt': 1632243600, 'temp': 3.93, 'feels_like': 3.93, 'pressure': 1028, 'humidity': 94, 'dew_point': 3.05, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 358, 'wind_gust': 1.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0}, {'dt': 1632247200, 'temp': 3.12, 'feels_like': 3.12, 'pressure': 1028, 'humidity': 95, 'dew_point': 2.4, 'uvi': 0, 
'clouds': 90, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 335, 'wind_gust': 1.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632250800, 'temp': 2.51, 'feels_like': 2.51, 'pressure': 1028, 'humidity': 95, 'dew_point': 1.79, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 294, 'wind_gust': 1.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632254400, 'temp': 2.12, 'feels_like': 2.12, 'pressure': 1029, 'humidity': 94, 'dew_point': 1.26, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 284, 'wind_gust': 1.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632258000, 
'temp': 1.55, 'feels_like': 1.55, 'pressure': 1029, 'humidity': 94, 'dew_point': 0.69, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 281, 'wind_gust': 1.19, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632261600, 'temp': 1.07, 'feels_like': 1.07, 'pressure': 1029, 'humidity': 93, 'dew_point': 3.2, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 268, 'wind_gust': 1.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632265200, 'temp': 0.96, 'feels_like': 0.96, 'pressure': 1029, 'humidity': 92, 'dew_point': 2.98, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 261, 'wind_gust': 1.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632268800, 'temp': 0.57, 'feels_like': 0.57, 'pressure': 1028, 'humidity': 92, 'dew_point': 2.54, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 260, 'wind_gust': 1.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632272400, 'temp': 
-0.62, 'feels_like': -0.62, 'pressure': 1028, 'humidity': 94, 'dew_point': 1.71, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 263, 'wind_gust': 1.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632276000, 'temp': -1.11, 'feels_like': -3, 'pressure': 1028, 'humidity': 95, 'dew_point': 1.41, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.49, 'wind_deg': 252, 'wind_gust': 1.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632279600, 'temp': -1.26, 'feels_like': -3.16, 'pressure': 1028, 'humidity': 95, 'dew_point': 1.27, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 270, 'wind_gust': 1.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632283200, 'temp': -1.35, 'feels_like': -3.55, 'pressure': 1028, 'humidity': 96, 'dew_point': 1.16, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 262, 'wind_gust': 1.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632286800, 'temp': -1.2, 'feels_like': -3.44, 'pressure': 1028, 'humidity': 95, 'dew_point': 1.25, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 276, 'wind_gust': 1.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0}, {'dt': 1632290400, 'temp': 0.24, 'feels_like': -1.84, 'pressure': 1028, 'humidity': 91, 'dew_point': 2.11, 'uvi': 0.18, 'clouds': 100, 
'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 274, 'wind_gust': 3.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0}, {'dt': 1632294000, 'temp': 2.31, 'feels_like': 0.04, 'pressure': 1027, 'humidity': 82, 'dew_point': 2.66, 'uvi': 0.71, 'clouds': 98, 'visibility': 10000, 'wind_speed': 2.18, 'wind_deg': 298, 'wind_gust': 4.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0}, {'dt': 1632297600, 'temp': 3.54, 'feels_like': 1.12, 'pressure': 1027, 'humidity': 74, 'dew_point': 2.42, 'uvi': 1.61, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.56, 'wind_deg': 310, 'wind_gust': 5.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0}, {'dt': 1632301200, 'temp': 
3.83, 'feels_like': 1.34, 'pressure': 1026, 'humidity': 72, 'dew_point': 2.32, 'uvi': 2.67, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.7, 'wind_deg': 322, 'wind_gust': 5.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0}, {'dt': 1632304800, 'temp': 3.34, 'feels_like': 1.12, 'pressure': 1026, 'humidity': 75, 'dew_point': 2.34, 'uvi': 3.35, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.3, 'wind_deg': 327, 'wind_gust': 4.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0}, {'dt': 1632308400, 'temp': 3.6, 'feels_like': 1.46, 'pressure': 1026, 'humidity': 73, 'dew_point': 2.23, 'uvi': 3.7, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.27, 'wind_deg': 326, 'wind_gust': 4.37, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0}, {'dt': 1632312000, 'temp': 3.86, 'feels_like': 1.89, 'pressure': 1026, 'humidity': 73, 'dew_point': 2.46, 'uvi': 3.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.14, 'wind_deg': 330, 'wind_gust': 4.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0}, {'dt': 1632315600, 'temp': 
3.81, 'feels_like': 2.16, 'pressure': 1026, 'humidity': 76, 'dew_point': 3.01, 'uvi': 2.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 335, 'wind_gust': 3.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0.14}, {'dt': 1632319200, 'temp': 3.51, 'feels_like': 2.13, 'pressure': 1026, 'humidity': 82, 'dew_point': 3.75, 'uvi': 1.51, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 333, 'wind_gust': 3.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0.14}, {'dt': 1632322800, 'temp': 3.3, 'feels_like': 1.9, 'pressure': 1025, 'humidity': 86, 'dew_point': 4.18, 'uvi': 0.7, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 331, 'wind_gust': 2.99, 'weather': [{'id': 
804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0.15}, {'dt': 1632326400, 'temp': 2.95, 'feels_like': 1.44, 'pressure': 1026, 'humidity': 89, 'dew_point': 4.49, 'uvi': 0.21, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 328, 'wind_gust': 2.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0.15}, {'dt': 1632330000, 'temp': 2.14, 'feels_like': 0.85, 'pressure': 1026, 'humidity': 94, 'dew_point': 4.42, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 319, 'wind_gust': 2.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'pop': 0.07}, {'dt': 1632333600, 'temp': 1.11, 'feels_like': 1.11, 'pressure': 1027, 'humidity': 96, 'dew_point': 3.79, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 299, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0.07}, {'dt': 1632337200, 'temp': 0.9, 'feels_like': 0.9, 'pressure': 1027, 'humidity': 96, 'dew_point': 3.53, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 290, 'wind_gust': 1.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'pop': 0.02}, {'dt': 1632340800, 'temp': 0.55, 'feels_like': 0.55, 'pressure': 1027, 'humidity': 97, 'dew_point': 3.23, 'uvi': 0, 
'clouds': 84, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 272, 'wind_gust': 1.4, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'pop': 0.02}, {'dt': 1632344400, 'temp': -0.02, 'feels_like': -0.02, 'pressure': 1028, 'humidity': 97, 'dew_point': 2.76, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 264, 'wind_gust': 1.51, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'pop': 0.02}, {'dt': 1632348000, 'temp': -0.51, 'feels_like': -0.51, 'pressure': 1028, 'humidity': 97, 'dew_point': 2.3, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 253, 'wind_gust': 1.45, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'pop': 0.02}, {'dt': 1632351600, 'temp': -0.77, 'feels_like': -0.77, 'pressure': 1027, 'humidity': 97, 'dew_point': 2.03, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 241, 'wind_gust': 1.4, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632355200, 'temp': -1.03, 'feels_like': -2.86, 'pressure': 1027, 'humidity': 97, 'dew_point': 1.8, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 220, 'wind_gust': 1.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'pop': 0}, {'dt': 1632358800, 'temp': -1.26, 'feels_like': -3.31, 'pressure': 1027, 'humidity': 97, 'dew_point': 1.51, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 217, 'wind_gust': 1.47, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'pop': 0}, {'dt': 1632362400, 'temp': -1.34, 'feels_like': -3.61, 'pressure': 1026, 'humidity': 96, 'dew_point': 1.32, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.71, 'wind_deg': 212, 'wind_gust': 1.59, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'pop': 0}, {'dt': 1632366000, 'temp': -1.44, 'feels_like': -3.62, 'pressure': 1026, 'humidity': 96, 'dew_point': 1.14, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 208, 'wind_gust': 1.5, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'pop': 0}, {'dt': 1632369600, 'temp': -1.65, 'feels_like': -3.89, 'pressure': 1026, 'humidity': 95, 'dew_point': 0.73, 'uvi': 0, 'clouds': 31, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 204, 'wind_gust': 1.42, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'pop': 0}, {'dt': 1632373200, 'temp': -1.71, 'feels_like': -4.31, 'pressure': 1025, 'humidity': 93, 'dew_point': 0.5, 'uvi': 0, 'clouds': 26, 'visibility': 10000, 'wind_speed': 1.9, 'wind_deg': 201, 'wind_gust': 1.59, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'pop': 0}, {'dt': 1632376800, 'temp': 0.25, 'feels_like': -1.52, 'pressure': 1024, 'humidity': 88, 'dew_point': 1.63, 'uvi': 0.21, 'clouds': 22, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 203, 'wind_gust': 1.51, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'pop': 0}, {'dt': 1632380400, 'temp': 3.62, 'feels_like': 3.62, 'pressure': 1022, 'humidity': 77, 'dew_point': 2.96, 'uvi': 0.75, 'clouds': 7, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 207, 'wind_gust': 1.47, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1632384000, 'temp': 6.84, 'feels_like': 6.84, 'pressure': 1021, 'humidity': 63, 'dew_point': 3.19, 'uvi': 1.7, 'clouds': 8, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 208, 'wind_gust': 1.17, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1632387600, 'temp': 9.58, 'feels_like': 9.58, 'pressure': 1020, 'humidity': 51, 'dew_point': 2.91, 'uvi': 2.85, 'clouds': 8, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 348, 'wind_gust': 0.66, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1632391200, 'temp': 11.41, 'feels_like': 9.76, 'pressure': 1019, 'humidity': 44, 'dew_point': 2.38, 'uvi': 3.87, 'clouds': 8, 'visibility': 10000, 
'wind_speed': 0.85, 'wind_deg': 351, 'wind_gust': 0.89, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1632394800, 'temp': 12.69, 'feels_like': 11.06, 'pressure': 1018, 'humidity': 40, 'dew_point': 2.08, 'uvi': 4.28, 'clouds': 7, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 358, 'wind_gust': 1.1, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1632398400, 'temp': 13.18, 'feels_like': 11.55, 'pressure': 1018, 'humidity': 38, 'dew_point': 1.78, 'uvi': 3.96, 'clouds': 8, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 359, 'wind_gust': 1.42, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1632402000, 'temp': 13.02, 'feels_like': 11.4, 'pressure': 1017, 'humidity': 39, 'dew_point': 2.04, 'uvi': 3.1, 'clouds': 1, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 359, 'wind_gust': 1.61, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 
'icon': '01d'}], 'pop': 0}, {'dt': 1632405600, 'temp': 12.74, 'feels_like': 11.14, 'pressure': 1016, 'humidity': 41, 'dew_point': 2.62, 'uvi': 1.91, 'clouds': 6, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 351, 'wind_gust': 1.41, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1632409200, 'temp': 11.81, 'feels_like': 10.4, 'pressure': 1016, 'humidity': 52, 'dew_point': 5.04, 'uvi': 0.87, 'clouds': 6, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 348, 'wind_gust': 1.44, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}]}


clouds_lst = []
cloud_type_lst = []
icon_lst = []
pop_lst = []
time_lst = []
temps_lst = []
feels_lst = []
pressure_lst = []
humidity_lst = []
dew_point_lst = []
uvi_lst = []
cloud_coverage_lst = []
visibility_lst = []
wind_speed_lst = []
wind_direction_lst = []
wind_gust_lst = []



for r in response['hourly']['weather']:
    clouds = r['main']
    clouds_lst.append(clouds)

for r in response['hourly']:
    cloud_type = r['description']
    cloud_type_lst.append(cloud_type)
    
for r in response['hourly']:
    icons = r['icon']
    icon_lst.append(icons)

for r in response['hourly']:
    pops = r['pop']
    pop_lst.append(pops)

for r in response['hourly']:
    times = r['dt']
    time_lst.append(times)

for r in response['hourly']:
    temps = r['temp']
    temps_lst.append(temps)

for r in response['hourly']:
    feels_like = r['feels_like']
    feels_lst.append(feels_like)

for r in response['hourly']:
    pressure = r['pressure']
    pressure_lst.append(pressure)

for r in response['hourly']:
    humidity = r['humidity']
    humidity_lst.append(humidity)
    
for r in response['hourly']:
    dew_point = r['dew_point']
    dew_point_lst.append(dew_point)

for r in response['hourly']:
    uvi = r['uvi']
    uvi_lst.append(uvi)

for r in response['hourly']:
    cloud_coverage = r['clouds']
    cloud_coverage_lst.append(cloud_coverage)

for r in response['hourly']:
    visibility = r['visibility']
    visibility_lst.append(visibility)

for r in response['hourly']:
    wind_speed = r['wind_speed']
    wind_speed_lst.append(wind_speed)

for r in response['hourly']:
    wind_direction = r['wind_deg']
    wind_direction_lst.append(wind_direction)

for r in response['hourly']:
    wind_gusts = r['wind_gust']
    wind_gust_lst.append(wind_gusts)
    
    
print(clouds_lst)
print(cloud_type_lst)
print(icon_lst)
print(pop_lst)
print(time_lst)
print(temps_lst)
print(feels_lst)
print(pressure_lst)
print(humidity_lst)
print(dew_point_lst)
print(uvi_lst)
print(cloud_coverage_lst)
print(visibility_lst)
print(wind_speed_lst)
print(wind_direction_lst)
print(wind_gust_lst)
