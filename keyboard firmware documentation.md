# Mechanical Keyboard Firmware Documentation

## Overview

This firmware runs my custom mechanical keyboard using a custom keyboard controller and CircuitPython firmware.

It handles:

- Full keyboard key input
- SSD1306 128×32 OLED display
- Per-key NeoPixel RGB LED lighting
- Full key matrix scanning
- USB keyboard input

Everything works together to handle typing input, visual feedback, and keyboard controls.

---

## Hardware

### Microcontroller

- Custom keyboard controller
- CircuitPython-compatible MCU

### Display

- SSD1306 OLED (128×32, I2C)
- Address: `0x3C`
- Framebuffer-based display driver

### Input

- Custom keyboard layout
- Full keyboard matrix
- Mechanical MX-style switches
- Diode-protected matrix

### Output

- Individual RGB LEDs assigned to each key
- Custom lighting effects and animations

---

## Pin Mapping

### Key Matrix

- Rows: Configured based on keyboard PCB layout
- Columns: Configured based on keyboard PCB layout
- Diode orientation: `COL2ROW`

### OLED (I2C)

- SDA: Configured GPIO pin
- SCL: Configured GPIO pin
- I2C Speed: 400 kHz

### RGB LEDs

- Data: Configured GPIO pin
- LED Count: Configured based on keyboard PCB

---

## Key System

Each key has:

- A physical switch position
- A keyboard keycode
- An RGB lighting position
- A matrix row and column location
- Optional custom behavior

### Current key actions

- Standard keyboard input
- Function keys
- Navigation keys
- Arrow keys
- Number pad support
- Modifier keys
- Media controls

---

## Key Press Behavior

When a key is pressed:

1. The matrix scanner detects the switch press.
2. The key debounce system confirms the input.
3. The keyboard sends the matching USB HID keycode.
4. The OLED updates with keyboard status.
5. The matching key LED animation starts.

When the key is released:

- The key state is cleared.
- The HID release signal is sent.
- The LED animation returns to the idle state.

---

## OLED System

The OLED uses a framebuffer-based driver.

### Features

- Text rendering
- Keyboard status display
- Layer information
- Animation support
- Direct I2C updates

---

## OLED Animation States

### Idle

- Shows the current time in `HH:MM`
- Shows keyboard status below
- Slightly moves the display content to prevent static appearance

### Key Press

- Displays the pressed key name.
- Shows keyboard activity feedback.
- Updates only when the screen state changes.

### Hold

- The key information remains displayed briefly.

### Fade Out

- The display clears with a smooth wipe animation.
- The OLED returns to the idle screen.

---

## LED System

The LED system controls all keyboard RGB LEDs.

### Behavior

- LEDs remain in the selected idle mode.
- Pressing a key starts a lighting animation.
- Each key can have its own RGB color.

### On Key Press

- The pressed key LED activates.
- Lighting effects spread across the keyboard.
- The selected key color is displayed.

### On Key Release

- LEDs return to the idle lighting state.
- Effects clear smoothly.

### How it Works

- The animation runs inside the keyboard main loop.
- It uses timed updates instead of blocking delays.
- Key scanning continues while effects are running.

---

## LED Animation Engine

The LEDs use a time-based animation system.

### Press Animation

- The pressed key lights first.
- The effect expands across nearby LEDs.
- Each LED uses its assigned color.

### Release Animation

- The effect fades away.
- LEDs return to their default state.

### Timing

- Animation frames update using timed intervals.
- No blocking delays are used.

---

## Keyboard Matrix

The keyboard uses a row and column scanning system.

### How it Works

- The firmware activates one row at a time.
- Column inputs are checked for switch presses.
- The pressed switch location is converted into a keycode.
- The HID report is sent over USB.

### Features

- Debouncing
- Multiple key support
- Modifier key handling
- Full keyboard compatibility

---

## USB HID System

The keyboard communicates as a standard USB keyboard device.

### Features

- Plug-and-play support
- Standard keyboard shortcuts
- Modifier support
- Media key support

---

## Performance

### OLED

- The display only updates when required.
- Animations control when each frame is drawn.

### LEDs

- LED animations run inside the keyboard scan loop.
- They do not interrupt typing.
- Updates happen asynchronously.

### Input

- Matrix scanning runs continuously.
- Key presses are detected with low latency.
- Multiple keys can be pressed simultaneously.

---

## System Flow

1. A key is pressed.
2. The matrix scanner detects the switch.
3. The firmware processes the key event.
4. The USB HID report is sent.
5. The OLED shows keyboard feedback.
6. The RGB LED animation starts.
7. The keyboard returns to the idle state.

---

## Summary

This firmware brings the entire keyboard system together.

It includes:

- Full keyboard support
- Custom matrix scanning
- OLED visual feedback
- RGB lighting effects
- USB HID keyboard output

Everything runs together so the input system, display, lighting, and keyboard controls stay synchronized.
