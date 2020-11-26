from microbit import *
import random
import music
from gesture import *
gesture = Gesture()

directions = [Image.ARROW_N, Image.ARROW_W, Image.ARROW_E, Image.ARROW_S]

potential_directions = ['up', 'down', 'left', 'right']
random.choice(potential_directions)
store_directions = [
    random.choice(potential_directions),
    random.choice(potential_directions),
    random.choice(potential_directions),
    random.choice(potential_directions),
    random.choice(potential_directions)
]


gesture_map = {
    'up': Image.ARROW_S,
    'down': Image.ARROW_N,
    'left': Image.ARROW_E,
    'right': Image.ARROW_W,
}


for dir in store_directions:
    display.show(gesture_map[dir])
    print(dir)
    sleep(1000)
    display.clear()
    sleep(500)

display.show(Image.TARGET)
sleep(500)
# track the current guesture you want them to do
current = 0
store_directions[current]
error = 0

while True:
    if error >= 3:
        display.show(Image.ANGRY)
        pin2.write_digital(1)
        music.play(music.POWER_DOWN)
    elif current >= 5:
        display.show(Image.HAPPY)
        music.play(music.WEDDING)
    else:
        g = gesture.read()
        if g == 'none':
            display.clear()
        elif g == store_directions[current]:
            print(g)
            display.show(Image.YES)
            sleep(300)
            current = current+1
        else:
            error = error +1
            display.show(Image.NO)
            sleep(300)

        sleep(300)