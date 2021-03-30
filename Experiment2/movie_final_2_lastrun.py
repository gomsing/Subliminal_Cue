#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on 1월 22, 2021, at 11:55
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
psychopyVersion = '2020.2.4'
expName = 'movie_final_2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
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
    originPath='C:\\Users\\hwang\\Dropbox\\Exp_Eugene\\subliminal cue\\experiment2\\experiment\\movie_final_2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='default', color=[0,0,0], colorSpace='rgb',
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
    text='앞으로 30개의 영상들을 보게 됩니다. \nYou will be watching 30 videos.\n\n고개가 최대한 움직이지 않게 시청을 해주시기 바랍니다. \nPlease try not to move your head during the experiment.\n\n답변은 모두 키보드로 해주시면 됩니다. \nAll the questions are answered using the keyboard. \n\n우측 방향키(→)를 눌러서 시작해주세요. \nPress right key to proceed.',
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
opacity = 0.15
cue = 0.008

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
side = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#side = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
#side = [0,0,1,1,1,1]
random.shuffle(side) #같은 비율 유지 
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

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='수고하셨습니다 :) \n\n실험의 다음 단계 안내를 기다려주세요 ',
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
    
    starttime = 0
    num = trials.thisN
    side_rec = ''
    if side[num] == 0: #left 80%, right 20% 
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
        
        
    elif side[num] == 1:  #left 20%, right 80% 
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
    thisExp.addData('noise_time', time.time())
    thisExp.addData('noise_tick', cv2.getTickCount())
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
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(3.000000)
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
        if tThisFlipGlobal > text_3.tStartRefresh + 3-frameTolerance:
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
