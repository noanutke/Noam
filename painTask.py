#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on October 21, 2018, at 15:39
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'feedbackInTheMagnet'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 720), fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
imgStartExp = visual.ImageStim(
    win=win, name='imgStartExp',
    image='start.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "startFixation"
startFixationClock = core.Clock()
fixationStart = visual.TextStim(win=win, name='fixationStart',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.6, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
p_port = parallel.ParallelPort(address='0x0378')

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
fixationTrial = visual.TextStim(win=win, name='fixationTrial',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.6, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
p_port_2 = parallel.ParallelPort(address='0x0378')

# Initialize components for Routine "jitter1"
jitter1Clock = core.Clock()
jitt_1 = visual.TextStim(win=win, name='jitt_1',
    text=None,
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "stimulus"
stimulusClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=0.6, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);
stim = visual.ImageStim(
    win=win, name='stim',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
p_port_7 = parallel.ParallelPort(address='0x0378')

# Initialize components for Routine "jitter2"
jitter2Clock = core.Clock()
jitt_2 = visual.TextStim(win=win, name='jitt_2',
    text=None,
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "feedback_3"
feedback_3Clock = core.Clock()
scaleImage = visual.ImageStim(
    win=win, name='scaleImage',
    image='scale.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.53, pos=[0.01, -0.04], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='', markerStart='5', tickHeight='5', showAccept=False)
p_port_3 = parallel.ParallelPort(address='0x0378')

# Initialize components for Routine "arrow"
arrowClock = core.Clock()
ar_st = visual.ImageStim(
    win=win, name='ar_st',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "response"
responseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
t = 0
welcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
expStart_key_resp = event.BuilderKeyResponse()
# keep track of which components have finished
welcomeComponents = [imgStartExp, expStart_key_resp]
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *imgStartExp* updates
    if t >= 0.0 and imgStartExp.status == NOT_STARTED:
        # keep track of start time/frame for later
        imgStartExp.tStart = t
        imgStartExp.frameNStart = frameN  # exact frame index
        imgStartExp.setAutoDraw(True)
    
    # *expStart_key_resp* updates
    if t >= 0.0 and expStart_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        expStart_key_resp.tStart = t
        expStart_key_resp.frameNStart = frameN  # exact frame index
        expStart_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(expStart_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if expStart_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            if expStart_key_resp.keys == []:  # then this was the first keypress
                expStart_key_resp.keys = theseKeys[0]  # just the first key pressed
                expStart_key_resp.rt = expStart_key_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if expStart_key_resp.keys in ['', [], None]:  # No response was made
    expStart_key_resp.keys=None
thisExp.addData('expStart_key_resp.keys',expStart_key_resp.keys)
if expStart_key_resp.keys != None:  # we had a response
    thisExp.addData('expStart_key_resp.rt', expStart_key_resp.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "startFixation"-------
t = 0
startFixationClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
startFixationComponents = [fixationStart, p_port]
for thisComponent in startFixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "startFixation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = startFixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixationStart* updates
    if t >= 0.0 and fixationStart.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixationStart.tStart = t
        fixationStart.frameNStart = frameN  # exact frame index
        fixationStart.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixationStart.status == STARTED and t >= frameRemains:
        fixationStart.setAutoDraw(False)
    # *p_port* updates
    if t >= 0.0 and p_port.status == NOT_STARTED:
        # keep track of start time/frame for later
        p_port.tStart = t
        p_port.frameNStart = frameN  # exact frame index
        p_port.status = STARTED
        win.callOnFlip(p_port.setData, int(1))
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if p_port.status == STARTED and t >= frameRemains:
        p_port.status = STOPPED
        win.callOnFlip(p_port.setData, int(0))
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startFixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "startFixation"-------
for thisComponent in startFixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if p_port.status == STARTED:
    win.callOnFlip(p_port.setData, int(0))

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'blocksList.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "fixation_2"-------
    t = 0
    fixation_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [fixationTrial, p_port_2]
    for thisComponent in fixation_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixationTrial* updates
        if t >= 0.0 and fixationTrial.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationTrial.tStart = t
            fixationTrial.frameNStart = frameN  # exact frame index
            fixationTrial.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixationTrial.status == STARTED and t >= frameRemains:
            fixationTrial.setAutoDraw(False)
        # *p_port_2* updates
        if t >= 0.0 and p_port_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port_2.tStart = t
            p_port_2.frameNStart = frameN  # exact frame index
            p_port_2.status = STARTED
            win.callOnFlip(p_port_2.setData, int(5))
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if p_port_2.status == STARTED and t >= frameRemains:
            p_port_2.status = STOPPED
            win.callOnFlip(p_port_2.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_2"-------
    for thisComponent in fixation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_2.status == STARTED:
        win.callOnFlip(p_port_2.setData, int(0))
    
    # ------Prepare to start Routine "jitter1"-------
    t = 0
    jitter1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    jitter1Components = [jitt_1]
    for thisComponent in jitter1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "jitter1"-------
    while continueRoutine:
        # get current time
        t = jitter1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *jitt_1* updates
        if t >= 0.0 and jitt_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            jitt_1.tStart = t
            jitt_1.frameNStart = frameN  # exact frame index
            jitt_1.setAutoDraw(True)
        frameRemains = 0.0 + jitter1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if jitt_1.status == STARTED and t >= frameRemains:
            jitt_1.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jitter1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "jitter1"-------
    for thisComponent in jitter1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "jitter1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimulus"-------
    t = 0
    stimulusClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(17.000000)
    # update component parameters for each repeat
    stim.setImage(stimulus)
    stim.setSize((1,1))
    # keep track of which components have finished
    stimulusComponents = [text, stim, p_port_7]
    for thisComponent in stimulusComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimulus"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimulusClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 17.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # *stim* updates
        if t >= 0.0 and stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim.tStart = t
            stim.frameNStart = frameN  # exact frame index
            stim.setAutoDraw(True)
        frameRemains = 0.0 + 17.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if stim.status == STARTED and t >= frameRemains:
            stim.setAutoDraw(False)
        # *p_port_7* updates
        if t >= 0.0 and p_port_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port_7.tStart = t
            p_port_7.frameNStart = frameN  # exact frame index
            p_port_7.status = STARTED
            win.callOnFlip(p_port_7.setData, int(1))
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if p_port_7.status == STARTED and t >= frameRemains:
            p_port_7.status = STOPPED
            win.callOnFlip(p_port_7.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimulusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimulus"-------
    for thisComponent in stimulusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_7.status == STARTED:
        win.callOnFlip(p_port_7.setData, int(0))
    
    # ------Prepare to start Routine "jitter2"-------
    t = 0
    jitter2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    jitter2Components = [jitt_2]
    for thisComponent in jitter2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "jitter2"-------
    while continueRoutine:
        # get current time
        t = jitter2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *jitt_2* updates
        if t >= 0.0 and jitt_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            jitt_2.tStart = t
            jitt_2.frameNStart = frameN  # exact frame index
            jitt_2.setAutoDraw(True)
        frameRemains = 0.0 + jitter2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if jitt_2.status == STARTED and t >= frameRemains:
            jitt_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jitter2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "jitter2"-------
    for thisComponent in jitter2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "jitter2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback_3"-------
    t = 0
    feedback_3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    rating.reset()
    # keep track of which components have finished
    feedback_3Components = [scaleImage, rating, p_port_3]
    for thisComponent in feedback_3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback_3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *scaleImage* updates
        if t >= 0.0 and scaleImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            scaleImage.tStart = t
            scaleImage.frameNStart = frameN  # exact frame index
            scaleImage.setAutoDraw(True)
        frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if scaleImage.status == STARTED and t >= frameRemains:
            scaleImage.setAutoDraw(False)
        # *rating* updates
        if t >= 0.0 and rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating.tStart = t
            rating.frameNStart = frameN  # exact frame index
            rating.setAutoDraw(True)
        # *p_port_3* updates
        if t >= 0.0 and p_port_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port_3.tStart = t
            p_port_3.frameNStart = frameN  # exact frame index
            p_port_3.status = STARTED
            win.callOnFlip(p_port_3.setData, int(6))
        frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if p_port_3.status == STARTED and t >= frameRemains:
            p_port_3.status = STOPPED
            win.callOnFlip(p_port_3.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback_3"-------
    for thisComponent in feedback_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('rating.response', rating.getRating())
    trials.addData('rating.rt', rating.getRT())
    if p_port_3.status == STARTED:
        win.callOnFlip(p_port_3.setData, int(0))
    
    # set up handler to look after randomisation of conditions etc
    arrowsGame = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('arrows.xlsx'),
        seed=None, name='arrowsGame')
    thisExp.addLoop(arrowsGame)  # add the loop to the experiment
    thisArrowsGame = arrowsGame.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisArrowsGame.rgb)
    if thisArrowsGame != None:
        for paramName in thisArrowsGame.keys():
            exec(paramName + '= thisArrowsGame.' + paramName)
    
    for thisArrowsGame in arrowsGame:
        currentLoop = arrowsGame
        # abbreviate parameter names if possible (e.g. rgb = thisArrowsGame.rgb)
        if thisArrowsGame != None:
            for paramName in thisArrowsGame.keys():
                exec(paramName + '= thisArrowsGame.' + paramName)
        
        # ------Prepare to start Routine "arrow"-------
        t = 0
        arrowClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.750000)
        # update component parameters for each repeat
        ar_st.setImage(direction)
        key_resp_2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        arrowComponents = [ar_st, key_resp_2]
        for thisComponent in arrowComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "arrow"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = arrowClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ar_st* updates
            if t >= 0.0 and ar_st.status == NOT_STARTED:
                # keep track of start time/frame for later
                ar_st.tStart = t
                ar_st.frameNStart = frameN  # exact frame index
                ar_st.setAutoDraw(True)
            frameRemains = 0.0 + 0.75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if ar_st.status == STARTED and t >= frameRemains:
                ar_st.setAutoDraw(False)
            
            # *key_resp_2* updates
            if t >= 0.0 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 0.75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if key_resp_2.status == STARTED and t >= frameRemains:
                key_resp_2.status = STOPPED
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '4'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if key_resp_2.keys == []:  # then this was the first keypress
                        key_resp_2.keys = theseKeys[0]  # just the first key pressed
                        key_resp_2.rt = key_resp_2.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in arrowComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "arrow"-------
        for thisComponent in arrowComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys=None
        arrowsGame.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            arrowsGame.addData('key_resp_2.rt', key_resp_2.rt)
        
        # ------Prepare to start Routine "response"-------
        t = 0
        responseClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        key_resp_3 = event.BuilderKeyResponse()
        # keep track of which components have finished
        responseComponents = [key_resp_3]
        for thisComponent in responseComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "response"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = responseClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_3* updates
            if t >= 0.0 and key_resp_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_3.tStart = t
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if key_resp_3.status == STARTED and t >= frameRemains:
                key_resp_3.status = STOPPED
            if key_resp_3.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '4'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if key_resp_3.keys == []:  # then this was the first keypress
                        key_resp_3.keys = theseKeys[0]  # just the first key pressed
                        key_resp_3.rt = key_resp_3.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "response"-------
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys=None
        arrowsGame.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            arrowsGame.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'arrowsGame'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
