import digitalio
_DIGITS = {
    0:   (1, 1, 1, 1, 1, 1, 0),
    1:   (0, 1, 1, 0, 0, 0, 0),
    2:   (1, 1, 0, 1, 1, 0, 1),
    3:   (1, 1, 1, 1, 0, 0, 1),
    4:   (0, 1, 1, 0, 0, 1, 1),
    5:   (1, 0, 1, 1, 0, 1, 1),
    6:   (1, 0, 1, 1, 1, 1, 1),
    7:   (1, 1, 1, 0, 0, 0, 0),
    8:   (1, 1, 1, 1, 1, 1, 1),
    9:   (1, 1, 1, 1, 0, 1, 1),
    'A': (1, 1, 1, 0, 1, 1, 1),
    'B': (0, 0, 1, 1, 1, 1, 1),
    'C': (1, 0, 0, 1, 1, 1, 0),
    'D': (0, 1, 1, 1, 1, 0, 1),
    'E': (1, 0, 0, 1, 1, 1, 1),
    'F': (1, 0, 0, 0, 1, 1, 1),
    'G': (1, 0, 1, 1, 1, 1, 1),
    'H': (0, 1, 1, 0, 1, 1, 1),
    'I': (0, 0, 0, 0, 1, 1, 0),
    'J': (0, 1, 1, 1, 1, 0, 0),
    'L': (0, 0, 0, 1, 1, 1, 0),
    'N': (1, 1, 1, 0, 1, 1, 0),
    'O': (1, 1, 1, 1, 1, 1, 0),
    'P': (1, 1, 0, 0, 1, 1, 1),
    'Q': (1, 1, 1, 0, 0, 1, 1),
    'R': (1, 0, 0, 0, 1, 1, 0),
    'S': (1, 0, 1, 1, 0, 1, 1),
    'T': (0, 0, 0, 1, 1, 1, 1),
    'U': (0, 1, 1, 1, 1, 1, 0),
    'Y': (0, 1, 1, 1, 0, 1, 1),
    'Z': (1, 1, 0, 1, 1, 0, 1),
    'a': (1, 1, 1, 1, 1, 0, 1),
    'b': (0, 0, 1, 1, 1, 1, 1),
    'c': (0, 0, 0, 1, 1, 0, 1),
    'd': (0, 1, 1, 1, 1, 0, 1),
    'e': (1, 1, 0, 1, 1, 1, 1),
    'f': (1, 0, 0, 0, 1, 1, 1),
    'g': (1, 1, 1, 1, 0, 1, 1),
    'h': (0, 0, 1, 0, 1, 1, 1),
    'i': (0, 0, 1, 0, 0, 0, 0),
    'j': (0, 1, 1, 1, 0, 0, 0),
    'l': (0, 0, 0, 1, 1, 1, 0),
    'n': (0, 0, 1, 0, 1, 0, 1),
    'o': (0, 0, 1, 1, 1, 0, 1),
    'p': (1, 1, 0, 0, 1, 1, 1),
    'q': (1, 1, 1, 0, 0, 1, 1),
    'r': (0, 0, 0, 0, 1, 0, 1),
    's': (1, 0, 1, 1, 0, 1, 1),
    't': (0, 0, 0, 1, 1, 1, 1),
    'u': (0, 0, 1, 1, 1, 0, 0),
    'y': (0, 1, 1, 1, 0, 1, 1),
    # ── Symbols ──────────────────────────────
    '-': (0, 0, 0, 0, 0, 0, 1),
    '_': (0, 0, 0, 1, 0, 0, 0),
    '.': (0, 0, 0, 0, 0, 0, 0),  # dp only — use dp=True
    '!': (0, 1, 1, 0, 0, 0, 0),  # like 1, dp=True for !
    '?': (1, 1, 0, 0, 1, 0, 1),
    "'": (0, 0, 0, 0, 0, 1, 0),
    '"': (0, 1, 0, 0, 0, 1, 0),
    '[': (1, 0, 0, 1, 1, 1, 0),
    ']': (1, 1, 1, 1, 0, 0, 0),
    '=': (0, 0, 0, 1, 0, 0, 1),
    '+': (0, 0, 1, 0, 1, 0, 1),
    '^': (1, 1, 0, 0, 0, 1, 0),
    ' ': (0, 0, 0, 0, 0, 0, 0),
}
class SevenSeg:
    def __init__(self, pins, common_anode=False):
        if len(pins)!=8:
            raise ValueError("Exactly 8 pins required: [a, b, c, d, e, f, g, dp]")
        self.common_anode=common_anode
        self._pins=[]
        for pin in pins:
            p = digitalio.DigitalInOut(pin)
            p.direction = digitalio.Direction.OUTPUT
            p.value = False
            self._pins.append(p)
        self.clear()
    def _write(self, segments, dp=False):
        for i, val in enumerate(segments):
            if self.common_anode:
                self._pins[i].value=not bool(val)
            else:
                self._pins[i].value=bool(val)
        if self.common_anode:
            self._pins[7].value=not bool(dp)
        else:
            self._pins[7].value=bool(dp)
    def show(self, char, dp=False):
        if isinstance(char, str) and len(char)==1 and char.isdigit():
            char=int(char)
        if char not in _DIGITS:
            raise  ValueError(f"Unsupported character: {char!r}")
        segments=_DIGITS[char]
        self._write(segments, dp)
    def clear(self):
        off=1 if self.common_anode else 0
        for p in self._pins:
            p.value=bool(off)
    def dot(self, on=True):
        if self.common_anode:
            self._pins[7].value=not bool(on)
        else:
            self._pins[7].value=bool(on)
    def deinit(self):
        self.clear()
        for pin in self._pins:
                pin.deinit()
    
