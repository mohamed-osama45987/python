import time
import datetime
import pygame


# alarm_time will be 23:00:00
def set_alarm(alart_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "./sound/alarm.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake UP!")
            # to play sound
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False

        time.sleep(1)  # to sleep for 1 sec


if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(alart_time=alarm_time)
