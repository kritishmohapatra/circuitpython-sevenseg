# SPDX-FileCopyrightText: 2026 Kritish Mohapatra
# SPDX-License-Identifier: MIT

import board
import time
from circuitpython_sevenseg import SevenSeg

seg = SevenSeg(
    pins=[board.GP2, board.GP3, board.GP4, board.GP5,
          board.GP6, board.GP7, board.GP8, board.GP9],
    common_anode=False
)

TEST_CHARS = [
    0,1,2,3,4,5,6,7,8,9,
    'A','B','C','D','E','F','G','H','I','J',
    'L','N','O','P','Q','R','S','T','U','Y','Z',
    'a','b','c','d','e','f','g','h','i','j',
    'l','n','o','p','q','r','s','t','u','y',
    '-','_','?',' ',
]

while True:
    for char in TEST_CHARS:
        print(f"Showing: {repr(char)}")
        seg.show(char)
        time.sleep(0.8)
    seg.clear()
    time.sleep(1)
