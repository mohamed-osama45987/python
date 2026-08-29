# used to performe mutiple tasks concurrently at the same time
# Good for I/O tasks like reading files or calling an api

import threading
import time


def walk_dog(dog_name, last):
    time.sleep(8)  # wait 8 sec
    print(f"You finish walking {dog_name}{last}")


def take_out_trash():
    time.sleep(2)
    print("You take out the trash")


def get_mail():
    time.sleep(4)
    print("You get the mail")


# you can call all of them at the same time like
# if a function conatins args you need to pass an args tuple and if only 1 arg you must add , at the end like rgs=("Scooby",).
chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()  # to start the thread

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# to wait for all the theads to finish before printing this value
chore1.join()
chore2.join()
chore2.join()
print("All chores are completed")


# if you called them like this they will excute in order meaning i the second function will have to wait
# for the first function to finish before excuting
# called seqauntial execution
walk_dog()
take_out_trash()
get_mail()
