#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on 1월 22, 2021, at 13:34
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'movie_w_question_flicker'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\user\\Dropbox\\Exp_Eugene\\subliminal cue\\experiment2\\experiment\\movie_w_question_flicker_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "inst"
instClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='앞으로 30개의 영상들을 보고 감정과 경험에 대한 설문을 하게 됩니다.  \nYou will be watching 30 videos and answering few questions regarding your emotion and experience. \n\n고개가 최대한 움직이지 않게 시청을 해주시기 바랍니다. \nPlease try not to move your head during the experiment.\n\n답변은 모두 키보드로 해주시면 됩니다. \nAll the questions are answered using the keyboard. \n\n우측 방향키(→)를 눌러서 시작해주세요. \nPress right key to proceed.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='우측 방향키(→)를 눌러서 영상을 시작해주세요. \nPress right key (→) to play the video. \n\n다음에 나오는 +에 시선을 집중시켰다가, 영상이 시작되면 자유롭게 시청을 해주세요. \nPlease focus first on the + that will follow. When the video starts, you can watch it freely. ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "focus"
focusClock = core.Clock()
import time
import random
import cv2


thisExp.addData('exp_time', time.time())
thisExp.addData('exp_tick', cv2.getTickCount())
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',units='deg', 
    size=(1,1),
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
#right
loc1 = [16, 2.7]
loc2 = [8, 2.7]
loc3 = [16, 8.1]
loc4 = [8, 8.1]
loc5 = [16, -2.7]
loc6 = [8, -2.7]
loc7 = [16, -8.1]
loc8 = [8, -8.1]
#left
loc9 = [-16, 2.7]
loc10 = [-8, 2.7]
loc11 = [-16, 8.1]
loc12 = [-8, 8.1]
loc13 = [-16, -2.7]
loc14 = [-8, -2.7]
loc15 = [-16, -8.1]
loc16 = [-8, -8.1]

#time
timeset = [1, 2, 3, 4, 5, 0.5, 1.5, 2.5, 3.5, 4.5]

#condition
block = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#block = [0,0,1,1,1]
#random.shuffle(side) #같은 비율 유지 
random.shuffle(block)
right_loc = [loc1, loc2, loc3, loc4, loc5, loc6, loc7, loc8]
left_loc = [loc9, loc10, loc11, loc12, loc13, loc14, loc15, loc16]

cue1 = visual.ImageStim(
    win=win,
    name='cue1', units='deg', 
    image='cue_1.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
cue2 = visual.ImageStim(
    win=win,
    name='cue2', units='deg', 
    image='cue_1.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
cue3 = visual.ImageStim(
    win=win,
    name='cue3', units='deg', 
    image='cue_1.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
cue4 = visual.ImageStim(
    win=win,
    name='cue4', units='deg', 
    image='cue_1.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
cue5 = visual.ImageStim(
    win=win,
    name='cue5', units='deg', 
    image='cue_1.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
cue6 = visual.ImageStim(
    win=win,
    name='cue6', units='deg', 
    image='cue_1.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
cue7 = visual.ImageStim(
    win=win,
    name='cue7', units='deg', 
    image='cue_1.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
cue8 = visual.ImageStim(
    win=win,
    name='cue8', units='deg', 
    image='cue_1.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
cue9 = visual.ImageStim(
    win=win,
    name='cue9', units='deg', 
    image='cue_1.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
cue10 = visual.ImageStim(
    win=win,
    name='cue10', units='deg', 
    image='cue_1.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
cue1_2 = visual.ImageStim(
    win=win,
    name='cue1_2', units='deg', 
    image='cue.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
cue2_2 = visual.ImageStim(
    win=win,
    name='cue2_2', units='deg', 
    image='cue.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
cue3_2 = visual.ImageStim(
    win=win,
    name='cue3_2', units='deg', 
    image='cue.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
cue4_2 = visual.ImageStim(
    win=win,
    name='cue4_2', units='deg', 
    image='cue.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
cue5_2 = visual.ImageStim(
    win=win,
    name='cue5_2', units='deg', 
    image='cue.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
cue6_2 = visual.ImageStim(
    win=win,
    name='cue6_2', units='deg', 
    image='cue.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
cue7_2 = visual.ImageStim(
    win=win,
    name='cue7_2', units='deg', 
    image='cue.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
cue8_2 = visual.ImageStim(
    win=win,
    name='cue8_2', units='deg', 
    image='cue.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
cue9_2 = visual.ImageStim(
    win=win,
    name='cue9_2', units='deg', 
    image='cue.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
cue10_2 = visual.ImageStim(
    win=win,
    name='cue10_2', units='deg', 
    image='cue.png', mask=None,
    ori=0, pos=[0,0], size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)

# Initialize components for Routine "noise"
noiseClock = core.Clock()
noise_2 = visual.NoiseStim(
    win=win, name='noise_2',units='deg', 
    noiseImage=None, mask=None,
    ori=0, pos=(0, 0), size=[48,27], sf=None,
    phase=0.0,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=64, filter=None,
    noiseType='Binary', noiseElementSize=0.1, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-1.0)
noise_2.buildNoise()

# Initialize components for Routine "q_like"
q_likeClock = core.Clock()
key_resp_ans = keyboard.Keyboard()
q1 = visual.TextStim(win=win, name='q1',
    text='영상이 좋으셨나요? Did you like the video?',
    font='Arial',
    pos=(0, 0.09), height=0.025, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
space = visual.TextStim(win=win, name='space',
    text="답변이 끝나면 아래방향키(↓)를 눌러서 넘어가주세요.\nif you are done with your choice, please press 'down(↓)' to proceed.\n\n답변 예시 : 1 = 키보드 키 '1'\ne.g. : 1 = keyboard key '1'",
    font='Arial',
    pos=(0, -0.06), height=0.02, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
scale = visual.TextStim(win=win, name='scale',
    text='좋지 않았다(did not like) = 1/ 중립(neutral) = 3 / 좋았다(liked) = 5',
    font='Arial',
    pos=(0, 0.04), height=0.02, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
slider = visual.Slider(win=win, name='slider',
    size=(1.0, 0.05), pos=(0, -0.3), units=None,
    labels=(1, 2, 3, 4, 5), ticks=(1, 2, 3, 4, 5),
    granularity=0, style=['rating'],
    color='LightGray', font='HelveticaBold',
    flip=False, depth=-5)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "q_str"
q_strClock = core.Clock()
q_strange = visual.TextStim(win=win, name='q_strange',
    text='영상에 이상한 부분이 있었나요? \nDid you notice anything strange from the video?\n\n(대칭으로 인한 이상함 제외)\n(ignore the strangeness that comes from the symmetricity)',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space_2 = visual.TextStim(win=win, name='space_2',
    text="'y' or 'n'",
    font='Arial',
    pos=(0, -0.1), height=0.02, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_yes = keyboard.Keyboard()

# Initialize components for Routine "strange"
strangeClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='deg', 
    image='question.png', mask=None,
    ori=0, pos=(0, 8), size=[16, 9],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text="1 과 2 중에 좀더 이상하다고 느낀 쪽을 골라주세요. \nWhich area felt 'more' strange to you? (between 1 and 2)\n(대칭 형태로 인한 이상함 제외)\n(ignore the strangeness from the symmetricity)\n\n답변이 끝나면 아래방향키(↓)를 눌러서 넘어가주세요.\nif you are done with your choice, please press 'down(↓)' to proceed",
    font='Arial',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_num = keyboard.Keyboard()
slider_2 = visual.Slider(win=win, name='slider_2',
    size=(1.0, 0.05), pos=(0, -0.3), units=None,
    labels=(1, 2), ticks=(1, 2),
    granularity=0, style=['rating'],
    color='LightGray', font='HelveticaBold',
    flip=False, depth=-4)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "dis"
disClock = core.Clock()
key_dis = keyboard.Keyboard()
text_7 = visual.TextStim(win=win, name='text_7',
    text="앞에 대답한 '이상함'이 영상 시청 경험에 방해가 되었나요?\nDid the 'strangeness' disturb your watching experience?\n\n1 = 방해가 되지 않음, 5 = 매우 방해 됨\n1 = was not disturbing, 5 = was very disturbing\n\n답변이 끝나면 아래방향키(↓)를 눌러서 넘어가주세요.\nif you are done with your choice, please press 'down(↓)' to proceed",
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_5 = keyboard.Keyboard()
slider_d = visual.Slider(win=win, name='slider_d',
    size=(1.0, 0.05), pos=(0, -0.3), units=None,
    labels=(1, 2, 3, 4, 5), ticks=(1, 2, 3, 4, 5),
    granularity=0, style=['rating'],
    color='LightGray', font='HelveticaBold',
    flip=False, depth=-4)

# Initialize components for Routine "question_2"
question_2Clock = core.Clock()
key_resp_ans_2 = keyboard.Keyboard()
question1 = visual.TextStim(win=win, name='question1',
    text='default text',
    font='Arial',
    pos=(0, 0.09), height=0.025, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text="답변이 끝나면 아래방향키(↓)를 눌러서 넘어가주세요.\nif you are done with your choice, please press 'down(↓)' to proceed.\n\n답변 예시 : 1 = 키보드 키 '1'\ne.g. : 1 = keyboard key '1'",
    font='Arial',
    pos=(0, -0.06), height=0.02, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font='Arial',
    pos=(0, 0.04), height=0.02, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_space_2 = keyboard.Keyboard()
slider_4 = visual.Slider(win=win, name='slider_4',
    size=(1.0, 0.05), pos=(0, -0.3), units=None,
    labels=(1, 2, 3, 4, 5), ticks=(1, 2, 3, 4, 5),
    granularity=0, style=['rating'],
    color='LightGray', font='HelveticaBold',
    flip=False, depth=-6)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='수고하셨습니다 :) \n\n실험이 완료 되었습니다. \n\n실험실을 나가셔도 됩니다. ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "inst"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instComponents = [text_2, key_resp_2]
for thisComponent in instComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inst"-------
while continueRoutine:
    # get current time
    t = instClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst"-------
for thisComponent in instComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "inst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('new_condition.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    break_2Components = [text, key_resp]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "break_2"-------
    while continueRoutine:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "focus"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    thisExp.addData('focus_tick', cv2.getTickCount())
    # keep track of which components have finished
    focusComponents = [polygon]
    for thisComponent in focusComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    focusClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "focus"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = focusClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=focusClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in focusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "focus"-------
    for thisComponent in focusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon.started', polygon.tStartRefresh)
    trials.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('movie_time', time.time())
    thisExp.addData('movie_tick', cv2.getTickCount())
    
    random.shuffle(left_loc)
    random.shuffle(right_loc)
    random.shuffle(timeset)
    
    opacity = 0.15
    cue = 0.008
    
    pos1 = [0,0]
    pos2 = [0,0]
    pos3 = [0,0]
    pos4 = [0,0]
    pos5 = [0,0]
    pos6 = [0,0]
    pos7 = [0,0]
    pos8 = [0,0]
    pos9 = [0,0]
    pos10 = [0,0]
    
    starttime = 0
    num = trials.thisN
    side = [0, 1]
    side2 = random.choices(side, weights = (50, 50), k = 1)
    side_rec = ''
    if block[num] == 0:
        cue = 0
        opacity = 0
        side_rec = 'none'
        thisExp.addData('side', side_rec)
    
    elif block[num] == 1:
        
        if side2[0] == 0: #left 80%, right 20% 
            pos1 = left_loc[0]
            pos2 = left_loc[1]
            pos3 = left_loc[2]
            pos4 = left_loc[3]
            pos5 = left_loc[4]
            pos6 = left_loc[5]
            pos7 = left_loc[6]
            pos8 = left_loc[7]
            pos9 = right_loc[0]
            pos10 = right_loc[1]
            #record side
            side_rec = 'left'
            thisExp.addData('side', side_rec)
            
            
        elif side2[0] == 1:  #left 20%, right 80% 
            pos1 = right_loc[0]
            pos2 = right_loc[1]
            pos3 = right_loc[2]
            pos4 = right_loc[3]
            pos5 = right_loc[4]
            pos6 = right_loc[5]
            pos7 = right_loc[6]
            pos8 = right_loc[7]
            pos9 = left_loc[0]
            pos10 = left_loc[1]
            
            #record side
            side_rec = 'right'
            thisExp.addData('side', side_rec)
    
    #time
    t1 = starttime + timeset[0]
    t2 = t1 + timeset[1]
    t3 = t2 + timeset[2]
    t4 = t3 + timeset[3]
    t5 = t4 + timeset[4]
    t6 = t5 + timeset[5]
    t7 = t6 + timeset[6]
    t8 = t7 + timeset[7]
    t9 = t8 + timeset[8]
    t10 = t9 + timeset[9]
    
    timeorder = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
    
    shuffle(timeorder)
    
    time1 = timeorder[0]
    time2 = timeorder[1]
    time3 = timeorder[2]
    time4 = timeorder[3]
    time5 = timeorder[4]
    time6 = timeorder[5]
    time7 = timeorder[6]
    time8 = timeorder[7]
    time9 = timeorder[8]
    time10 = timeorder[9]
        
        
    #add data position of cue
    thisExp.addData('pos1', pos1)
    thisExp.addData('pos2', pos2)
    thisExp.addData('pos3', pos3)
    thisExp.addData('pos4', pos4)
    thisExp.addData('pos5', pos5)
    thisExp.addData('pos6', pos6)
    thisExp.addData('pos7', pos7)
    thisExp.addData('pos8', pos8)
    thisExp.addData('pos9', pos9)
    thisExp.addData('pos10', pos10)
    thisExp.addData('opacity', opacity)
    thisExp.addData('cue', cue)
    movie = visual.MovieStim3(
        win=win, name='movie',units='deg', 
        noAudio = True,
        filename=video,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        size=[48,27],
        depth=-1.0,
        )
    cue1.setOpacity(opacity)
    cue1.setPos(pos1)
    cue2.setOpacity(opacity)
    cue2.setPos(pos2)
    cue3.setOpacity(opacity)
    cue3.setPos(pos3)
    cue4.setOpacity(opacity)
    cue4.setPos(pos4)
    cue5.setOpacity(opacity)
    cue5.setPos(pos5)
    cue6.setOpacity(opacity)
    cue6.setPos(pos6)
    cue7.setOpacity(opacity)
    cue7.setPos(pos7)
    cue8.setOpacity(opacity)
    cue8.setPos(pos8)
    cue9.setOpacity(opacity)
    cue9.setPos(pos9)
    cue10.setOpacity(opacity)
    cue10.setPos(pos10)
    cue1_2.setOpacity(opacity)
    cue1_2.setPos(pos1)
    cue2_2.setOpacity(opacity)
    cue2_2.setPos(pos2)
    cue3_2.setOpacity(opacity)
    cue3_2.setPos(pos3)
    cue4_2.setOpacity(opacity)
    cue4_2.setPos(pos4)
    cue5_2.setOpacity(opacity)
    cue5_2.setPos(pos5)
    cue6_2.setOpacity(opacity)
    cue6_2.setPos(pos6)
    cue7_2.setOpacity(opacity)
    cue7_2.setPos(pos7)
    cue8_2.setOpacity(opacity)
    cue8_2.setPos(pos8)
    cue9_2.setOpacity(opacity)
    cue9_2.setPos(pos9)
    cue10_2.setOpacity(opacity)
    cue10_2.setPos(pos10)
    # keep track of which components have finished
    trialComponents = [movie, cue1, cue2, cue3, cue4, cue5, cue6, cue7, cue8, cue9, cue10, cue1_2, cue2_2, cue3_2, cue4_2, cue5_2, cue6_2, cue7_2, cue8_2, cue9_2, cue10_2]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #add data time of cue 
        if cue1.status == STARTED:
            thisExp.addData('cue1_time', cv2.getTickCount())
        if cue2.status == STARTED:
            thisExp.addData('cue2_time', cv2.getTickCount())
        if cue3.status == STARTED:
            thisExp.addData('cue3_time', cv2.getTickCount())
        if cue4.status == STARTED:
            thisExp.addData('cue4_time', cv2.getTickCount())
        if cue5.status == STARTED:
            thisExp.addData('cue5_time', cv2.getTickCount())
        if cue6.status == STARTED:
            thisExp.addData('cue6_time', cv2.getTickCount())
        if cue7.status == STARTED:
            thisExp.addData('cue7_time', cv2.getTickCount())
        if cue8.status == STARTED:
            thisExp.addData('cue8_time', cv2.getTickCount())
        if cue9.status == STARTED:
            thisExp.addData('cue9_time', cv2.getTickCount())
        if cue10.status == STARTED:
            thisExp.addData('cue10_time', cv2.getTickCount())
        
        if cue1.status == FINISHED:
            thisExp.addData('cue1_end', cv2.getTickCount())
        if cue2.status == FINISHED:
            thisExp.addData('cue2_end', cv2.getTickCount())
        if cue3.status == FINISHED:
            thisExp.addData('cue3_end', cv2.getTickCount())
        if cue4.status == FINISHED:
            thisExp.addData('cue4_end', cv2.getTickCount())
        if cue5.status == FINISHED:
            thisExp.addData('cue5_end', cv2.getTickCount())
        if cue6.status == FINISHED:
            thisExp.addData('cue6_end', cv2.getTickCount())
        if cue7.status == FINISHED:
            thisExp.addData('cue7_end', cv2.getTickCount())
        if cue8.status == FINISHED:
            thisExp.addData('cue8_end', cv2.getTickCount())
        if cue9.status == FINISHED:
            thisExp.addData('cue9_end', cv2.getTickCount())
        if cue10.status == FINISHED:
            thisExp.addData('cue10_end', cv2.getTickCount())
            
        if cue1_2.status == STARTED:
            thisExp.addData('cue1_2', cv2.getTickCount())
        if cue2_2.status == STARTED:
            thisExp.addData('cue2_2', cv2.getTickCount())
        if cue3_2.status == STARTED:
            thisExp.addData('cue3_2', cv2.getTickCount())
        if cue4_2.status == STARTED:
            thisExp.addData('cue4_2', cv2.getTickCount())
        if cue5_2.status == STARTED:
            thisExp.addData('cue5_2', cv2.getTickCount())
        if cue6_2.status == STARTED:
            thisExp.addData('cue6_2', cv2.getTickCount())
        if cue7_2.status == STARTED:
            thisExp.addData('cue7_2', cv2.getTickCount())
        if cue8_2.status == STARTED:
            thisExp.addData('cue8_2', cv2.getTickCount())
        if cue9_2.status == STARTED:
            thisExp.addData('cue9_2', cv2.getTickCount())
        if cue10_2.status == STARTED:
            thisExp.addData('cue10_2', cv2.getTickCount())
        
        if cue1_2.status == FINISHED:
            thisExp.addData('cue1_2_end', cv2.getTickCount())
        if cue2_2.status == FINISHED:
            thisExp.addData('cue2_2_end', cv2.getTickCount())
        if cue3_2.status == FINISHED:
            thisExp.addData('cue3_2_end', cv2.getTickCount())
        if cue4_2.status == FINISHED:
            thisExp.addData('cue4_2_end', cv2.getTickCount())
        if cue5_2.status == FINISHED:
            thisExp.addData('cue5_2_end', cv2.getTickCount())
        if cue6_2.status == FINISHED:
            thisExp.addData('cue6_2_end', cv2.getTickCount())
        if cue7_2.status == FINISHED:
            thisExp.addData('cue7_2_end', cv2.getTickCount())
        if cue8_2.status == FINISHED:
            thisExp.addData('cue8_2_end', cv2.getTickCount())
        if cue9_2.status == FINISHED:
            thisExp.addData('cue9_2_end', cv2.getTickCount())
        if cue10_2.status == FINISHED:
            thisExp.addData('cue10_2_end', cv2.getTickCount())
        
        # *movie* updates
        if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            movie.frameNStart = frameN  # exact frame index
            movie.tStart = t  # local t and not account for scr refresh
            movie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
            movie.setAutoDraw(True)
        if movie.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > movie.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                movie.tStop = t  # not accounting for scr refresh
                movie.frameNStop = frameN  # exact frame index
                win.timeOnFlip(movie, 'tStopRefresh')  # time at next scr refresh
                movie.setAutoDraw(False)
        
        # *cue1* updates
        if cue1.status == NOT_STARTED and tThisFlip >= time1-frameTolerance:
            # keep track of start time/frame for later
            cue1.frameNStart = frameN  # exact frame index
            cue1.tStart = t  # local t and not account for scr refresh
            cue1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue1, 'tStartRefresh')  # time at next scr refresh
            cue1.setAutoDraw(True)
        if cue1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue1.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue1.tStop = t  # not accounting for scr refresh
                cue1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue1, 'tStopRefresh')  # time at next scr refresh
                cue1.setAutoDraw(False)
        
        # *cue2* updates
        if cue2.status == NOT_STARTED and tThisFlip >= time2-frameTolerance:
            # keep track of start time/frame for later
            cue2.frameNStart = frameN  # exact frame index
            cue2.tStart = t  # local t and not account for scr refresh
            cue2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue2, 'tStartRefresh')  # time at next scr refresh
            cue2.setAutoDraw(True)
        if cue2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue2.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue2.tStop = t  # not accounting for scr refresh
                cue2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue2, 'tStopRefresh')  # time at next scr refresh
                cue2.setAutoDraw(False)
        
        # *cue3* updates
        if cue3.status == NOT_STARTED and tThisFlip >= time3-frameTolerance:
            # keep track of start time/frame for later
            cue3.frameNStart = frameN  # exact frame index
            cue3.tStart = t  # local t and not account for scr refresh
            cue3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue3, 'tStartRefresh')  # time at next scr refresh
            cue3.setAutoDraw(True)
        if cue3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue3.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue3.tStop = t  # not accounting for scr refresh
                cue3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue3, 'tStopRefresh')  # time at next scr refresh
                cue3.setAutoDraw(False)
        
        # *cue4* updates
        if cue4.status == NOT_STARTED and tThisFlip >= time4-frameTolerance:
            # keep track of start time/frame for later
            cue4.frameNStart = frameN  # exact frame index
            cue4.tStart = t  # local t and not account for scr refresh
            cue4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue4, 'tStartRefresh')  # time at next scr refresh
            cue4.setAutoDraw(True)
        if cue4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue4.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue4.tStop = t  # not accounting for scr refresh
                cue4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue4, 'tStopRefresh')  # time at next scr refresh
                cue4.setAutoDraw(False)
        
        # *cue5* updates
        if cue5.status == NOT_STARTED and tThisFlip >= time5-frameTolerance:
            # keep track of start time/frame for later
            cue5.frameNStart = frameN  # exact frame index
            cue5.tStart = t  # local t and not account for scr refresh
            cue5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue5, 'tStartRefresh')  # time at next scr refresh
            cue5.setAutoDraw(True)
        if cue5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue5.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue5.tStop = t  # not accounting for scr refresh
                cue5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue5, 'tStopRefresh')  # time at next scr refresh
                cue5.setAutoDraw(False)
        
        # *cue6* updates
        if cue6.status == NOT_STARTED and tThisFlip >= time6-frameTolerance:
            # keep track of start time/frame for later
            cue6.frameNStart = frameN  # exact frame index
            cue6.tStart = t  # local t and not account for scr refresh
            cue6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue6, 'tStartRefresh')  # time at next scr refresh
            cue6.setAutoDraw(True)
        if cue6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue6.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue6.tStop = t  # not accounting for scr refresh
                cue6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue6, 'tStopRefresh')  # time at next scr refresh
                cue6.setAutoDraw(False)
        
        # *cue7* updates
        if cue7.status == NOT_STARTED and tThisFlip >= time7-frameTolerance:
            # keep track of start time/frame for later
            cue7.frameNStart = frameN  # exact frame index
            cue7.tStart = t  # local t and not account for scr refresh
            cue7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue7, 'tStartRefresh')  # time at next scr refresh
            cue7.setAutoDraw(True)
        if cue7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue7.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue7.tStop = t  # not accounting for scr refresh
                cue7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue7, 'tStopRefresh')  # time at next scr refresh
                cue7.setAutoDraw(False)
        
        # *cue8* updates
        if cue8.status == NOT_STARTED and tThisFlip >= time8-frameTolerance:
            # keep track of start time/frame for later
            cue8.frameNStart = frameN  # exact frame index
            cue8.tStart = t  # local t and not account for scr refresh
            cue8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue8, 'tStartRefresh')  # time at next scr refresh
            cue8.setAutoDraw(True)
        if cue8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue8.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue8.tStop = t  # not accounting for scr refresh
                cue8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue8, 'tStopRefresh')  # time at next scr refresh
                cue8.setAutoDraw(False)
        
        # *cue9* updates
        if cue9.status == NOT_STARTED and tThisFlip >= time9-frameTolerance:
            # keep track of start time/frame for later
            cue9.frameNStart = frameN  # exact frame index
            cue9.tStart = t  # local t and not account for scr refresh
            cue9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue9, 'tStartRefresh')  # time at next scr refresh
            cue9.setAutoDraw(True)
        if cue9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue9.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue9.tStop = t  # not accounting for scr refresh
                cue9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue9, 'tStopRefresh')  # time at next scr refresh
                cue9.setAutoDraw(False)
        
        # *cue10* updates
        if cue10.status == NOT_STARTED and tThisFlip >= time10-frameTolerance:
            # keep track of start time/frame for later
            cue10.frameNStart = frameN  # exact frame index
            cue10.tStart = t  # local t and not account for scr refresh
            cue10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue10, 'tStartRefresh')  # time at next scr refresh
            cue10.setAutoDraw(True)
        if cue10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue10.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue10.tStop = t  # not accounting for scr refresh
                cue10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue10, 'tStopRefresh')  # time at next scr refresh
                cue10.setAutoDraw(False)
        
        # *cue1_2* updates
        if cue1_2.status == NOT_STARTED and cue1.status == FINISHED:
            # keep track of start time/frame for later
            cue1_2.frameNStart = frameN  # exact frame index
            cue1_2.tStart = t  # local t and not account for scr refresh
            cue1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue1_2, 'tStartRefresh')  # time at next scr refresh
            cue1_2.setAutoDraw(True)
        if cue1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue1_2.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue1_2.tStop = t  # not accounting for scr refresh
                cue1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue1_2, 'tStopRefresh')  # time at next scr refresh
                cue1_2.setAutoDraw(False)
        
        # *cue2_2* updates
        if cue2_2.status == NOT_STARTED and cue2.status == FINISHED:
            # keep track of start time/frame for later
            cue2_2.frameNStart = frameN  # exact frame index
            cue2_2.tStart = t  # local t and not account for scr refresh
            cue2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue2_2, 'tStartRefresh')  # time at next scr refresh
            cue2_2.setAutoDraw(True)
        if cue2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue2_2.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue2_2.tStop = t  # not accounting for scr refresh
                cue2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue2_2, 'tStopRefresh')  # time at next scr refresh
                cue2_2.setAutoDraw(False)
        
        # *cue3_2* updates
        if cue3_2.status == NOT_STARTED and cue3.status == FINISHED:
            # keep track of start time/frame for later
            cue3_2.frameNStart = frameN  # exact frame index
            cue3_2.tStart = t  # local t and not account for scr refresh
            cue3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue3_2, 'tStartRefresh')  # time at next scr refresh
            cue3_2.setAutoDraw(True)
        if cue3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue3_2.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue3_2.tStop = t  # not accounting for scr refresh
                cue3_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue3_2, 'tStopRefresh')  # time at next scr refresh
                cue3_2.setAutoDraw(False)
        
        # *cue4_2* updates
        if cue4_2.status == NOT_STARTED and cue4.status == FINISHED:
            # keep track of start time/frame for later
            cue4_2.frameNStart = frameN  # exact frame index
            cue4_2.tStart = t  # local t and not account for scr refresh
            cue4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue4_2, 'tStartRefresh')  # time at next scr refresh
            cue4_2.setAutoDraw(True)
        if cue4_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue4_2.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue4_2.tStop = t  # not accounting for scr refresh
                cue4_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue4_2, 'tStopRefresh')  # time at next scr refresh
                cue4_2.setAutoDraw(False)
        
        # *cue5_2* updates
        if cue5_2.status == NOT_STARTED and cue5.status == FINISHED:
            # keep track of start time/frame for later
            cue5_2.frameNStart = frameN  # exact frame index
            cue5_2.tStart = t  # local t and not account for scr refresh
            cue5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue5_2, 'tStartRefresh')  # time at next scr refresh
            cue5_2.setAutoDraw(True)
        if cue5_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue5_2.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue5_2.tStop = t  # not accounting for scr refresh
                cue5_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue5_2, 'tStopRefresh')  # time at next scr refresh
                cue5_2.setAutoDraw(False)
        
        # *cue6_2* updates
        if cue6_2.status == NOT_STARTED and cue6.status == FINISHED:
            # keep track of start time/frame for later
            cue6_2.frameNStart = frameN  # exact frame index
            cue6_2.tStart = t  # local t and not account for scr refresh
            cue6_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue6_2, 'tStartRefresh')  # time at next scr refresh
            cue6_2.setAutoDraw(True)
        if cue6_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue6_2.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue6_2.tStop = t  # not accounting for scr refresh
                cue6_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue6_2, 'tStopRefresh')  # time at next scr refresh
                cue6_2.setAutoDraw(False)
        
        # *cue7_2* updates
        if cue7_2.status == NOT_STARTED and cue7.status == FINISHED:
            # keep track of start time/frame for later
            cue7_2.frameNStart = frameN  # exact frame index
            cue7_2.tStart = t  # local t and not account for scr refresh
            cue7_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue7_2, 'tStartRefresh')  # time at next scr refresh
            cue7_2.setAutoDraw(True)
        if cue7_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue7_2.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue7_2.tStop = t  # not accounting for scr refresh
                cue7_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue7_2, 'tStopRefresh')  # time at next scr refresh
                cue7_2.setAutoDraw(False)
        
        # *cue8_2* updates
        if cue8_2.status == NOT_STARTED and cue8.status == FINISHED:
            # keep track of start time/frame for later
            cue8_2.frameNStart = frameN  # exact frame index
            cue8_2.tStart = t  # local t and not account for scr refresh
            cue8_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue8_2, 'tStartRefresh')  # time at next scr refresh
            cue8_2.setAutoDraw(True)
        if cue8_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue8_2.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue8_2.tStop = t  # not accounting for scr refresh
                cue8_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue8_2, 'tStopRefresh')  # time at next scr refresh
                cue8_2.setAutoDraw(False)
        
        # *cue9_2* updates
        if cue9_2.status == NOT_STARTED and cue9.status == FINISHED:
            # keep track of start time/frame for later
            cue9_2.frameNStart = frameN  # exact frame index
            cue9_2.tStart = t  # local t and not account for scr refresh
            cue9_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue9_2, 'tStartRefresh')  # time at next scr refresh
            cue9_2.setAutoDraw(True)
        if cue9_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue9_2.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue9_2.tStop = t  # not accounting for scr refresh
                cue9_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue9_2, 'tStopRefresh')  # time at next scr refresh
                cue9_2.setAutoDraw(False)
        
        # *cue10_2* updates
        if cue10_2.status == NOT_STARTED and cue10.status == FINISHED:
            # keep track of start time/frame for later
            cue10_2.frameNStart = frameN  # exact frame index
            cue10_2.tStart = t  # local t and not account for scr refresh
            cue10_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue10_2, 'tStartRefresh')  # time at next scr refresh
            cue10_2.setAutoDraw(True)
        if cue10_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue10_2.tStartRefresh + cue-frameTolerance:
                # keep track of stop time/frame for later
                cue10_2.tStop = t  # not accounting for scr refresh
                cue10_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue10_2, 'tStopRefresh')  # time at next scr refresh
                cue10_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('movie_endtime', cv2.getTickCount())
    movie.stop()
    trials.addData('cue1.started', cue1.tStartRefresh)
    trials.addData('cue1.stopped', cue1.tStopRefresh)
    trials.addData('cue2.started', cue2.tStartRefresh)
    trials.addData('cue2.stopped', cue2.tStopRefresh)
    trials.addData('cue3.started', cue3.tStartRefresh)
    trials.addData('cue3.stopped', cue3.tStopRefresh)
    trials.addData('cue4.started', cue4.tStartRefresh)
    trials.addData('cue4.stopped', cue4.tStopRefresh)
    trials.addData('cue5.started', cue5.tStartRefresh)
    trials.addData('cue5.stopped', cue5.tStopRefresh)
    trials.addData('cue6.started', cue6.tStartRefresh)
    trials.addData('cue6.stopped', cue6.tStopRefresh)
    trials.addData('cue7.started', cue7.tStartRefresh)
    trials.addData('cue7.stopped', cue7.tStopRefresh)
    trials.addData('cue8.started', cue8.tStartRefresh)
    trials.addData('cue8.stopped', cue8.tStopRefresh)
    trials.addData('cue9.started', cue9.tStartRefresh)
    trials.addData('cue9.stopped', cue9.tStopRefresh)
    trials.addData('cue10.started', cue10.tStartRefresh)
    trials.addData('cue10.stopped', cue10.tStopRefresh)
    trials.addData('cue1_2.started', cue1_2.tStartRefresh)
    trials.addData('cue1_2.stopped', cue1_2.tStopRefresh)
    trials.addData('cue2_2.started', cue2_2.tStartRefresh)
    trials.addData('cue2_2.stopped', cue2_2.tStopRefresh)
    trials.addData('cue3_2.started', cue3_2.tStartRefresh)
    trials.addData('cue3_2.stopped', cue3_2.tStopRefresh)
    trials.addData('cue4_2.started', cue4_2.tStartRefresh)
    trials.addData('cue4_2.stopped', cue4_2.tStopRefresh)
    trials.addData('cue5_2.started', cue5_2.tStartRefresh)
    trials.addData('cue5_2.stopped', cue5_2.tStopRefresh)
    trials.addData('cue6_2.started', cue6_2.tStartRefresh)
    trials.addData('cue6_2.stopped', cue6_2.tStopRefresh)
    trials.addData('cue7_2.started', cue7_2.tStartRefresh)
    trials.addData('cue7_2.stopped', cue7_2.tStopRefresh)
    trials.addData('cue8_2.started', cue8_2.tStartRefresh)
    trials.addData('cue8_2.stopped', cue8_2.tStopRefresh)
    trials.addData('cue9_2.started', cue9_2.tStartRefresh)
    trials.addData('cue9_2.stopped', cue9_2.tStopRefresh)
    trials.addData('cue10_2.started', cue10_2.tStartRefresh)
    trials.addData('cue10_2.stopped', cue10_2.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "noise"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    thisExp.addData('noise_tick', cv2.getTickCount())
    thisExp.addData('noise_time', time.time())
    # keep track of which components have finished
    noiseComponents = [noise_2]
    for thisComponent in noiseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    noiseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "noise"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = noiseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=noiseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *noise_2* updates
        if noise_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            noise_2.frameNStart = frameN  # exact frame index
            noise_2.tStart = t  # local t and not account for scr refresh
            noise_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise_2, 'tStartRefresh')  # time at next scr refresh
            noise_2.setAutoDraw(True)
        if noise_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noise_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                noise_2.tStop = t  # not accounting for scr refresh
                noise_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noise_2, 'tStopRefresh')  # time at next scr refresh
                noise_2.setAutoDraw(False)
        if noise_2.status == STARTED:
            if noise_2._needBuild:
                noise_2.buildNoise()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in noiseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "noise"-------
    for thisComponent in noiseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('noise_2.started', noise_2.tStartRefresh)
    trials.addData('noise_2.stopped', noise_2.tStopRefresh)
    
    # ------Prepare to start Routine "q_like"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_ans.keys = []
    key_resp_ans.rt = []
    _key_resp_ans_allKeys = []
    slider.reset()
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    q_likeComponents = [key_resp_ans, q1, space, scale, slider, key_resp_4]
    for thisComponent in q_likeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    q_likeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "q_like"-------
    while continueRoutine:
        # get current time
        t = q_likeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=q_likeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if key_resp_ans.keys == '1':
            slider.markerPos = 1
        elif key_resp_ans.keys == '2':
            slider.markerPos = 2
        elif key_resp_ans.keys == '3':
            slider.markerPos = 3
        elif key_resp_ans.keys == '4':
            slider.markerPos = 4
        elif key_resp_ans.keys == '5':
            slider.markerPos = 5
        
        # *key_resp_ans* updates
        waitOnFlip = False
        if key_resp_ans.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_ans.frameNStart = frameN  # exact frame index
            key_resp_ans.tStart = t  # local t and not account for scr refresh
            key_resp_ans.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_ans, 'tStartRefresh')  # time at next scr refresh
            key_resp_ans.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_ans.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_ans.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_ans.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_ans.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _key_resp_ans_allKeys.extend(theseKeys)
            if len(_key_resp_ans_allKeys):
                key_resp_ans.keys = _key_resp_ans_allKeys[-1].name  # just the last key pressed
                key_resp_ans.rt = _key_resp_ans_allKeys[-1].rt
        
        # *q1* updates
        if q1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            q1.frameNStart = frameN  # exact frame index
            q1.tStart = t  # local t and not account for scr refresh
            q1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(q1, 'tStartRefresh')  # time at next scr refresh
            q1.setAutoDraw(True)
        
        # *space* updates
        if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space.frameNStart = frameN  # exact frame index
            space.tStart = t  # local t and not account for scr refresh
            space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space, 'tStartRefresh')  # time at next scr refresh
            space.setAutoDraw(True)
        
        # *scale* updates
        if scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scale.frameNStart = frameN  # exact frame index
            scale.tStart = t  # local t and not account for scr refresh
            scale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scale, 'tStartRefresh')  # time at next scr refresh
            scale.setAutoDraw(True)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['down'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in q_likeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "q_like"-------
    for thisComponent in q_likeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_ans.keys in ['', [], None]:  # No response was made
        key_resp_ans.keys = None
    trials.addData('key_resp_ans.keys',key_resp_ans.keys)
    if key_resp_ans.keys != None:  # we had a response
        trials.addData('key_resp_ans.rt', key_resp_ans.rt)
    trials.addData('key_resp_ans.started', key_resp_ans.tStartRefresh)
    trials.addData('key_resp_ans.stopped', key_resp_ans.tStopRefresh)
    trials.addData('q1.started', q1.tStartRefresh)
    trials.addData('q1.stopped', q1.tStopRefresh)
    trials.addData('space.started', space.tStartRefresh)
    trials.addData('space.stopped', space.tStopRefresh)
    trials.addData('scale.started', scale.tStartRefresh)
    trials.addData('scale.stopped', scale.tStopRefresh)
    trials.addData('slider.response', slider.getRating())
    trials.addData('slider.rt', slider.getRT())
    trials.addData('slider.started', slider.tStartRefresh)
    trials.addData('slider.stopped', slider.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "q_like" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "q_str"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_yes.keys = []
    key_resp_yes.rt = []
    _key_resp_yes_allKeys = []
    # keep track of which components have finished
    q_strComponents = [q_strange, space_2, key_resp_yes]
    for thisComponent in q_strComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    q_strClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "q_str"-------
    while continueRoutine:
        # get current time
        t = q_strClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=q_strClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *q_strange* updates
        if q_strange.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            q_strange.frameNStart = frameN  # exact frame index
            q_strange.tStart = t  # local t and not account for scr refresh
            q_strange.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(q_strange, 'tStartRefresh')  # time at next scr refresh
            q_strange.setAutoDraw(True)
        
        # *space_2* updates
        if space_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_2.frameNStart = frameN  # exact frame index
            space_2.tStart = t  # local t and not account for scr refresh
            space_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_2, 'tStartRefresh')  # time at next scr refresh
            space_2.setAutoDraw(True)
        
        # *key_resp_yes* updates
        waitOnFlip = False
        if key_resp_yes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_yes.frameNStart = frameN  # exact frame index
            key_resp_yes.tStart = t  # local t and not account for scr refresh
            key_resp_yes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_yes, 'tStartRefresh')  # time at next scr refresh
            key_resp_yes.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_yes.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_yes.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_yes.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_yes.getKeys(keyList=['y', 'n'], waitRelease=False)
            _key_resp_yes_allKeys.extend(theseKeys)
            if len(_key_resp_yes_allKeys):
                key_resp_yes.keys = _key_resp_yes_allKeys[-1].name  # just the last key pressed
                key_resp_yes.rt = _key_resp_yes_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in q_strComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "q_str"-------
    for thisComponent in q_strComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('q_strange.started', q_strange.tStartRefresh)
    trials.addData('q_strange.stopped', q_strange.tStopRefresh)
    trials.addData('space_2.started', space_2.tStartRefresh)
    trials.addData('space_2.stopped', space_2.tStopRefresh)
    # check responses
    if key_resp_yes.keys in ['', [], None]:  # No response was made
        key_resp_yes.keys = None
    trials.addData('key_resp_yes.keys',key_resp_yes.keys)
    if key_resp_yes.keys != None:  # we had a response
        trials.addData('key_resp_yes.rt', key_resp_yes.rt)
    trials.addData('key_resp_yes.started', key_resp_yes.tStartRefresh)
    trials.addData('key_resp_yes.stopped', key_resp_yes.tStopRefresh)
    # the Routine "q_str" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "strange"-------
    continueRoutine = True
    # update component parameters for each repeat
    # only run the routine if the response was a 1:
    if key_resp_yes.keys == 'n':
        continueRoutine = False # don't even start this routine
    key_resp_num.keys = []
    key_resp_num.rt = []
    _key_resp_num_allKeys = []
    slider_2.reset()
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    strangeComponents = [image, text_4, key_resp_num, slider_2, key_resp_3]
    for thisComponent in strangeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    strangeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "strange"-------
    while continueRoutine:
        # get current time
        t = strangeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=strangeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if key_resp_num.keys == '1':
            slider_2.markerPos = 1
        elif key_resp_num.keys == '2':
            slider_2.markerPos = 2
        
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        
        # *key_resp_num* updates
        waitOnFlip = False
        if key_resp_num.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_num.frameNStart = frameN  # exact frame index
            key_resp_num.tStart = t  # local t and not account for scr refresh
            key_resp_num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_num, 'tStartRefresh')  # time at next scr refresh
            key_resp_num.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_num.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_num.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_num.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_num.getKeys(keyList=['1', '2'], waitRelease=False)
            _key_resp_num_allKeys.extend(theseKeys)
            if len(_key_resp_num_allKeys):
                key_resp_num.keys = _key_resp_num_allKeys[-1].name  # just the last key pressed
                key_resp_num.rt = _key_resp_num_allKeys[-1].rt
        
        # *slider_2* updates
        if slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_2.frameNStart = frameN  # exact frame index
            slider_2.tStart = t  # local t and not account for scr refresh
            slider_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
            slider_2.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['down'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in strangeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "strange"-------
    for thisComponent in strangeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    trials.addData('text_4.started', text_4.tStartRefresh)
    trials.addData('text_4.stopped', text_4.tStopRefresh)
    # check responses
    if key_resp_num.keys in ['', [], None]:  # No response was made
        key_resp_num.keys = None
    trials.addData('key_resp_num.keys',key_resp_num.keys)
    if key_resp_num.keys != None:  # we had a response
        trials.addData('key_resp_num.rt', key_resp_num.rt)
    trials.addData('key_resp_num.started', key_resp_num.tStartRefresh)
    trials.addData('key_resp_num.stopped', key_resp_num.tStopRefresh)
    trials.addData('slider_2.response', slider_2.getRating())
    trials.addData('slider_2.rt', slider_2.getRT())
    trials.addData('slider_2.started', slider_2.tStartRefresh)
    trials.addData('slider_2.stopped', slider_2.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    trials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "strange" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "dis"-------
    continueRoutine = True
    # update component parameters for each repeat
    # only run the routine if the response was a 1:
    if key_resp_yes.keys == 'n':
        continueRoutine = False # don't even start this routine
    key_dis.keys = []
    key_dis.rt = []
    _key_dis_allKeys = []
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    slider_d.reset()
    # keep track of which components have finished
    disComponents = [key_dis, text_7, key_resp_5, slider_d]
    for thisComponent in disComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    disClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "dis"-------
    while continueRoutine:
        # get current time
        t = disClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=disClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if key_dis.keys == '1':
            slider_d.markerPos = 1
        elif key_dis.keys == '2':
            slider_d.markerPos = 2
        elif key_dis.keys == '3':
            slider_d.markerPos = 3
        elif key_dis.keys == '4':
            slider_d.markerPos = 4
        elif key_dis.keys == '5':
            slider_d.markerPos = 5
        
        # *key_dis* updates
        waitOnFlip = False
        if key_dis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_dis.frameNStart = frameN  # exact frame index
            key_dis.tStart = t  # local t and not account for scr refresh
            key_dis.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_dis, 'tStartRefresh')  # time at next scr refresh
            key_dis.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_dis.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_dis.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_dis.status == STARTED and not waitOnFlip:
            theseKeys = key_dis.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _key_dis_allKeys.extend(theseKeys)
            if len(_key_dis_allKeys):
                key_dis.keys = _key_dis_allKeys[-1].name  # just the last key pressed
                key_dis.rt = _key_dis_allKeys[-1].rt
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['down'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *slider_d* updates
        if slider_d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_d.frameNStart = frameN  # exact frame index
            slider_d.tStart = t  # local t and not account for scr refresh
            slider_d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_d, 'tStartRefresh')  # time at next scr refresh
            slider_d.setAutoDraw(True)
        
        # Check slider_d for response to end routine
        if slider_d.getRating() is not None and slider_d.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in disComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "dis"-------
    for thisComponent in disComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_dis.keys in ['', [], None]:  # No response was made
        key_dis.keys = None
    trials.addData('key_dis.keys',key_dis.keys)
    if key_dis.keys != None:  # we had a response
        trials.addData('key_dis.rt', key_dis.rt)
    trials.addData('key_dis.started', key_dis.tStartRefresh)
    trials.addData('key_dis.stopped', key_dis.tStopRefresh)
    trials.addData('text_7.started', text_7.tStartRefresh)
    trials.addData('text_7.stopped', text_7.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    trials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    trials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    trials.addData('slider_d.response', slider_d.getRating())
    trials.addData('slider_d.rt', slider_d.getRT())
    trials.addData('slider_d.started', slider_d.tStartRefresh)
    trials.addData('slider_d.stopped', slider_d.tStopRefresh)
    # the Routine "dis" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('question2.xlsx'),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "question_2"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_ans_2.keys = []
        key_resp_ans_2.rt = []
        _key_resp_ans_2_allKeys = []
        question1.setText(questions1)
        text_6.setText(scale1)
        key_resp_space_2.keys = []
        key_resp_space_2.rt = []
        _key_resp_space_2_allKeys = []
        slider_4.reset()
        # keep track of which components have finished
        question_2Components = [key_resp_ans_2, question1, text_5, text_6, key_resp_space_2, slider_4]
        for thisComponent in question_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        question_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "question_2"-------
        while continueRoutine:
            # get current time
            t = question_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=question_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if key_resp_ans_2.keys == '1':
                slider_4.markerPos = 1
            elif key_resp_ans_2.keys == '2':
                slider_4.markerPos = 2
            elif key_resp_ans_2.keys == '3':
                slider_4.markerPos = 3
            elif key_resp_ans_2.keys == '4':
                slider_4.markerPos = 4
            elif key_resp_ans_2.keys == '5':
                slider_4.markerPos = 5
            
            # *key_resp_ans_2* updates
            waitOnFlip = False
            if key_resp_ans_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_ans_2.frameNStart = frameN  # exact frame index
                key_resp_ans_2.tStart = t  # local t and not account for scr refresh
                key_resp_ans_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_ans_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_ans_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_ans_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_ans_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_ans_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_ans_2.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
                _key_resp_ans_2_allKeys.extend(theseKeys)
                if len(_key_resp_ans_2_allKeys):
                    key_resp_ans_2.keys = _key_resp_ans_2_allKeys[-1].name  # just the last key pressed
                    key_resp_ans_2.rt = _key_resp_ans_2_allKeys[-1].rt
            
            # *question1* updates
            if question1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question1.frameNStart = frameN  # exact frame index
                question1.tStart = t  # local t and not account for scr refresh
                question1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question1, 'tStartRefresh')  # time at next scr refresh
                question1.setAutoDraw(True)
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                text_6.setAutoDraw(True)
            
            # *key_resp_space_2* updates
            waitOnFlip = False
            if key_resp_space_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_space_2.frameNStart = frameN  # exact frame index
                key_resp_space_2.tStart = t  # local t and not account for scr refresh
                key_resp_space_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_space_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_space_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_space_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_space_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_space_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_space_2.getKeys(keyList=['down'], waitRelease=False)
                _key_resp_space_2_allKeys.extend(theseKeys)
                if len(_key_resp_space_2_allKeys):
                    key_resp_space_2.keys = _key_resp_space_2_allKeys[-1].name  # just the last key pressed
                    key_resp_space_2.rt = _key_resp_space_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *slider_4* updates
            if slider_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_4.frameNStart = frameN  # exact frame index
                slider_4.tStart = t  # local t and not account for scr refresh
                slider_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_4, 'tStartRefresh')  # time at next scr refresh
                slider_4.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in question_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "question_2"-------
        for thisComponent in question_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_ans_2.keys in ['', [], None]:  # No response was made
            key_resp_ans_2.keys = None
        trials_2.addData('key_resp_ans_2.keys',key_resp_ans_2.keys)
        if key_resp_ans_2.keys != None:  # we had a response
            trials_2.addData('key_resp_ans_2.rt', key_resp_ans_2.rt)
        trials_2.addData('key_resp_ans_2.started', key_resp_ans_2.tStartRefresh)
        trials_2.addData('key_resp_ans_2.stopped', key_resp_ans_2.tStopRefresh)
        trials_2.addData('question1.started', question1.tStartRefresh)
        trials_2.addData('question1.stopped', question1.tStopRefresh)
        trials_2.addData('text_5.started', text_5.tStartRefresh)
        trials_2.addData('text_5.stopped', text_5.tStopRefresh)
        trials_2.addData('text_6.started', text_6.tStartRefresh)
        trials_2.addData('text_6.stopped', text_6.tStopRefresh)
        # check responses
        if key_resp_space_2.keys in ['', [], None]:  # No response was made
            key_resp_space_2.keys = None
        trials_2.addData('key_resp_space_2.keys',key_resp_space_2.keys)
        if key_resp_space_2.keys != None:  # we had a response
            trials_2.addData('key_resp_space_2.rt', key_resp_space_2.rt)
        trials_2.addData('key_resp_space_2.started', key_resp_space_2.tStartRefresh)
        trials_2.addData('key_resp_space_2.stopped', key_resp_space_2.tStopRefresh)
        trials_2.addData('slider_4.response', slider_4.getRating())
        trials_2.addData('slider_4.rt', slider_4.getRT())
        trials_2.addData('slider_4.started', slider_4.tStartRefresh)
        trials_2.addData('slider_4.stopped', slider_4.tStopRefresh)
        # the Routine "question_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text_3]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
