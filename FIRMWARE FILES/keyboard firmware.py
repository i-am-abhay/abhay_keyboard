# code.py
# ANSI 104 Keyboard Placeholder
# Matrix + OLED + RGB LEDs

import time
import board
import busio
import displayio
import terminalio

from digitalio import DigitalInOut, Direction, Pull
import neopixel

import adafruit_displayio_ssd1306
from adafruit_display_text import label


# ==================================================
# OLED DISPLAY
# ==================================================

displayio.release_displays()

# Change pins if needed
i2c = busio.I2C(
    board.D5,   # SCL
    board.D4,   # SDA
    frequency=400000
)

display_bus = displayio.I2CDisplay(
    i2c,
    device_address=0x3C
)

display = adafruit_displayio_ssd1306.SSD1306(
    display_bus,
    width=128,
    height=32
)

screen = displayio.Group()

text = label.Label(
    terminalio.FONT,
    text="ANSI 104 Keyboard",
    x=0,
    y=8
)

screen.append(text)

display.root_group = screen


# ==================================================
# RGB LEDS
# ==================================================

# Change pin and count
LED_PIN = board.D10
LED_COUNT = 104

pixels = neopixel.NeoPixel(
    LED_PIN,
    LED_COUNT,
    brightness=0.2,
    auto_write=True
)

# Startup placeholder lighting
for i in range(LED_COUNT):
    pixels[i] = (20, 20, 20)

time.sleep(1)

pixels.fill((0, 0, 0))


# ==================================================
# ANSI 104 KEYMAP PLACEHOLDER
# ==================================================

KEYMAP = [

    # Function row
    [
        "ESC",
        "F1","F2","F3","F4",
        "F5","F6","F7","F8",
        "F9","F10","F11","F12"
    ],

    # Number row
    [
        "`","1","2","3","4",
        "5","6","7","8",
        "9","0","-","=",
        "BACKSPACE"
    ],

    # Q row
    [
        "TAB",
        "Q","W","E","R","T",
        "Y","U","I","O","P",
        "[","]","\\"
    ],

    # Home row
    [
        "CAPS",
        "A","S","D","F","G",
        "H","J","K","L",
        ";","'",
        "ENTER"
    ],

    # Bottom row
    [
        "SHIFT_L",
        "Z","X","C","V","B",
        "N","M",
        ",",".","/",
        "SHIFT_R"
    ],

    # Space row
    [
        "CTRL_L",
        "WIN_L",
        "ALT_L",
        "SPACE",
        "ALT_R",
        "FN",
        "CTRL_R"
    ],

    # Navigation
    [
        "INSERT",
        "HOME",
        "PAGE_UP",
        "DELETE",
        "END",
        "PAGE_DOWN"
    ],

    # Arrows
    [
        "UP",
        "LEFT",
        "DOWN",
        "RIGHT"
    ],

    # Numpad
    [
        "NUM_LOCK",
        "NUM/",
        "NUM*",
        "NUM-",
        "NUM7",
        "NUM8",
        "NUM9",
        "NUM+",
        "NUM4",
        "NUM5",
        "NUM6",
        "NUM1",
        "NUM2",
        "NUM3",
        "NUM_ENTER",
        "NUM0",
        "NUM."
    ]
]


# ==================================================
# MATRIX PLACEHOLDER
# ==================================================

ROWS = []
COLS = []


def scan_keyboard():
    """
    Add matrix scanning here:
    - set row pins
    - read columns
    - send HID reports
    """
    pass


# ==================================================
# MAIN LOOP
# ==================================================

while True:

    scan_keyboard()

    # OLED heartbeat placeholder
    text.text = "ANSI 104 Keyboard"

    time.sleep(0.01)
