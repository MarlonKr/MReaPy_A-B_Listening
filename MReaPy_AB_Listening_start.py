from sws_pythoncommands import *



trk_current = RPR_GetSelectedTrack(0,0)

if "B| " in getname(trk_current) or "A| " in getname(trk_current) or "Root| " in getname(trk_current) :

    from MReaPy_AB_Listening_finish import identify_tracks
    trk_a = identify_tracks()[0]
    trk_b = identify_tracks()[1]
    trk_root = identify_tracks()[2]

    if RPR_GetMediaTrackInfo_Value(trk_a, "B_MAINSEND") == 0:
        switch = 0
        RPR_SetMediaTrackInfo_Value(trk_a, "B_MAINSEND",1)

    else:
        switch = 1
        RPR_SetMediaTrackInfo_Value(trk_a,"B_MAINSEND", 0)


    RPR_SetMediaTrackInfo_Value(trk_b, "B_MAINSEND", switch)

    RPR_SetOnlyTrackSelected(trk_current)




else:

    input = UserInput("A/B Comparison", "Shall it be? y/n", 1, "y")
    if input == "y" or input == "Y":


        trk_current_name = getname(trk_current)
        RPR_GetSetMediaTrackInfo_String(trk_current, "P_NAME", f"Root| {trk_current_name}", 1)

        inserttrackabove()
        trk_a= RPR_GetSelectedTrack(0, 0)

        RPR_SetTrackColor(trk_a, 21004543)
        RPR_GetSetMediaTrackInfo_String(trk_a, "P_NAME", f"A| {trk_current_name}", 1)

        inserttrackabove()
        trk_b= RPR_GetSelectedTrack(0, 0)

        RPR_SetTrackColor(trk_b, 21004543)
        RPR_GetSetMediaTrackInfo_String(trk_b, "P_NAME", f"B| {trk_current_name}", 1)



        RPR_SetTrackSelected(trk_a, 1)
        RPR_SetTrackSelected(trk_b, 1)
        RPR_SetTrackSelected(trk_current, 1)



        RPR_SetMediaTrackInfo_Value(trk_a, "B_MAINSEND", 0)
        RPR_SetMediaTrackInfo_Value(trk_b, "B_MAINSEND", 1)
        RPR_SetMediaTrackInfo_Value(trk_current, "B_MAINSEND", 0)
        RPR_CreateTrackSend(trk_current, trk_b)
        RPR_CreateTrackSend(trk_current, trk_a)

        RPR_SetOnlyTrackSelected(trk_current)



    else:
        pass





