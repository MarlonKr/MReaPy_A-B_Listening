from sws_pythoncommands import *

if "A| " in getname(RPR_GetSelectedTrack(0,0)) or "B| " in getname(RPR_GetSelectedTrack(0,0)):

    input = UserInput("A/B move FX-Chain", "do you want to continue?", 1, "y")
    if input == "y":
        from MReaPy_AB_Listening_finish import identify_tracks

        trk_root = identify_tracks()[2]

        def check_ablm2():
            if RPR_TrackFX_GetByName(trk_selected, "ABLM2", 0) != -1:
                trk_selected_ablm = True
            else:
                trk_selected_ablm = False

            if RPR_TrackFX_GetByName(trk_root ,"ABLM2",0) != -1:
                trk_root_ablm= True
            else:
                trk_root_ablm= False

            return trk_selected_ablm, trk_root_ablm

        trk_selected = RPR_GetSelectedTrack(0, 0)

        trk_selected_fx_count = RPR_TrackFX_GetCount(trk_selected)
        trk_root_fx_count = RPR_TrackFX_GetCount(trk_root)

        if check_ablm2()[0] == True and check_ablm2()[1] == True:
            fxsrc_int = trk_selected_fx_count - 2
            fxdest_int = trk_root_fx_count - 1
            while fxsrc_int >= 1:
                RPR_TrackFX_CopyToTrack(trk_selected, fxsrc_int, trk_root, fxdest_int, True)
                fxsrc_int -= 1

        if check_ablm2()[0] == False and check_ablm2()[1] == False:
            fxsrc_int = trk_selected_fx_count
            fxdest_int = trk_root_fx_count
            while fxsrc_int >= 0:
                RPR_TrackFX_CopyToTrack(trk_selected, fxsrc_int, trk_root, fxdest_int, True)
                fxsrc_int -= 1

        if check_ablm2()[0] == False and check_ablm2()[1] == True:
            fxsrc_int = trk_selected_fx_count
            fxdest_int = trk_root_fx_count - 1
            while fxsrc_int >= 0:
                RPR_TrackFX_CopyToTrack(trk_selected, fxsrc_int, trk_root, fxdest_int, True)
                fxsrc_int -= 1

        if check_ablm2()[0] == True and check_ablm2()[1] == False:
            fxsrc_int = trk_selected_fx_count - 2
            fxdest_int = trk_root_fx_count
            while fxsrc_int >= 1:
                RPR_TrackFX_CopyToTrack(trk_selected, fxsrc_int, trk_root, fxdest_int, True)
                fxsrc_int -= 1

    else:
        pass

else:
    debug("No A/B track selected")
    pass