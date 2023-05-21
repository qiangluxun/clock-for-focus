import time

def focus_timer():
    minutes = int(input("input："))
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1

    print('Time is up!')
