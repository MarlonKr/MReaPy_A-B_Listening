# MReaPy_A-B_Listening_Suite
A collection of interdependent action scripts for fast and reliable A/B listening, written in Python. Automatically provides routing structure, smooth and fast switching between track A and B without clicks, fully compatible with TBProAudio's ABLM2 for equal loudness.


# What is it?
These are 4 independently working Reaper action scripts written in Python that can be used as shortcuts to 1) create a routing structure for A/B listening purposes, 2) quickly accept favorable FX(chains) to continue further processing and A/B listening, 3) randomly switch between track A and track B to overcome cognitive biases, 4) reset the routing to the previous state by deleting track A and B.


# Tip
During A/B listening, use the plugin [ABLM2 from TBProAudio](https://www.tbproaudio.de/products/ablm). This way you can be sure that there are virtually no loudness differences and you can more reliably determine whether your processing adds value or not. This script is fully compatible with AB/LM2 instances on one to all three tracks. Consider using my [MReapy_ABLM2_Extension](https://github.com/MarlonKr/MReaPy_ABLM2_Extension) for more convenience and a quick workflow.


# Use
## MReaPy_A/B_start
Creates 2 tracks, called "A| [track title]" and "B| [track title]". The track with the sound source is renamed "Root| [track title]" and its "main send" is set to "off". Tracks "A" and "B" both receive the signal from track "Root", with the main output of one track set to "off" and that of the other track set to "on". 

If you now select either track "A" or track "b" and trigger the action script "MReapy_A/B_start" again, the "Main Send" states of both tracks change, so that you can work quickly and - unlike when using the mute button - without sample problems and thus with little to no clicks/artifacts. 

## MReaPy_A/B_move
Moves the FX chain of the selected track to the "root" track source. If AB_LM2 is available in each or both tracks, the FX chain is automatically placed between the two ABLM2 instances of track "Root" and ignored in track "A"/track "B".

## MReaPy_A/B_random
Randomly toggles the "Main Send" of Track "A" and "Track "B", i.e. either the "Main Send" is toggled on both tracks or remains the same. By doing so while not looking at the "main send" state, you are forced to your ears identifying the processed track. Use this action frequently when listening A/B to overcome possible cognitive biases, such as the fallacy that you tend to favor the edited track because _it must sound better_ because _it has been edited for minutes_. If playback is stopped before this action is triggered, playback will start automatically; if playback is already in progress, it will continue.

## MReapy_A/B_finish
Deletes tracks "A" and "B" and renames the track "Root" from "Root| [track title]" back to "[track title]".


# Installation 
## Requirements
- Python 3.9<
- Reaper [SWS/S&M Extension](https://www.sws-extension.org/) 

## Download 
Download all scripts from this repository and put them in the same folder. 

>sws_python.py and sws_pythoncommands.py are mandatory references that should always be in the same folder of my scripts. The sws_python.py script is the main reference for the Reaper API in order to work, sws_pythoncommands.py are handy functions I wrote for tedious tasks and are referenced in all my scripts (feel free to check them and use them for your own).

Next, add all or any of the scripts as needed using the action list window in Reaper.

>"Actions" → "Show Action List" → "New Action..." → "Load Reascript" → select file → execute or assign a shortcut.




