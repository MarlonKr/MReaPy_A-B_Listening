# MReaPy_A-B_Listening_Suite
A collection of interdependent action scripts for quick and reliable A/B listening, written in python. Automatically deploy routing structure, smooth and quickly switch between track A and B without clicks, functioning with TBProAudio's ABLM2 for equal loudness.


# What is it?
These are 4 intedependent working Reaper action scripts written in python, useable as shortcuts to 1) create a routing structure for A/B listening purposes, 2) quickly accept favourable FX(-chains) and continuing A/B lsitening with new FX, 3) randomly switching between track A and track B in order to overcome cognitive biases by not knowing which track is which, 4) reset routing to your former state by deleting track A and B.


# Tip
Use [https://www.tbproaudio.de/products/ablm](TBProAudio's ABLM2] plugin during A/B listening. By doing so, you can be sure there are virtually no loudness differences and you can quickly switch between A and B and determine whether your processing adds value or not. This script is fully compatible with AB/LM2 instances on a single up to all three tracks. Consider using my [MReapy_ABLM2_Extension](https://github.com/MarlonKr/MReaPy_ABLM2_Extension) for further convienience and a fast workflow.


# Use
## MReaPy_A/B_start
Creates 2 tracks, called "A| [track Title]" and "B| [track title]". The track that is supposed to be manipulated by deploying FX will be renamed to "Root| [track title]". Track "A" and track "B" both receive the signal of track "root", while one of them's main output is set "off" an one's set "on".

By selecting either track "A" or track "b" and re-triggering action script "MReapy_A/B_start", "main send" states of both tracks switch, so that one can quickly and - comparing to using the mute button - without any sample issues and therefore no to little clicks/artifacts. 

## MReaPy_A/B_move
Moves the selected track's FX chain to the "Root" track source. If AB_LM2 is available in each or in both of the tracks, the FX chain will automatically be set in between the two ABLM2 instances of track "Root" and be ignored in track "A"/track "B".

## MReaPy_A/B_random
Switches the "main send" of Track "A" and "Track"B" by chance, meaning either "main send" will switch on both tracks or stay the same. Use this to overcome possible coginitive bias, such as being sunken cost fallacies that tend you to favour the processed track because _it has to sound better_ because _it has been processed for minutes_. If playback is stopped before triggering this action, playback will automatically start, if playback is playing already, it will continue to play.

## MReapy_A/B_finish
Deletes track "A" and "B" and renames track "Root" from "Root| [track title" back to "[track title]".


# Installation 
## Requirements
- Python 3.9<
- Reaper [SWS/S&M Extension](https://www.sws-extension.org/) 

## Download 
Download all scripts from this repository and put them in the same folder. 

>sws_python.py and sws_pythoncommands.py are mandatory references that should always be in the same folder of my scripts. The sws_python.py script is the main reference for the Reaper API in order to work, sws_pythoncommands.py are handy functions I wrote for tedious tasks and are referenced in all my scripts (feel free to check them and use them for your own).

Next, add all or any of the scripts as needed using the action list window in Reaper.

>"Actions" → "Show Action List" → "New Action..." → "Load Reascript" → select file → execute or assign a shortcut.




