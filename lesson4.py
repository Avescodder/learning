import collections

days = {
    'weekend':['saturday', 'sunday'],
    'weekday':['monday', 'tuesady', 'wednesday', 'thursday', 'friday']
}

def get_day(days, day):
    [last] = collections.deque(days, maxlen=1)
    for k, v in days.items():
        if day in v:
            print(f"It's a {k}")
        elif k == last:
            print("Invalid day entered")
        

if __name__ == '__main__':
    day = input("Write a name of the day\n").lower()
    get_day(days, day)