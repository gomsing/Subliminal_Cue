#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.7),
    on January 22, 2021, at 14:01
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('3.0.7')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.7'
expName = 'experiment_final_0803'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
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
    originPath='C:\\Users\\user\\Dropbox\\Exp_Eugene\\subliminal cue\\experiment 1\\experiment_final_0803_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0.004,0.004,0.004], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instruction_4"
instruction_4Clock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', units='deg', 
    image='inst2_1.png', mask=None,
    ori=0, pos=(0, 0), size=(40,24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "eye_fixation_2"
eye_fixation_2Clock = core.Clock()
 
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',units='deg', 
    size=(1,1),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
polygon_8 = visual.Polygon(
    win=win, name='polygon_8',units='deg', 
    edges=90, size=(2, 2),
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.004,0.004,0.004], fillColorSpace='rgb',
    opacity=0, depth=-2.0, interpolate=True)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "color_tut"
color_tutClock = core.Clock()
SubPos = [0,0]
Dist1Pos=[0,0]
Dist2Pos=[0,0]
Dist3Pos=[0,0]
TargHolePos=[0,0]
DistHole1Pos=[0,0]
DistHole2Pos=[0,0]
DistHole3Pos=[0,0]
TargColor = ''
Dist1Color = ''
Dist2Color = ''
Dist3Color = ''



#color distribution
color1 = [0.919328101270864,0.562714754347291,0.677880544326632] #pink
color2 = [0.738273479967632,0.665884513139248,0.394944342687036] #blue
color3 = [0.285277976226026,0.744574124644093,0.664931204138875] #yellow
color4 = [0.532436017960231,0.678950350974952,0.941414538047463] #green

leftUpPos = [-3, 3]
leftDownPos = [-3, -3]
rightUpPos = [3, 3]
rightDownPos = [3, -3]

def holeup(pos):
    pos1 = [0, 0]
    pos1[0] = pos[0]
    pos1[1] = pos[1]+0.5
    return pos1

def holedown(pos):
    pos1 = [0, 0]
    pos1[0] = pos[0]
    pos1[1] = pos[1]-0.5
    return pos1

def holeleft(pos):
    pos1 = [0,0]
    pos1[1] = pos[1]
    pos1[0] = pos[0] - 0.5
    return pos1


def holeright(pos):
    pos1 = [0, 0]
    pos1[1] = pos[1]
    pos1[0] = pos[0] + 0.5
    return pos1


polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices='cross',units='deg', 
    size=(1, 1),
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
target_red_2 = visual.Polygon(
    win=win, name='target_red_2',units='deg', 
    edges=90, size=(2, 2),
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
sub_cue_4 = visual.Polygon(
    win=win, name='sub_cue_4',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
mask1_6 = visual.Polygon(
    win=win, name='mask1_6',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=(-3,-3),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
mask2_8 = visual.Polygon(
    win=win, name='mask2_8',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=(-3, 3),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
mask1_7 = visual.Polygon(
    win=win, name='mask1_7',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=(3,-3),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
mask1_8 = visual.Polygon(
    win=win, name='mask1_8',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=(3,3),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
circle1 = visual.Polygon(
    win=win, name='circle1',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
circle2 = visual.Polygon(
    win=win, name='circle2',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
circle3 = visual.Polygon(
    win=win, name='circle3',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
circle4 = visual.Polygon(
    win=win, name='circle4',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
hole = visual.Polygon(
    win=win, name='hole',units='deg', 
    edges=90, size=(0.6, 0.6),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
hole_3 = visual.Polygon(
    win=win, name='hole_3',units='deg', 
    edges=90, size=(0.6, 0.6),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
hole3_2 = visual.Polygon(
    win=win, name='hole3_2',units='deg', 
    edges=90, size=(0.6, 0.6),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
hole_5 = visual.Polygon(
    win=win, name='hole_5',units='deg', 
    edges=90, size=(0.6, 0.6),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)

# Initialize components for Routine "feedback_color_2"
feedback_color_2Clock = core.Clock()
feedback = visual.TextStim(win=win, name='feedback',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instruction_4"
instruction_4Clock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', units='deg', 
    image='inst2_1.png', mask=None,
    ori=0, pos=(0, 0), size=(40,24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "eye_fixation"
eye_fixationClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',units='deg', 
    size=(1,1),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
polygon_7 = visual.Polygon(
    win=win, name='polygon_7',units='deg', 
    edges=90, size=(2, 2),
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.004,0.004,0.004], fillColorSpace='rgb',
    opacity=0, depth=-2.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "color"
colorClock = core.Clock()
SubPos = [0,0]
Dist1Pos=[0,0]
Dist2Pos=[0,0]
Dist3Pos=[0,0]
TargHolePos=[0,0]
DistHole1Pos=[0,0]
DistHole2Pos=[0,0]
DistHole3Pos=[0,0]
TargColor = ''
Dist1Color = ''
Dist2Color = ''
Dist3Color = ''



#color distribution
color1 = [0.919328101270864,0.562714754347291,0.677880544326632] #pink
color2 = [0.738273479967632,0.665884513139248,0.394944342687036] #blue
color3 = [0.285277976226026,0.744574124644093,0.664931204138875] #yellow
color4 = [0.532436017960231,0.678950350974952,0.941414538047463] #green

leftUpPos = [-3, 3]
leftDownPos = [-3, -3]
rightUpPos = [3, 3]
rightDownPos = [3, -3]

def holeup(pos):
    pos1 = [0, 0]
    pos1[0] = pos[0]
    pos1[1] = pos[1]+0.5
    return pos1

def holedown(pos):
    pos1 = [0, 0]
    pos1[0] = pos[0]
    pos1[1] = pos[1]-0.5
    return pos1

def holeleft(pos):
    pos1 = [0,0]
    pos1[1] = pos[1]
    pos1[0] = pos[0] - 0.5
    return pos1


def holeright(pos):
    pos1 = [0, 0]
    pos1[1] = pos[1]
    pos1[0] = pos[0] + 0.5
    return pos1


polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',units='deg', 
    size=(1, 1),
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
target_red = visual.Polygon(
    win=win, name='target_red',units='deg', 
    edges=90, size=(2, 2),
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
sub_cue = visual.Polygon(
    win=win, name='sub_cue',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
mask1 = visual.Polygon(
    win=win, name='mask1',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=(-3,-3),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
mask2 = visual.Polygon(
    win=win, name='mask2',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=(-3, 3),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
mask1_3 = visual.Polygon(
    win=win, name='mask1_3',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=(3,-3),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
mask1_4 = visual.Polygon(
    win=win, name='mask1_4',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=(3,3),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
circle1_2 = visual.Polygon(
    win=win, name='circle1_2',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
circle2_2 = visual.Polygon(
    win=win, name='circle2_2',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
circle3_2 = visual.Polygon(
    win=win, name='circle3_2',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
circle4_2 = visual.Polygon(
    win=win, name='circle4_2',units='deg', 
    edges=90, size=(2,2),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
hole_1 = visual.Polygon(
    win=win, name='hole_1',units='deg', 
    edges=90, size=(0.6, 0.6),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
hole_2 = visual.Polygon(
    win=win, name='hole_2',units='deg', 
    edges=90, size=(0.6, 0.6),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
hole3 = visual.Polygon(
    win=win, name='hole3',units='deg', 
    edges=90, size=(0.6, 0.6),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
hole_4 = visual.Polygon(
    win=win, name='hole_4',units='deg', 
    edges=90, size=(0.6, 0.6),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)

# Initialize components for Routine "feedback_color"
feedback_colorClock = core.Clock()
feedback_4 = visual.TextStim(win=win, name='feedback_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
nblockText=''
text_2 = visual.TextStim(win=win, name='text_2',
    text='Take a break! \n\nPress the space bar when you are ready to start again!\n\n잠시 쉬어가세요! \n\n준비가 되셨을때 스페이스바를 눌러서 다시 실험으로 돌아가세요. ',
    font='Arial',
    pos=(0, 0.1), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=(0, -0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='you are all done!\n\nthank you for participating :) \n\n수고하셨습니다!\n\n참여해주셔서 감사합니다.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction_4"-------
t = 0
instruction_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_12 = event.BuilderKeyResponse()
# keep track of which components have finished
instruction_4Components = [image_4, key_resp_12]
for thisComponent in instruction_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction_4"-------
while continueRoutine:
    # get current time
    t = instruction_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if t >= 0.0 and image_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_4.tStart = t
        image_4.frameNStart = frameN  # exact frame index
        image_4.setAutoDraw(True)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_4"-------
for thisComponent in instruction_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('tutorial.xlsx'),
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
    
    # ------Prepare to start Routine "eye_fixation_2"-------
    t = 0
    eye_fixation_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    win.mouseVisible = True
    mousePos1 = mouse_2.getPos()
    
    
    # setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    eye_fixation_2Components = [polygon_4, polygon_8, mouse_2]
    for thisComponent in eye_fixation_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "eye_fixation_2"-------
    while continueRoutine:
        # get current time
        t = eye_fixation_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if polygon_8.contains(mouse_2):
            core.wait(0.1)
            continueRoutine = False 
        
        
        # *polygon_4* updates
        if t >= 0.0 and polygon_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_4.tStart = t
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.setAutoDraw(True)
        
        # *polygon_8* updates
        if t >= 0.0 and polygon_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_8.tStart = t
            polygon_8.frameNStart = frameN  # exact frame index
            polygon_8.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eye_fixation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "eye_fixation_2"-------
    for thisComponent in eye_fixation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    win.mouseVisible = False 
    # store data for trials (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [polygon]:
            if obj.contains(mouse_2):
                gotValidClick = True
                mouse_2.clicked_name.append(obj.name)
    trials.addData('mouse_2.x', x)
    trials.addData('mouse_2.y', y)
    trials.addData('mouse_2.leftButton', buttons[0])
    trials.addData('mouse_2.midButton', buttons[1])
    trials.addData('mouse_2.rightButton', buttons[2])
    if len(mouse_2.clicked_name):
        trials.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
    # the Routine "eye_fixation_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "color_tut"-------
    t = 0
    color_tutClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    import numpy as np
    from numpy.random import random
    
    
    #---------------------------------position---------
    if cue1 == 'Valid':
        SubPos = TargPos1
    elif cue1 == 'Invalid':
        SubPos = Dist1Pos
    
    if TargPos1 == [-3,3]:
        posLists = [leftDownPos, rightUpPos, rightDownPos]
        Pos = ['leftDownPos', 'rightUpPos', 'rightDownPos']
        StartIdx =  np.random.choice(Pos, 3, p=[0.34, 0.33, 0.33], replace = False)
        StartPos = []
        for idx in StartIdx:
            StartPos.append(posLists[Pos.index(idx)])
        Dist1Pos = StartPos[0]
        Dist2Pos = StartPos[1]
        Dist3Pos = StartPos[2]
        if random()>0.5:
            TargHolePos = holeleft(TargPos1)
            np.random.shuffle(StartPos)
            DistHole1Pos = holedown(StartPos[0])
            DistHole2Pos = holeright(StartPos[1])
            DistHole3Pos = holeup(StartPos[2])
            corrAns = 'left'
        else: 
            TargHolePos = holeright(TargPos1)
            np.random.shuffle(StartPos)
            DistHole1Pos = holedown(StartPos[0])
            DistHole2Pos = holeleft(StartPos[1])
            DistHole3Pos = holeup(StartPos[2])
            corrAns = 'right'
    
    elif TargPos1 == [-3,-3]:
        posLists = [leftUpPos, rightUpPos, rightDownPos]
        Pos = ['leftUpPos', 'rightUpPos', 'rightDownPos']
        StartIdx =  np.random.choice(Pos, 3, p=[0.34, 0.33, 0.33], replace = False)
        StartPos = []
        for idx in StartIdx:
            StartPos.append(posLists[Pos.index(idx)])
        Dist1Pos = StartPos[0]
        Dist2Pos = StartPos[1]
        Dist3Pos = StartPos[2]
        if random()>0.5:
            TargHolePos = holeleft(TargPos1)
            np.random.shuffle(StartPos)
            DistHole1Pos = holedown(StartPos[0])
            DistHole2Pos = holeright(StartPos[1])
            DistHole3Pos = holeup(StartPos[2])
            corrAns = 'left'
        else: 
            TargHolePos = holeright(TargPos1)
            np.random.shuffle(StartPos)
            DistHole1Pos = holedown(StartPos[0])
            DistHole2Pos = holeleft(StartPos[1])
            DistHole3Pos = holeup(StartPos[2])
            corrAns = 'right'
    
    
    elif TargPos1 == [3,3]:
        posLists = [leftUpPos, leftDownPos, rightDownPos]
        Pos = ['leftUpPos', 'leftDownPos', 'rightDownPos']
        StartIdx =  np.random.choice(Pos, 3, p=[0.34, 0.33, 0.33], replace = False)
        StartPos = []
        for idx in StartIdx:
            StartPos.append(posLists[Pos.index(idx)])
        Dist1Pos = StartPos[0]
        Dist2Pos = StartPos[1]
        Dist3Pos = StartPos[2]
        if random()>0.5:
            TargHolePos = holeleft(TargPos1)
            np.random.shuffle(StartPos)
            DistHole1Pos = holedown(StartPos[0])
            DistHole2Pos = holeright(StartPos[1])
            DistHole3Pos = holeup(StartPos[2])
            corrAns = 'left'
        else: 
            TargHolePos = holeright(TargPos1)
            np.random.shuffle(StartPos)
            DistHole1Pos = holedown(StartPos[0])
            DistHole2Pos = holeleft(StartPos[1])
            DistHole3Pos = holeup(StartPos[2])
            corrAns = 'right'
        
    elif TargPos1 == [3,-3]:
        posLists = [leftUpPos, leftDownPos, rightUpPos]
        Pos = ['leftDownPos', 'rightUpPos', 'leftUpPos']
        StartIdx =  np.random.choice(Pos, 3, p=[0.34, 0.33, 0.33], replace = False)
        StartPos = []
        for idx in StartIdx:
            StartPos.append(posLists[Pos.index(idx)])
        Dist1Pos = StartPos[0]
        Dist2Pos = StartPos[1]
        Dist3Pos = StartPos[2]
        if random()>0.5:
            TargHolePos = holeleft(TargPos1)
            np.random.shuffle(StartPos)
            DistHole1Pos = holedown(StartPos[0])
            DistHole2Pos = holeright(StartPos[1])
            DistHole3Pos = holeup(StartPos[2])
            corrAns = 'left'
        else: 
            TargHolePos = holeright(TargPos1)
            np.random.shuffle(StartPos)
            DistHole1Pos = holedown(StartPos[0])
            DistHole2Pos = holeleft(StartPos[1])
            DistHole3Pos = holeup(StartPos[2])
            corrAns = 'right'
    
    #-----------------color-------------------------------------------------------------#
        
    if TargColor1 == 'color1': #if target color is color1
        #distribute color randomly
    #    colorLists = [color2, color3, color4]
    #    color = ['color2', 'color3', 'color4']
    #    colorIdx = np.random.choice(color, 3, p=[0.34, 0.33, 0.33], replace = False)
    #    colorPos = []
    #    for idx in colorIdx:
    #        colorPos.append(colorLists[color.index(idx)])
        TargColor1 = color1
        Dist1Color = color2
        Dist2Color = color3
        Dist3Color = color4
            
    elif TargColor1 == 'color2': #if target color is color 2
        #distribute color randomly
     #   colorLists = [color1, color3, color4]
     #   color = ['color1', 'color3', 'color4']
     #   colorIdx = np.random.choice(color, 3, p=[0.34, 0.33, 0.33], replace = False)
     #   colorPos = []
     #   for idx in colorIdx:
      #      colorPos.append(colorLists[color.index(idx)])
        TargColor1 = color2
        Dist1Color = color1
        Dist2Color = color3
        Dist3Color = color4
        
    elif TargColor1 == 'color3':
        TargColor1 = color3
        Dist1Color = color1
        Dist2Color = color2
        Dist3Color = color4
    
    elif TargColor1 == 'color4':
        TargColor1 = color4
        Dist1Color = color1
        Dist2Color = color2
        Dist3Color = color3
        
    #---------------------------hole-------------------------
    
    
        
                
    target_red_2.setFillColor(TargColor1)
    sub_cue_4.setPos(SubPos)
    circle1.setPos(TargPos1)
    circle1.setFillColor(TargColor1)
    circle2.setPos(Dist1Pos)
    circle2.setFillColor(Dist1Color)
    circle3.setPos(Dist2Pos)
    circle3.setFillColor(Dist2Color)
    circle4.setPos(Dist3Pos)
    circle4.setFillColor(Dist3Color)
    circle4.setLineColor(Dist3Color)
    hole.setPos(TargHolePos)
    hole_3.setPos(DistHole1Pos)
    hole3_2.setPos(DistHole2Pos)
    hole_5.setPos(DistHole3Pos)
    key_resp_4 = event.BuilderKeyResponse()
    # keep track of which components have finished
    color_tutComponents = [polygon_3, target_red_2, sub_cue_4, mask1_6, mask2_8, mask1_7, mask1_8, circle1, circle2, circle3, circle4, hole, hole_3, hole3_2, hole_5, key_resp_4]
    for thisComponent in color_tutComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "color_tut"-------
    while continueRoutine:
        # get current time
        t = color_tutClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_3* updates
        if t >= 0.0 and polygon_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_3.tStart = t
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.setAutoDraw(True)
        
        # *target_red_2* updates
        if t >= 0.0 and target_red_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            target_red_2.tStart = t
            target_red_2.frameNStart = frameN  # exact frame index
            target_red_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if target_red_2.status == STARTED and t >= frameRemains:
            target_red_2.setAutoDraw(False)
        
        # *sub_cue_4* updates
        if t >= 1.0 and sub_cue_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            sub_cue_4.tStart = t
            sub_cue_4.frameNStart = frameN  # exact frame index
            sub_cue_4.setAutoDraw(True)
        if sub_cue_4.status == STARTED and frameN >= (sub_cue_4.frameNStart + 2):
            sub_cue_4.setAutoDraw(False)
        
        # *mask1_6* updates
        if (sub_cue_4.status == FINISHED) and mask1_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask1_6.tStart = t
            mask1_6.frameNStart = frameN  # exact frame index
            mask1_6.setAutoDraw(True)
        if mask1_6.status == STARTED and t >= (mask1_6.tStart + 0.033):
            mask1_6.setAutoDraw(False)
        
        # *mask2_8* updates
        if (sub_cue_4.status == FINISHED) and mask2_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask2_8.tStart = t
            mask2_8.frameNStart = frameN  # exact frame index
            mask2_8.setAutoDraw(True)
        if mask2_8.status == STARTED and t >= (mask2_8.tStart + 0.033):
            mask2_8.setAutoDraw(False)
        
        # *mask1_7* updates
        if (sub_cue_4.status == FINISHED) and mask1_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask1_7.tStart = t
            mask1_7.frameNStart = frameN  # exact frame index
            mask1_7.setAutoDraw(True)
        if mask1_7.status == STARTED and t >= (mask1_7.tStart + 0.033):
            mask1_7.setAutoDraw(False)
        
        # *mask1_8* updates
        if (sub_cue_4.status == FINISHED) and mask1_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask1_8.tStart = t
            mask1_8.frameNStart = frameN  # exact frame index
            mask1_8.setAutoDraw(True)
        if mask1_8.status == STARTED and t >= (mask1_8.tStart + 0.033):
            mask1_8.setAutoDraw(False)
        
        # *circle1* updates
        if (mask1_6.status == FINISHED) and circle1.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle1.tStart = t
            circle1.frameNStart = frameN  # exact frame index
            circle1.setAutoDraw(True)
        if circle1.status == STARTED and t >= (circle1.tStart + 0.2):
            circle1.setAutoDraw(False)
        
        # *circle2* updates
        if (mask1_6.status == FINISHED) and circle2.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle2.tStart = t
            circle2.frameNStart = frameN  # exact frame index
            circle2.setAutoDraw(True)
        if circle2.status == STARTED and t >= (circle2.tStart + 0.2):
            circle2.setAutoDraw(False)
        
        # *circle3* updates
        if (mask1_6.status == FINISHED) and circle3.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle3.tStart = t
            circle3.frameNStart = frameN  # exact frame index
            circle3.setAutoDraw(True)
        if circle3.status == STARTED and t >= (circle3.tStart + 0.2):
            circle3.setAutoDraw(False)
        
        # *circle4* updates
        if (mask1_6.status == FINISHED) and circle4.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle4.tStart = t
            circle4.frameNStart = frameN  # exact frame index
            circle4.setAutoDraw(True)
        if circle4.status == STARTED and t >= (circle4.tStart + 0.2):
            circle4.setAutoDraw(False)
        
        # *hole* updates
        if (mask1_6.status == FINISHED) and hole.status == NOT_STARTED:
            # keep track of start time/frame for later
            hole.tStart = t
            hole.frameNStart = frameN  # exact frame index
            hole.setAutoDraw(True)
        if hole.status == STARTED and t >= (hole.tStart + 0.2):
            hole.setAutoDraw(False)
        
        # *hole_3* updates
        if (mask1_6.status == FINISHED) and hole_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            hole_3.tStart = t
            hole_3.frameNStart = frameN  # exact frame index
            hole_3.setAutoDraw(True)
        if hole_3.status == STARTED and t >= (hole_3.tStart + 0.2):
            hole_3.setAutoDraw(False)
        
        # *hole3_2* updates
        if (mask1_6.status == FINISHED) and hole3_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            hole3_2.tStart = t
            hole3_2.frameNStart = frameN  # exact frame index
            hole3_2.setAutoDraw(True)
        if hole3_2.status == STARTED and t >= (hole3_2.tStart + 0.2):
            hole3_2.setAutoDraw(False)
        
        # *hole_5* updates
        if (mask1_6.status == FINISHED) and hole_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            hole_5.tStart = t
            hole_5.frameNStart = frameN  # exact frame index
            hole_5.setAutoDraw(True)
        if hole_5.status == STARTED and t >= (hole_5.tStart + 0.2):
            hole_5.setAutoDraw(False)
        
        # *key_resp_4* updates
        if (circle1.status == FINISHED) and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['right', 'left'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_4.keys = theseKeys[-1]  # just the last key pressed
                key_resp_4.rt = key_resp_4.clock.getTime()
                # was this 'correct'?
                if (key_resp_4.keys == str(corrAns)) or (key_resp_4.keys == corrAns):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in color_tutComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "color_tut"-------
    for thisComponent in color_tutComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_4.corr = 1;  # correct non-response
        else:
           key_resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    trials.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    # the Routine "color_tut" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback_color_2"-------
    t = 0
    feedback_color_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.150000)
    # update component parameters for each repeat
    if key_resp_4.corr:
        msg = '정답!'
    else :
        msg = '오답'
    feedback.setText(msg)
    # keep track of which components have finished
    feedback_color_2Components = [feedback]
    for thisComponent in feedback_color_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback_color_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback_color_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback* updates
        if t >= 0.0 and feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback.tStart = t
            feedback.frameNStart = frameN  # exact frame index
            feedback.setAutoDraw(True)
        frameRemains = 0.0 + 0.15- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedback.status == STARTED and t >= frameRemains:
            feedback.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_color_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback_color_2"-------
    for thisComponent in feedback_color_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "instruction_4"-------
t = 0
instruction_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_12 = event.BuilderKeyResponse()
# keep track of which components have finished
instruction_4Components = [image_4, key_resp_12]
for thisComponent in instruction_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction_4"-------
while continueRoutine:
    # get current time
    t = instruction_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if t >= 0.0 and image_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_4.tStart = t
        image_4.frameNStart = frameN  # exact frame index
        image_4.setAutoDraw(True)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_4"-------
for thisComponent in instruction_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=10, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('cue_condition0630.xlsx'),
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
        
        # ------Prepare to start Routine "eye_fixation"-------
        t = 0
        eye_fixationClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        win.mouseVisible = True
        mousePos = mouse.getPos()
        
        
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        eye_fixationComponents = [polygon, polygon_7, mouse]
        for thisComponent in eye_fixationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "eye_fixation"-------
        while continueRoutine:
            # get current time
            t = eye_fixationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if polygon_7.contains(mouse):
                core.wait(0.1)
                continueRoutine = False 
            
            # *polygon* updates
            if t >= 0.0 and polygon.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon.tStart = t
                polygon.frameNStart = frameN  # exact frame index
                polygon.setAutoDraw(True)
            
            # *polygon_7* updates
            if t >= 0.0 and polygon_7.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_7.tStart = t
                polygon_7.frameNStart = frameN  # exact frame index
                polygon_7.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in eye_fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "eye_fixation"-------
        for thisComponent in eye_fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        win.mouseVisible = False 
        # store data for trials_2 (TrialHandler)
        x, y = mouse.getPos()
        buttons = mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [polygon]:
                if obj.contains(mouse):
                    gotValidClick = True
                    mouse.clicked_name.append(obj.name)
        trials_2.addData('mouse.x', x)
        trials_2.addData('mouse.y', y)
        trials_2.addData('mouse.leftButton', buttons[0])
        trials_2.addData('mouse.midButton', buttons[1])
        trials_2.addData('mouse.rightButton', buttons[2])
        if len(mouse.clicked_name):
            trials_2.addData('mouse.clicked_name', mouse.clicked_name[0])
        # the Routine "eye_fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "color"-------
        t = 0
        colorClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        import numpy as np
        from numpy.random import random
        
        #threshold------------------------------------------
        value = (reversal_value[-8] + reversal_value[-7] + reversal_value[-6] + reversal_value[-5] + reversal_value[-4] + reversal_value[-3] + reversal_value[-2] + reversal_value[-1]) / 8
        
        #value = (thStore[-1] + thStore[-2] + thStore[-3] + thStore [-4])/4
        
        #---------------------------------position---------
        if cue == 'Valid':
            SubPos = TargPos
        elif cue == 'Invalid':
            SubPos = Dist1Pos
        
        if TargPos == [-3,3]:
            posLists = [leftDownPos, rightUpPos, rightDownPos]
            Pos = ['leftDownPos', 'rightUpPos', 'rightDownPos']
            StartIdx =  np.random.choice(Pos, 3, p=[0.34, 0.33, 0.33], replace = False)
            StartPos = []
            for idx in StartIdx:
                StartPos.append(posLists[Pos.index(idx)])
            Dist1Pos = StartPos[0]
            Dist2Pos = StartPos[1]
            Dist3Pos = StartPos[2]
            if random()>0.5:
                TargHolePos = holeleft(TargPos)
                np.random.shuffle(StartPos)
                DistHole1Pos = holedown(StartPos[0])
                DistHole2Pos = holeright(StartPos[1])
                DistHole3Pos = holeup(StartPos[2])
                corrAns = 'left'
            else: 
                TargHolePos = holeright(TargPos)
                np.random.shuffle(StartPos)
                DistHole1Pos = holedown(StartPos[0])
                DistHole2Pos = holeleft(StartPos[1])
                DistHole3Pos = holeup(StartPos[2])
                corrAns = 'right'
        
        elif TargPos == [-3,-3]:
            posLists = [leftUpPos, rightUpPos, rightDownPos]
            Pos = ['leftUpPos', 'rightUpPos', 'rightDownPos']
            StartIdx =  np.random.choice(Pos, 3, p=[0.34, 0.33, 0.33], replace = False)
            StartPos = []
            for idx in StartIdx:
                StartPos.append(posLists[Pos.index(idx)])
            Dist1Pos = StartPos[0]
            Dist2Pos = StartPos[1]
            Dist3Pos = StartPos[2]
            if random()>0.5:
                TargHolePos = holeleft(TargPos)
                np.random.shuffle(StartPos)
                DistHole1Pos = holedown(StartPos[0])
                DistHole2Pos = holeright(StartPos[1])
                DistHole3Pos = holeup(StartPos[2])
                corrAns = 'left'
            else: 
                TargHolePos = holeright(TargPos)
                np.random.shuffle(StartPos)
                DistHole1Pos = holedown(StartPos[0])
                DistHole2Pos = holeleft(StartPos[1])
                DistHole3Pos = holeup(StartPos[2])
                corrAns = 'right'
        
        
        elif TargPos == [3,3]:
            posLists = [leftUpPos, leftDownPos, rightDownPos]
            Pos = ['leftUpPos', 'leftDownPos', 'rightDownPos']
            StartIdx =  np.random.choice(Pos, 3, p=[0.34, 0.33, 0.33], replace = False)
            StartPos = []
            for idx in StartIdx:
                StartPos.append(posLists[Pos.index(idx)])
            Dist1Pos = StartPos[0]
            Dist2Pos = StartPos[1]
            Dist3Pos = StartPos[2]
            if random()>0.5:
                TargHolePos = holeleft(TargPos)
                np.random.shuffle(StartPos)
                DistHole1Pos = holedown(StartPos[0])
                DistHole2Pos = holeright(StartPos[1])
                DistHole3Pos = holeup(StartPos[2])
                corrAns = 'left'
            else: 
                TargHolePos = holeright(TargPos)
                np.random.shuffle(StartPos)
                DistHole1Pos = holedown(StartPos[0])
                DistHole2Pos = holeleft(StartPos[1])
                DistHole3Pos = holeup(StartPos[2])
                corrAns = 'right'
            
        elif TargPos == [3,-3]:
            posLists = [leftUpPos, leftDownPos, rightUpPos]
            Pos = ['leftDownPos', 'rightUpPos', 'leftUpPos']
            StartIdx =  np.random.choice(Pos, 3, p=[0.34, 0.33, 0.33], replace = False)
            StartPos = []
            for idx in StartIdx:
                StartPos.append(posLists[Pos.index(idx)])
            Dist1Pos = StartPos[0]
            Dist2Pos = StartPos[1]
            Dist3Pos = StartPos[2]
            if random()>0.5:
                TargHolePos = holeleft(TargPos)
                np.random.shuffle(StartPos)
                DistHole1Pos = holedown(StartPos[0])
                DistHole2Pos = holeright(StartPos[1])
                DistHole3Pos = holeup(StartPos[2])
                corrAns = 'left'
            else: 
                TargHolePos = holeright(TargPos)
                np.random.shuffle(StartPos)
                DistHole1Pos = holedown(StartPos[0])
                DistHole2Pos = holeleft(StartPos[1])
                DistHole3Pos = holeup(StartPos[2])
                corrAns = 'right'
        
        #-----------------color-------------------------------------------------------------#
            
        if TargColor == 'color1': #if target color is color1
            #distribute color randomly
        #    colorLists = [color2, color3, color4]
        #    color = ['color2', 'color3', 'color4']
        #    colorIdx = np.random.choice(color, 3, p=[0.34, 0.33, 0.33], replace = False)
        #    colorPos = []
        #    for idx in colorIdx:
        #        colorPos.append(colorLists[color.index(idx)])
            TargColor = color1
            Dist1Color = color2
            Dist2Color = color3
            Dist3Color = color4
                
        elif TargColor == 'color2': #if target color is color 2
            #distribute color randomly
         #   colorLists = [color1, color3, color4]
         #   color = ['color1', 'color3', 'color4']
         #   colorIdx = np.random.choice(color, 3, p=[0.34, 0.33, 0.33], replace = False)
         #   colorPos = []
         #   for idx in colorIdx:
          #      colorPos.append(colorLists[color.index(idx)])
            TargColor = color2
            Dist1Color = color1
            Dist2Color = color3
            Dist3Color = color4
            
        elif TargColor == 'color3':
            TargColor = color3
            Dist1Color = color1
            Dist2Color = color2
            Dist3Color = color4
        
        elif TargColor == 'color4':
            TargColor = color4
            Dist1Color = color1
            Dist2Color = color2
            Dist3Color = color3
            
        #---------------------------hole-------------------------
        
        
            
                    
        target_red.setFillColor(TargColor)
        sub_cue.setPos(SubPos)
        circle1_2.setPos(TargPos)
        circle1_2.setFillColor(TargColor)
        circle2_2.setPos(Dist1Pos)
        circle2_2.setFillColor(Dist1Color)
        circle3_2.setPos(Dist2Pos)
        circle3_2.setFillColor(Dist2Color)
        circle4_2.setPos(Dist3Pos)
        circle4_2.setFillColor(Dist3Color)
        circle4_2.setLineColor(Dist3Color)
        hole_1.setPos(TargHolePos)
        hole_2.setPos(DistHole1Pos)
        hole3.setPos(DistHole2Pos)
        hole_4.setPos(DistHole3Pos)
        key_resp_3 = event.BuilderKeyResponse()
        # keep track of which components have finished
        colorComponents = [polygon_2, target_red, sub_cue, mask1, mask2, mask1_3, mask1_4, circle1_2, circle2_2, circle3_2, circle4_2, hole_1, hole_2, hole3, hole_4, key_resp_3]
        for thisComponent in colorComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "color"-------
        while continueRoutine:
            # get current time
            t = colorClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_2* updates
            if t >= 0.0 and polygon_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_2.tStart = t
                polygon_2.frameNStart = frameN  # exact frame index
                polygon_2.setAutoDraw(True)
            
            # *target_red* updates
            if t >= 0.0 and target_red.status == NOT_STARTED:
                # keep track of start time/frame for later
                target_red.tStart = t
                target_red.frameNStart = frameN  # exact frame index
                target_red.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if target_red.status == STARTED and t >= frameRemains:
                target_red.setAutoDraw(False)
            
            # *sub_cue* updates
            if t >= 1.5 and sub_cue.status == NOT_STARTED:
                # keep track of start time/frame for later
                sub_cue.tStart = t
                sub_cue.frameNStart = frameN  # exact frame index
                sub_cue.setAutoDraw(True)
            if sub_cue.status == STARTED and frameN >= (sub_cue.frameNStart + value):
                sub_cue.setAutoDraw(False)
            
            # *mask1* updates
            if (sub_cue.status == FINISHED) and mask1.status == NOT_STARTED:
                # keep track of start time/frame for later
                mask1.tStart = t
                mask1.frameNStart = frameN  # exact frame index
                mask1.setAutoDraw(True)
            if mask1.status == STARTED and t >= (mask1.tStart + 0.033):
                mask1.setAutoDraw(False)
            
            # *mask2* updates
            if (sub_cue.status == FINISHED) and mask2.status == NOT_STARTED:
                # keep track of start time/frame for later
                mask2.tStart = t
                mask2.frameNStart = frameN  # exact frame index
                mask2.setAutoDraw(True)
            if mask2.status == STARTED and t >= (mask2.tStart + 0.033):
                mask2.setAutoDraw(False)
            
            # *mask1_3* updates
            if (sub_cue.status == FINISHED) and mask1_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                mask1_3.tStart = t
                mask1_3.frameNStart = frameN  # exact frame index
                mask1_3.setAutoDraw(True)
            if mask1_3.status == STARTED and t >= (mask1_3.tStart + 0.033):
                mask1_3.setAutoDraw(False)
            
            # *mask1_4* updates
            if (sub_cue.status == FINISHED) and mask1_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                mask1_4.tStart = t
                mask1_4.frameNStart = frameN  # exact frame index
                mask1_4.setAutoDraw(True)
            if mask1_4.status == STARTED and t >= (mask1_4.tStart + 0.033):
                mask1_4.setAutoDraw(False)
            
            # *circle1_2* updates
            if (mask1.status == FINISHED) and circle1_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                circle1_2.tStart = t
                circle1_2.frameNStart = frameN  # exact frame index
                circle1_2.setAutoDraw(True)
            if circle1_2.status == STARTED and t >= (circle1_2.tStart + 0.2):
                circle1_2.setAutoDraw(False)
            
            # *circle2_2* updates
            if (mask1.status == FINISHED) and circle2_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                circle2_2.tStart = t
                circle2_2.frameNStart = frameN  # exact frame index
                circle2_2.setAutoDraw(True)
            if circle2_2.status == STARTED and t >= (circle2_2.tStart + 0.2):
                circle2_2.setAutoDraw(False)
            
            # *circle3_2* updates
            if (mask1.status == FINISHED) and circle3_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                circle3_2.tStart = t
                circle3_2.frameNStart = frameN  # exact frame index
                circle3_2.setAutoDraw(True)
            if circle3_2.status == STARTED and t >= (circle3_2.tStart + 0.2):
                circle3_2.setAutoDraw(False)
            
            # *circle4_2* updates
            if (mask1.status == FINISHED) and circle4_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                circle4_2.tStart = t
                circle4_2.frameNStart = frameN  # exact frame index
                circle4_2.setAutoDraw(True)
            if circle4_2.status == STARTED and t >= (circle4_2.tStart + 0.2):
                circle4_2.setAutoDraw(False)
            
            # *hole_1* updates
            if (mask1.status == FINISHED) and hole_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                hole_1.tStart = t
                hole_1.frameNStart = frameN  # exact frame index
                hole_1.setAutoDraw(True)
            if hole_1.status == STARTED and t >= (hole_1.tStart + 0.2):
                hole_1.setAutoDraw(False)
            
            # *hole_2* updates
            if (mask1.status == FINISHED) and hole_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                hole_2.tStart = t
                hole_2.frameNStart = frameN  # exact frame index
                hole_2.setAutoDraw(True)
            if hole_2.status == STARTED and t >= (hole_2.tStart + 0.2):
                hole_2.setAutoDraw(False)
            
            # *hole3* updates
            if (mask1.status == FINISHED) and hole3.status == NOT_STARTED:
                # keep track of start time/frame for later
                hole3.tStart = t
                hole3.frameNStart = frameN  # exact frame index
                hole3.setAutoDraw(True)
            if hole3.status == STARTED and t >= (hole3.tStart + 0.2):
                hole3.setAutoDraw(False)
            
            # *hole_4* updates
            if (mask1.status == FINISHED) and hole_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                hole_4.tStart = t
                hole_4.frameNStart = frameN  # exact frame index
                hole_4.setAutoDraw(True)
            if hole_4.status == STARTED and t >= (hole_4.tStart + 0.2):
                hole_4.setAutoDraw(False)
            
            # *key_resp_3* updates
            if (circle1_2.status == FINISHED) and key_resp_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_3.tStart = t
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_3.status == STARTED:
                theseKeys = event.getKeys(keyList=['right', 'left'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_3.rt = key_resp_3.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_3.keys == str(corrAns)) or (key_resp_3.keys == corrAns):
                        key_resp_3.corr = 1
                    else:
                        key_resp_3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in colorComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "color"-------
        for thisComponent in colorComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('threshold', value)
        trials_2.addData('circle_start', circle1_2.tStart)
        trials_2.addData('sub_cue_start', sub_cue.tStart)
        trials_2.addData('mask_start', mask1.tStart)
        trials_2.addData('sub_cue_time', mask1.tStart - sub_cue.tStart)
        trials_2.addData('Subpos', SubPos)
        
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys=None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_3.corr = 1;  # correct non-response
            else:
               key_resp_3.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('key_resp_3.keys',key_resp_3.keys)
        trials_2.addData('key_resp_3.corr', key_resp_3.corr)
        if key_resp_3.keys != None:  # we had a response
            trials_2.addData('key_resp_3.rt', key_resp_3.rt)
        # the Routine "color" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedback_color"-------
        t = 0
        feedback_colorClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.150000)
        # update component parameters for each repeat
        if key_resp_3.corr:
            msg = '정답!'
        else :
            msg = '오답'
        feedback_4.setText(msg)
        # keep track of which components have finished
        feedback_colorComponents = [feedback_4]
        for thisComponent in feedback_colorComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedback_color"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedback_colorClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_4* updates
            if t >= 0.0 and feedback_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_4.tStart = t
                feedback_4.frameNStart = frameN  # exact frame index
                feedback_4.setAutoDraw(True)
            frameRemains = 0.0 + 0.15- win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedback_4.status == STARTED and t >= frameRemains:
                feedback_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_colorComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback_color"-------
        for thisComponent in feedback_colorComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
    
    # ------Prepare to start Routine "break_2"-------
    t = 0
    break_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    nblock=block.thisRepN+1
    nblockText="You finished %d out of 10 blocks."%(nblock)
    text_3.setText(nblockText)
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    break_2Components = [text_2, text_3, key_resp_2]
    for thisComponent in break_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "break_2"-------
    while continueRoutine:
        # get current time
        t = break_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    block.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        block.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10 repeats of 'block'


# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
