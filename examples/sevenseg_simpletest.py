# SPDX-FileCopyrightText: 2026 Kritish Mohapatra
# SPDX-License-Identifier: MIT

"""
Simple test for circuitpython-sevenseg library.
Counts 0-9 on a single digit 7-segment display.

Hardware:
    - Raspberry Pi Pico / Pico 2W
    - Single digit 7-segment display (common cathode)

Wiring:
    segment a → GP2
    segment b → GP3
    segment c → GP4
    segment d → GP5
    segment e → GP6
    segment f → GP7
    segment g → GP8
    segment dp → GP9
"""

import board
import time
from circuitpython_sevenseg import SevenSeg

seg = SevenSeg(
    pins=[board.GP2, board.GP3, board.GP4, board.GP5,
          board.GP6, board.GP7, board.GP8, board.GP9],
    common_anode=False
)

while True:
    for digit in range(10):
        print(f"Showing: {digit}")
        seg.show(digit)
        time.sleep(0.8)
    seg.clear()
    time.sleep(0.5)
