import os
from sys import getallocatedblocks
from bs4 import BeautifulSoup
import requests
import time
import getTeamRankingTemplate


statCategoryIds = [28, 27, 699, 701, 700, 702, 785, 786, 790, 791, 756, 926, 876, 697, 877, 698, 694, 693, 458, 456, 463, 96, 98, 459, 457, 25, 695, 741, 462, 97, 704, 703, 24, 23, 468, 696, 465, 40, 466, 467, 705, 22, 21, 29, 460, 461, 742]

for stat in statCategoryIds:
    teamList = getTeamRankingTemplate.main(stat)
    time.sleep(1)
    for statToAdd in teamList:
        print(statToAdd)
