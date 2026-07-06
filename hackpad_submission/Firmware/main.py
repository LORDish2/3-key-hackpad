import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# Switches are wired directly from GPIO pins to GND.
# Update these pins if you change the KiCad schematic.
keyboard.matrix = KeysScanner(
    pins=(board.D8, board.D9, board.D10),
    value_when_pressed=False,
    pull=True,
)

keyboard.keymap = [
    [
        KC.MPLY,
        KC.MNXT,
        KC.MPRV,
    ]
]

if __name__ == "__main__":
    keyboard.go()
