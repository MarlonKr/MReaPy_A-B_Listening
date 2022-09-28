from sws_pythoncommands import *


def identify_tracks():
    trk_selected = RPR_GetSelectedTrack(0, 0)

    if "A| " in getname(trk_selected):
        # global trk_a
        trk_a = trk_selected

        trk_to_find = "B| "
        validation = True
    elif "B| " in getname(trk_selected):
        # global trk_b
        trk_b = trk_selected

        trk_to_find = "A| "
        validation = True
    else:
        validation = False

    if validation == False:
        debug("no A/B track selected")
        pass

    else:
        ### Find trk_root
        trk_root_name = RPR_GetTrackReceiveName(trk_selected, 0, "", 1000)[3]

        i = 0
        while RPR_GetTrack(0, i) != mediatracknumberError():
            trk_current = RPR_GetTrack(0, i)
            if getname(trk_current) == trk_root_name:
                # global trk_root
                trk_root = trk_current
                break
            else:
                pass

            i += 1

        ### find trk_a or b
        def identify_a_or_b(a_or_b):
            i = 0
            while i < 20:
                # global trk_identify_name
                trk_identify_name = RPR_GetTrackSendName(trk_root, i, "", 1000)[3]

                if a_or_b in trk_identify_name:

                    i = 0
                    while i != mediatracknumberError():
                        if getname(RPR_GetTrack(0, i)) == trk_identify_name:
                            global trk_identify
                            trk_identify = RPR_GetTrack(0, i)
                            break
                        else:
                            i += 1
                            pass
                    break

                else:

                    i += 1
                    pass

        if trk_to_find == "A| ":
            identify_a_or_b("A| ")
            # global trk_a
            trk_a = trk_identify



        elif trk_to_find == "B| ":
            identify_a_or_b("B| ")
            # global trk_b
            trk_b = trk_identify
        else:
            debug("something went wrong")

        return trk_a, trk_b, trk_root




if __name__ == "__main__":

    input = UserInput("delete comparison", "do you want to continue? y/n", 1, "y")

    if input == "y":

        ### identify selected track

        trk_a = identify_tracks()[0]
        trk_b = identify_tracks()[1]
        trk_root = identify_tracks()[2]
        RPR_DeleteTrack(trk_a)
        RPR_DeleteTrack(trk_b)
        name = getname(trk_root)
        name = name.split("Root| ")[1]
        rename(trk_root, name)
        RPR_SetMediaTrackInfo_Value(trk_root, "B_MAINSEND", 1)


    else:
        pass