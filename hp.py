print ("This program is for healthy programming"
       "in which you will get reminder to do"
       "healthy activities")
print("Enter 'stop' to stop reminder")

def log(rem):
    import datetime
    rem=rem[:-4]
    with open("mylogs.txt",'a') as f:
        f.writelines("\n"+str(rem)+"\t-------"+str(str(datetime.datetime.now())))
def play(rem):
    from pygame import mixer
    while True:
        mixer.init()
        mixer.music.load(rem)
        mixer.music.play()
        if input()=="stop":
            log(rem)
            break
def wait():
    from time import time
    initeye=initexe=initdri=time()
    while True:
        time()
        if time()-initdri>drisec:
            initdri = time()
            play("Drink.mp3")

        elif time() - initeye > eyesec:
            initeye = time()
            play(("Eye.mp3"))

        elif time()-initexe>exesec:
            initexe = time()
            play("Exercise.mp3")

if __name__ == '__main__':
    exesec=60
    drisec=10
    eyesec=30
    wait()