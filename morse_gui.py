from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
import time

# number of the pin for LED

led = 8

def setup_led_pin_out(led_pin):
    GPIO.setup(led_pin, GPIO.OUT)

def pin_setup():
    GPIO.setmode(GPIO.BOARD)
    setup_led_pin_out(led)

def entry_valid(text):
    if len(text) <= 12:
        return True
    else:
        return False

def exit_program():
    GPIO.cleanup()
    main_window.destroy()

# a dict to store our dictionary of alphabet to morse code

morse_code = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'P': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': ' ',
    "'": '.----.',
    '(': '-.--.-',
    ')': '-.--.-',
    ',': '--..--',
    '-': '-....-',
    '.': '.-.-.-',
    '/': '-..-.',
    ':': '---...',
    ';': '-.-.-.',
    '?': '..--..',
    '_': '..--.-'}

pin_setup()

main_window = Tk()
main_window.title('Morse Translator')
entry_validation = main_window.register(entry_valid)

my_font = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')

entry_content = StringVar()
entry_field = Entry(main_window, textvariable = entry_content, width = 15, validate = 'key', validatecommand = (entry_validation, '%P'))
entry_field.grid(row = 0, column = 0)

submit_button = Button(main_window, text = 'SUBMIT', font = my_font, command = translate_text, bg = 'grey', height = 1, width = 15)
submit_button.grid(row = 1, column = 0)

main_window.protocol('WM DELETE WINDOW', exit_program)
main_window.mainloop()
