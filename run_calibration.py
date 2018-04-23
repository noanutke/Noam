#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on April 22, 2018, at 11:04
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
from psychopy.tools.filetools import fromFile

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import calibration





# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'feedbackInTheMagnet'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}

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
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

calibration_object = calibration.Calibration(expInfo['participant']);
# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 720), fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
startNewLocation = visual.TextStim(win=win, name='startNewLocation',
                                   text=u'Start VAS tests for new location',
                                   font=u'Arial',
                                   pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                   color=u'white', colorSpace='rgb', opacity=1,
                                   depth=-1.0);

# Initialize components for Routine "stimulus"
stimulusClock = core.Clock()
text = visual.TextStim(win=win, name='text',
                       text=u'+',
                       font=u'Arial',
                       pos=(0, 0), height=0.6, wrapWidth=None, ori=0,
                       color=u'white', colorSpace='rgb', opacity=1,
                       depth=0.0);
p_port_7 = parallel.ParallelPort(address='0x0378')

# Initialize components for Routine "painFeedbackRoutine"
painFeedbackRoutineClock = core.Clock()
p_port_3 = parallel.ParallelPort(address='0x0378')
painRatingText = visual.TextStim(win=win, name='painRatingText',
                                 text=u'Insert pain rating (0-10)',
                                 font=u'Arial',
                                 pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                 color=u'white', colorSpace='rgb', opacity=1,
                                 depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# set up handler to look after randomisation of conditions etc
locationsLoop = data.TrialHandler(nReps=8, method='sequential',
                                  extraInfo=expInfo, originPath=-1,
                                  trialList=[None],
                                  seed=None, name='locationsLoop')
thisExp.addLoop(locationsLoop)  # add the loop to the experiment
thisLocationsLoop = locationsLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLocationsLoop.rgb)
if thisLocationsLoop != None:
    for paramName in thisLocationsLoop.keys():
        exec (paramName + '= thisLocationsLoop.' + paramName)

for thisLocationsLoop in locationsLoop:
    currentLoop = locationsLoop
    # abbreviate parameter names if possible (e.g. rgb = thisLocationsLoop.rgb)
    if thisLocationsLoop != None:
        for paramName in thisLocationsLoop.keys():
            exec (paramName + '= thisLocationsLoop.' + paramName)

    # ------Prepare to start Routine "welcome"-------
    t = 0
    welcomeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    expStart_key_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    welcomeComponents = [expStart_key_resp, startNewLocation]
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "welcome"-------
    while continueRoutine:
        # get current time
        t = welcomeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

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

        # *startNewLocation* updates
        if t >= 0.0 and startNewLocation.status == NOT_STARTED:
            # keep track of start time/frame for later
            startNewLocation.tStart = t
            startNewLocation.frameNStart = frameN  # exact frame index
            startNewLocation.setAutoDraw(True)

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
        expStart_key_resp.keys = None
    locationsLoop.addData('expStart_key_resp.keys', expStart_key_resp.keys)
    if expStart_key_resp.keys != None:  # we had a response
        locationsLoop.addData('expStart_key_resp.rt', expStart_key_resp.rt)
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential',
                               extraInfo=expInfo, originPath=-1,
                               trialList=data.importConditions(u'VAS_order1.xlsx'),
                               seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec (paramName + '= thisTrial.' + paramName)

    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec (paramName + '= thisTrial.' + paramName)

        # ------Prepare to start Routine "stimulus"-------
        t = 0
        stimulusClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.700000)
        # update component parameters for each repeat
        # keep track of which components have finished
        stimulusComponents = [text, p_port_7]
        for thisComponent in stimulusComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "stimulus"-------
        calibration_object.runVAS(vas)
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
            frameRemains = 0.0 + 1.70 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if text.status == STARTED and t >= frameRemains:
                text.setAutoDraw(False)
            # *p_port_7* updates
            if t >= 0.0 and p_port_7.status == NOT_STARTED:
                # keep track of start time/frame for later
                p_port_7.tStart = t
                p_port_7.frameNStart = frameN  # exact frame index
                p_port_7.status = STARTED
                win.callOnFlip(p_port_7.setData, int(1))
            frameRemains = 0.0 + 1.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
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

        # ------Prepare to start Routine "painFeedbackRoutine"-------
        t = 0
        painFeedbackRoutineClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        painRating = event.BuilderKeyResponse()
        # keep track of which components have finished
        painFeedbackRoutineComponents = [p_port_3, painRating, painRatingText]
        for thisComponent in painFeedbackRoutineComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "painFeedbackRoutine"-------
        while continueRoutine:
            # get current time
            t = painFeedbackRoutineClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *p_port_3* updates
            if t >= 0.0 and p_port_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                p_port_3.tStart = t
                p_port_3.frameNStart = frameN  # exact frame index
                p_port_3.status = STARTED
                win.callOnFlip(p_port_3.setData, int(6))
            frameRemains = 0.0 + 8 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if p_port_3.status == STARTED and t >= frameRemains:
                p_port_3.status = STOPPED
                win.callOnFlip(p_port_3.setData, int(0))

            # *painRating* updates
            if t >= 0.0 and painRating.status == NOT_STARTED:
                # keep track of start time/frame for later
                painRating.tStart = t
                painRating.frameNStart = frameN  # exact frame index
                painRating.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(painRating.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if painRating.status == STARTED:
                theseKeys = event.getKeys(keyList=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'space'])

                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    painRating.keys = theseKeys[-1]  # just the last key pressed
                    painRating.rt = painRating.clock.getTime()
                    calibration_object.updateRating(painRating.keys)
                    # a response ends the routine
                    continueRoutine = False

            # *painRatingText* updates
            if t >= 0.0 and painRatingText.status == NOT_STARTED:
                # keep track of start time/frame for later
                painRatingText.tStart = t
                painRatingText.frameNStart = frameN  # exact frame index
                painRatingText.setAutoDraw(True)

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in painFeedbackRoutineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "painFeedbackRoutine"-------
        for thisComponent in painFeedbackRoutineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if p_port_3.status == STARTED:
            win.callOnFlip(p_port_3.setData, int(0))
        # check responses
        if painRating.keys in ['', [], None]:  # No response was made
            painRating.keys = None
        trials.addData('painRating.keys', painRating.keys)
        if painRating.keys != None:  # we had a response
            trials.addData('painRating.rt', painRating.rt)
        # the Routine "painFeedbackRoutine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    # completed 1 repeats of 'trials'

    thisExp.nextEntry()

# completed 8 repeats of 'locationsLoop'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + '.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
