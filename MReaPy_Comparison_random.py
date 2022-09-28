from sws_pythoncommands import *
import time
from datetime import datetime

current = RPR_GetSelectedTrack(0, 0)

if "B| " in getname(current) or "A| " in getname(current) or "Root| " in getname(current):

    from MReaPy_Comparison_finish import identify_tracks
    trk_a = identify_tracks()[0]
    trk_b = identify_tracks()[1]
    trk_root = identify_tracks()[2]

    def mine_randomizer():
        now = datetime.now().time()  # time object
        now = str(now)
        now = float(now[-1])
        now = now / 2
        now = str(now)
        now = now[-1]
        # debug(now)

        if now == "5":
            now = 1
        else:
            now = 0
        return now

    if mine_randomizer() == 0:
        RPR_SetMediaTrackInfo_Value(trk_a, "B_MAINSEND", 1)
        RPR_SetMediaTrackInfo_Value(trk_b, "B_MAINSEND", 0)

    else:
        RPR_SetMediaTrackInfo_Value(trk_a, "B_MAINSEND", 0)
        RPR_SetMediaTrackInfo_Value(trk_b, "B_MAINSEND", 1)


    play_state = RPR_GetPlayState()
    if play_state == 1:
        pass
    elif play_state ==4:
        pass
    else:
        #play
        RPR_Main_OnCommandEx(40073,0,0)
