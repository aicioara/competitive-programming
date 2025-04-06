import datetime

STARTING_COINS = 1507 # 2024-12-29 -> 2026-01-10
STARTING_COINS = 2724 # 2025-03-24 -> 2025-11-10
GOAL_COINS = 7200
STREAK_START = datetime.datetime(2025, 3, 24)
BIWEEKLY = datetime.datetime(2025, 1, 19)

def tshirt_date():
    coins = STARTING_COINS
    day = datetime.datetime.now()
    streak = (day - STREAK_START).days
    while True:
        if coins > GOAL_COINS:
            break

        day += datetime.timedelta(days=1)
        streak += 1

        # Daily checkin
        coins += 1

        # 30 day streak checkin
        if streak % 30 == 0:
            coins += 30

        # Daily challenge
        coins += 10

        # Every challenge in a month
        if day.month != (day + datetime.timedelta(days=1)).month:
            coins += 50

        # 25 challenges in a month
        if day.day == 25:
            coins += 25

        # Weekly luck on Sunday
        if day.weekday() == 6:
            coins += 10

        # Weekly contest on Saturday
        if day.weekday() == 5:
            coins += 5

        # Biweekly contest on Saturday
        if day.weekday() == 5 and ((day - BIWEEKLY).days // 7) % 2 == 0:
            coins += 5
            coins += 35 # Join both weekly and biweekly contest

    return day

if __name__ == "__main__":
    print(tshirt_date())
