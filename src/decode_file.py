import json
import matplotlib.pyplot as plt
import numpy as np

from phd import viz
import sys
import os
import traceback
# from pydantic import BaseModel

colors, swatches = viz.phd_style(jupyterStyle=True, grid=True)
%config InlineBackend.figure_formats = ['svg']
from dataclasses import dataclass

from snsphd.obj import DataObj
from model import Model, Result, Result1, IntegrationResult, Results


@dataclass
class CHB:
    _52: Model
    _53: Model
    _54: Model
    _55: Model
    _56: Model
    _57: Model
    _58: Model
    _59: Model
    
@dataclass
class CHA:
    _35: CHB
    _36: CHB
    _37: CHB
    _38: CHB
    _39: CHB
    _40: CHB
    _41: CHB
    _42: CHB


data_set = {}
chA_list = [35,36,37,38,39,40,41,42]
chB_list = [52,53,54,55,56,57,58,59]
object_a_set = []
for chA in chA_list:
    data_set[chA] = {}
    path = "../data/8ch_Feb24th/"
    object_b_set = []
    for chB in chB_list:
        try:
            with open(os.path.join(path, f"4.0A_{chA}_{chB}.json"), 'r') as file:
                data = json.load(file)
            # data_set[chA][chB] = DataObj(os.path.join(path, f"4.0A_{chA}_{chB}.json"))
            
            # object_b_set.append(DataObj(os.path.join(path, f"4.0A_{chA}_{chB}.json")))
            object_b_set.append(Model(**data))
            
        except:
            # traceback.print_exc()
            object_b_set.append(None)
            # data = {}
            # data_set[chA][chB] = data
            
    channel_B = CHB(*object_b_set)
    object_a_set.append(channel_B)
    
full = CHA(*object_a_set)

full._35._59.results[3]