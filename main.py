#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import time
from datetime import datetime

from masterpiece import Masterpiece


if __name__ == "__main__":
    dtime = datetime.now()
    ans_time = time.mktime(dtime.timetuple())
    params_file = open("song_settings.json", "r")
    params = json.load(params_file)
    params_file.close()
    my_masterpiece = Masterpiece(
        rules_path="rules.json",
        length=params["length"],
        tempo=params["tempo"])
    subfolder = "output"
    if not os.path.isdir(subfolder):
        os.mkdir(subfolder)
    my_masterpiece.create_midi_file("{folder}/midi_{suffix}.mid".format(
        folder=subfolder,
        suffix=ans_time))
