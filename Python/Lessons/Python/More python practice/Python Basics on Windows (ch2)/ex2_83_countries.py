try:
    countries = open ('C://Users//brendan//Documents//ex83_countries.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    nations = countries.read()
    print(nations)
    countries.close()
