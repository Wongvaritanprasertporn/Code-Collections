import keyboard
import sys
import os
import time

os.system('cls')

class Player:
    def __init__(self, name):
        self.name = name
        self.chance = 3

    def damage(self):
        self.chance -= 1

def disp_dialogue(dialogue):
    for character in dialogue:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print('\n')

def question(choice1, choice2):
    print(f'1 >>> {choice1}')
    print(f'2 >>> {choice2}')
    while True:
        key = int(input('>>> '))
        if key == 1 or key == 2:
            return key

intro = 'เกมนี้ได้รับแรงบันดาลใจจากเพลง วันหนึ่งฉันเดินเข้าป่า ของ แมกซ์ เจนมานะ'

disp_dialogue(intro)
player = Player(input('กรุณาตั้งชื่อตัวละคร\n>>> '))

dialogue1 = f'วันหนึ่ง {player.name} เดินเข้าป่า {player.name} เจอนกตัวหนึ่ง มันถาม {player.name} ว่าจะไปไหน'
dialogue2 = f'ไกลเกินกว่าที่ {player.name} เคยไป'
dialogue3 = f'อย่างน้อยก็ไม่ต้องพบเจอคนใจร้ายอย่างเธอ คนที่ไม่มีน้ำใจ ไม่มีเยื่อใยให้คนเคยรักกัน ใจร้ายอย่างเธอ ต้องทิ้งให้อยู่คนเดียว เผื่อเธอเหงาขึ้นมาจะได้กลับมารักกัน'
dialogue4 = f'วันหนึ่ง {player.name} เดินเข้าป่า {player.name} เจอเสือตัวใหญ่ มันถาม {player.name} ว่ากลัวบ้างไหม'
dialogue5 = f'ยังดีกว่าคนไร้หัวใจ'
dialogue6 = f'เมื่อ {player.name} ปวดร้าวจงเดินเข้าป่า อย่างน้อยก็ไม่ต้องพบเจอคนใจร้ายอย่างเธอ คนที่ไม่มีน้ำใจ ไม่มีเยื่อใยให้คนเคยรักกัน ใจร้ายอย่างเธอ ต้องทิ้งให้อยู่คนเดียวเผื่อเธอเหงาขึ้นมาจะได้กลับมารักกัน'

question1 = f'{player.name} จึงตอบ?'
q1choice1 = f'อยากไปให้ไกล'
q1choice2 = f'อยากเดินเที่ยวป่า'
q1wrong = f'จริงๆ {player.name} ไม่ได้อยากเดินเที่ยวป่า {player.name} อยากไปให้ไกล (-1)'

question2 = f'ถ้า {player.name} เหนื่อยล้าจง?'
q2choice1 = f'เดินเข้าป่า'
q2choice2 = f'เดินกลับบ้าน'
q2wrong = f'{player.name} ไม่ได้อยากเดินกลับบ้าน เพราะ (-1)'

question3 = f'{player.name} จึงตอบว่า?'
q3choice1 = f'ไม่เท่าไร'
q3choice2 = f'กลัวมากๆ'
q3wrong = f'{player.name}ไม่ได้กลัวเลย (-1)'

def main():
    disp_dialogue(dialogue1)
    disp_dialogue(question1)
    q1 = question(q1choice1, q1choice2)
    if q1 == 2:
        disp_dialogue(q1wrong)
        player.damage()
        if player.chance <= 0:
            print('คุณพลาดแล้ว จบเกม')
            keyboard.wait('enter')
            return

    disp_dialogue(dialogue2)
    disp_dialogue(question2)
    q2 = question(q2choice2, q2choice1)
    if q2 == 1:
        disp_dialogue(q2wrong)
        player.damage()
        if player.chance <= 0:
            print('คุณพลาดแล้ว จบเกม')
            keyboard.wait('enter')
            return

    disp_dialogue(dialogue3)
    disp_dialogue(dialogue4)

    disp_dialogue(question3)
    q3 = question(q3choice1, q3choice2)
    if q3 == 2:
        disp_dialogue(q3wrong)
        player.damage()
        if player.chance <= 0:
            print('คุณพลาดแล้ว จบเกม')
            keyboard.wait('enter')
            return

    disp_dialogue(dialogue5)
    disp_dialogue(dialogue6)
    disp_dialogue('ยินดีด้วย จบเกมแล้ว')
    keyboard.wait('enter')

main()