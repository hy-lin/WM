from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
import sys, time, random
import itertools

class SquarePos:
    def __init__(self, position, color, category):
        self.position = position
        self.color = color
        self.category = category #1 or 0
    def draw_cue(self):
        if self.category == 0:
            cir = visual.Circle(WIN, radius = 40, edges = 35, lineWidth = 1)
            cir.setPos(self.position)
            cir.setFillColor('white')
            cir.draw()
        elif self.category == 1:
            dim = visual.Rect(WIN, size=(130,130), ori =45, lineWidth =3 )
            dim.setPos(self.position)
            dim.setFillColor('white')
            dim.draw()
    def set_colors(category):
        selected_colors = sample(COLORS, set_size*2)
        color = list(set(catA_col) + set(catB_col))
        catA_col = selected_colors[:set_size+1] # 0
        catB_col = list(set(selected_colors) - set(catA_col)) #1
        color_new = list(set(COLORS)- set(selected_colors))
        color_postive =[]
        color_intrusion =[]
        if self.category = 0:
            color_postive.append(catA_col)
            color_intrusion.append(catB_col)
        elif self.category = 1:
            color_postive.append(catB_col)
            color_intrusion.append(catA_col)


    def draw_square(self, color=None):
        if color == None:
            color = self.color
        squ = visual.Rect(WIN, size=[110, 110],lineColor = 'white')
        squ.setFillColor(color)
        squ.setPos(self.position)
        squ.draw()
    def determine_cue(self):
        if self.category == 0:
            cir = visual.Circle(WIN, radius = 40, edges = 35, lineWidth = 1)
            cir.setPos([0,0])
            cir.setFillColor('white')
            cir.draw()
        elif self.category == 1:
            dim = visual.Rect(WIN, size=(130,130), ori =45, lineWidth =3 )
            dim.setPos([0,0])
            dim.setFillColor('white')
            dim.draw()
    def draw_res():
        squ = visual.Rect(WIN, size=[110, 110],lineColor = 'white')
        squ.setFillColor(display_color)
        squ.setPos([0,0])
        squ.draw()


def save_ans(rt, ans, stoptime, res, situation,set_size, FEEDBACK,n):
    print(rt, ans, stoptime, res, situation,set_size)
    record = []
    record.append(rt, ans, stoptime, res, situation,set_size,FEEDBACK,n)
    print(record)
    return record

def save_file(record):
     dataFile = open("%s.csv"%(INFO['ID']+'_'+INFO['age']), 'a')
     dataFile.write(INFO['ID']+','+INFO['age']+','+INFO['Block']+','+ INFO['Practice'] +'\n')
     dataFile.write(record)

def get_res(n):
    count = [0]*4
    result = []
    for i in range(n):#n=160
        rand = randint(0,3)
        while count[rand] == n/4:
            rand = randint(0,3)
        count[rand] += 1
        result.append(rand)
    for i in range(n):
        if result[i] == 3:
            result[i] = 0
    return result

def get_setsize(n):
    count = [0]*4
    result = []
    for i in range(n):#n=160
        which_group = randint(0,3)
        count[which_group] += 1
        result.append(which_group+1)
    return result

# def get_cue():
#     num = len(squares_pos)
#     temp_list = [ (x+1) for x in range(num)]
#     A_cue = sample(squares_pos, int(num/2))
#     B_cue = list(set(squares_pos)-set(A_cue))

#     return (A_cue, B_cue)

def run_stage1(squares_pos):
    FIX.draw()
    WIN.flip()
    core.wait(.5)
    for cue in squares_pos:
        cue.draw_cue()
        cue.draw_square()

    WIN.flip()
    stoptime = 2
    core.wait(stoptime)

def get_ans(ans,res):
    feedback = []
    for aws,resp in enumerate(ans,res):
        if ans == 's' and res ==1:
            FEEDBACK_O.draw()
            FEEDBACK.append(1)
        elif ans =='k' and res ==2:
            FEEDBACK_O.draw()
            FEEDBACK.append(1)
        elif ans == 'k' and res ==0:
            FEEDBACK_O.draw()
            FEEDBACK.append(1)
        else:
            FEEDBACK_X.draw()
            FEEDBACK.append(0)
    print(FEEDBACK)
    return FEEDBACK

def run_cue(cue_list, stoptime):
    for cue in cue_list:
        cue.determine_cue()
    WIN.flip()
    core.wait(stoptime)

def run_stage2(cue_list, selected_colors, res):
    target_cue = sample(cue_list, 1)[0]
    SquarePos.set_colors()

    if res == 0: #new
        display_color = sample(color_new,1)[0]
    elif res == 1: #positive
        display_color = sample(color_postive,1)[0]
    else:
        display_color = sample(color_intrusion, 1)[0]
    target_cue.determine_cue()
    target_cue.draw_res(display_color)
    WIN.flip()
    t1 = core.getTime()
    ans = event.waitKeys(keyList=['k', 's'])
    itertools.chain.from_iterable(ans) 
    t2 = core.getTime()
    WIN.flip()

    return (ans, t2-t1)

CASES = [0,1]
WIN = visual.Window((800, 600), color="grey", units="pix")
POSITIONS = [(100, 200), (100, -200), (-100, 200), (200, 100), (200, -100), (-200, 100), (-200, -100), (-100, -200)]
COLORS = [ '#0000FF', '#800080', '#FFC0CB','#FFFF00', '#1E90FF', '#008000', '#A52A2A','#F83759','#FFA500', '#C45366', '#7853C4', '#CFB46F', '#6FCF80']
STOPTIME_LIST = [ sample([0.3, 2],2) for x in range(120)]
RES_LIST = get_res(320)
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.', color = 'white')
FIX = visual.TextStim(WIN, text='+', height=80, color='white', pos=(0, 0))
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.', color = 'white')
FEEDBACK_O = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='Correct.', color = 'white')
FEEDBACK_X = visual.TextStim(WIN, pos=(0, 4), height=30,
text='Wrong.', color = 'white')
INFO = { 'ID': '', 'age': '', 'gender': ['Male', 'Female'],'Practice':['Yes','No']}

gui.DlgFromDict(dictionary=INFO, title='VWM Task', order=['ID', 'age'])

def trial(stoptime, set_size, res):
    cue_category=[[],[]]
    selected_colors = sample(COLORS, set_size*2)
    squares_pos = []

    '''init'''
    for i, pos in enumerate(sample(POSITIONS, set_size*2)):
        color = selected_colors[i]
        category = randint(0,1)
        if len(cue_category[category]) == set_size: #A full or B full
            category = 0 if category == 1 else 1

        squ = SquarePos(pos, color, category)
        squares_pos.append(squ)
        cue_category[category].append(squ)

    run_stage1(squares_pos)
    WIN.flip()
    for i, situation in enumerate(sample(CASES, 2)):
        run_cue(cue_category[situation], stoptime[i])
        WIN.flip()
        (ans, rt) = run_stage2(cue_category[situation], selected_colors, res)
        get_ans(ans,res)
        save_ans(rt=rt, ans=ans, stoptime=stoptime[i], res=res, situation=situation,set_size = set_size, FEEDBACK= FEEDBACK)
        return record


def main():
    ALERT_MSG.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    rounds = 160
    setsize_list = get_setsize(rounds)
    for i in range(rounds):
        trial(STOPTIME_LIST[i], setsize_list[i], RES_LIST[i])
    save_file(record)

def practice():
    def demo():
        rounds = 4
        setsize_list = get_setsize(rounds)
        for i in range(rounds):
            trial(STOPTIME_LIST[i], setsize_list[i], RES_LIST[i])
    ALERT_MSG.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    demo()
    end_demo = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='End of the demo, \nIt is your term now. Press "Space" to practice.', color = 'white')
    end_demo.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    rounds = 12
    setsize_list = get_setsize(rounds)
    for i in range(rounds):
        trial(STOPTIME_LIST[i], setsize_list[i], RES_LIST[i])
main()