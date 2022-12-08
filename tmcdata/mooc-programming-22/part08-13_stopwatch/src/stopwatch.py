from datetime import datetime, time, timedelta


class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes < 59:
                self.minutes += 1
            else:
                self.minutes = 0

    def __str__(self):
        my_time = time(minute=self.minutes, second=self.seconds)
        return f"{my_time.strftime('%M:%S')}"


if __name__ == '__main__':
    watch = Stopwatch()
    for i in range(3609):
        print(watch)
        watch.tick()
