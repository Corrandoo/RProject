import arduino_connector as arduino
import tkinter as tk
from psychopy import visual, core, event, clock
import random


arduino.connect_to_arduino()

def get_config_data():
    conf = open('config.txt', 'rt', encoding='utf-8')
    configuration = []
    for line in conf:
        configuration.append(line.split(" ")[2])
    return configuration



config = get_config_data()

isi_time = float(config[0])
stim_duration = float(config[1])


#### GET SCREEN RESOLUTION
root = tk.Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
#### STIMULUS PREPARATION
stims = ['yes_LI.jpg', 'rm5.png']
stims_number = random.randint(int(config[2]), int(config[3]))
total_stims_number = stims_number * 2

# a=random.sample(stims2, 40)

txt_1 = u'Сейчас вам потребуется ознакомиться с видео-роликами. Как будете готовы - нажмите "пробел".'
txt_2 = u'Отлично! теперь ваша задача - сыграть эти мелодии самостоятельно. Как будете готовы - нажмите "пробел".'

win = visual.Window([w, h], color=(config[4]))
ISI = clock.StaticPeriod(win=win, screenHz=59, name='ISI')

####OPENING
txt = visual.TextStim(win, text= u'Приготовьтесь. Как будете готовы - нажмите "пробел".', font='Helvetica', pos=[0.5, 0])
txt.draw()
win.flip()
event.waitKeys(keyList=['space'])
####OBSERVATION BEFORE
#movs = [visual.ImageStim(win, i, size=[w, h]) for i in stims]
movs = [visual.ImageStim(win, image=i, mask=None, units='', pos=(0.0, 0.0), size=None, ori=0.0, color=(1.0, 1.0, 1.0), colorSpace='rgb', contrast=1.0, opacity=1.0, depth=0, interpolate=False, flipHoriz=False, flipVert=False, texRes=128, name=None, autoLog=None, maskParams=None) for i in stims]

txt = visual.TextStim(win, text=txt_1, font='Helvetica', pos=[0.5, 0])
txt.draw()
win.flip()
event.waitKeys(keyList=['space'])
previous_stims = [] #list for controlling situations when we have more than 3 shows one by one
is_showing_only_one_type = False
stim1_shows = 0 #number of shows of each stim
stim2_shows = 0

for a in range (0, total_stims_number, 1):
    stim_type = random.randint(0, 1)
    previous_stims.append(stim_type)
    if stim_type == 0:
        if stim1_shows > stims_number:
            is_showing_only_one_type = True
            stim_type = 1
    elif stim_type == 1:
        if stim2_shows > stims_number:
            is_showing_only_one_type = True
            stim_type = 0

    if (a > 2) and (not is_showing_only_one_type):
        if (previous_stims[-1] == previous_stims[-2]) and (previous_stims [-2] == previous_stims [-3]):
            if stim_type == 0:
                stim_type = 1
                previous_stims[-1] = stim_type
            elif stim_type == 1:
                stim_type = 0
                previous_stims[-1] = stim_type
            else:
                win.close()
                core.quit()

    if stim_type == 0:
        stim1_shows += 1
    else:
        stim2_shows += 1
    mov = movs[stim_type]
    mov.draw()
    win.flip()
    if stim_type == 0:
        arduino.vibrate(stim_duration) #this will stop the stim for the configured time and will make arduino vibrate
    else:
        core.wait(stim_duration)

    win.flip()
    ISI.start(isi_time)
    ISI.complete()

txt = visual.TextStim(win, text=txt_1, font='Helvetica', pos=[0.5, 0])
txt.draw()
win.flip()
event.waitKeys(keyList=['space'])

####MAIN EXPERIMENT SEQUENCE

#movs = [visual.MovieStim3(win, i, size=[w,h]) for i in stims2]
#for mov in movs:
#    while mov.status != visual.FINISHED:
#        mov.draw()
#        win.flip()
#
#    win.flip()
##    event.waitKeys()



win.close()
core.quit()
# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
