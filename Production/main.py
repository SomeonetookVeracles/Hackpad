import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.col_pins = (
    board.GP1,   # Button 1
    board.GP2,   # Button 2  
    board.GP3,   # Button 3
    board.GP4,   # Button 4
    board.GP6,   # Button 5 
    board.GP7,   # Button 6
    board.GP8,   # Button 7
    board.GP11,  # Button 8 (encoder button)
)


encoder_handler = EncoderHandler()

encoder_handler.pins = (
    (board.GP10, board.GP9, None, False), 
)

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),  
]

keyboard.modules.append(encoder_handler)

keyboard.keymap = [
    [
        KC.F1,      # Button 1 - Function key F1
        KC.F2,      # Button 2 - Function key F2
        KC.F3,      # Button 3 - Function key F3
        KC.F4,      # Button 4 - Function key F4
        KC.F5,      # Button 5 - Function key F5
        KC.F6,      # Button 6 - Function key F6
        KC.F7,      # Button 7 - Function key F7
        KC.MUTE,    # Button 8 (encoder button) - Mute
    ]
]


if __name__ == '__main__':
    keyboard.go()
