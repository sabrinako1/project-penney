RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
BLACK = '\033[30;47m'
DIM = '\033[2m'
BOLD = '\033[1m'
RESET = '\033[0m'
DIM_GREY = "\033[2;90m"
DIM_RED = "\033[2;31m"

import random
import sys
import time
import math
from prompt_toolkit import prompt, print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

'█ ▛ ▙ ▜ ▟ ▀ ▘▝ ▌▖▄ ▖▕'

penney = rf"""
{BOLD}{DIM}{RED}░█▛▀█▌░█▛▀▀▘░█▙░█▌░█▙░█▌░█▛▀▀▘░█▌░█▌
{BOLD}{DIM}{RED}░█▙▄█▌░█▙▄  ░█▛▙█▌░█▛▙█▌░█▙▄  ░█▙▄█▌ 
{BOLD}{DIM}{RED}░█▌   ░█▙▄▄▖░█▌░█▌░█▌░█▌░█▙▄▄▖  ▄▄█▌
""".split('\n')

def random_card(*stat_lines):
	choices = [str(x + 2) for x in range(9)]
	choices.extend(['J', 'Q', 'K', 'A'])
	card_number = random.choice(choices)

	suits = [(RED, 'spade'), (RED, 'club'), (RED, 'diamond'), (RED, 'heart')]
	color, suit = random.choice(suits)

	spaces = ' ' * 4


	card_number = '67'
	card = f"""
{DIM}.──────────.{RESET}
{DIM}▏{RESET}{color}{card_number.ljust(2)}        {RESET}{BOLD}{DIM}▕{RESET}{spaces}{penney[1]}{RESET}
{DIM}▏{RESET}{color}   ▂  ▂   {RESET}{DIM}▕{RESET}{spaces}{penney[2]}{RESET}
{DIM}▏{RESET}{color}  ▐█▙▟█▌  {RESET}{DIM}▕{RESET}{spaces}{penney[3]}{RESET}
{DIM}▏{RESET}{color}   ▜██▛   {RESET}{DIM}▕{RESET}
{DIM}▏{RESET}{color}    ▜▛    {RESET}{DIM}▕{RESET}{DIM}{spaces}{stat_lines[0][0]}
{DIM}▏{RESET}{color}        {card_number.rjust(2)}{RESET}{BOLD}{DIM}▕{RESET}{BOLD}{spaces}{stat_lines[0][1]}
{DIM}'──────────'{RESET}
"""
	print(card)

def take_input(deck_count):
	random_card(
		('Current deck count', deck_count)
		)
	# print(f'{DIM}Current deck count: {RESET}{BOLD}{deck_count}{RESET}\n')
	print()
	print(f'{RED}█ {RESET}{BOLD}Input number of new simulations')
	# print_formatted_text(FormattedText([
	#     ("fg:ansired", "█ "),
	#     ("bold", "Input number of new simulations"),
	# ]))

	invalid = False

	while True:

		if invalid:
			placeholder = ("fg:#873636", "  Invalid")
		else:
			placeholder = ("fg:ansibrightblack", "  Press enter to quit")

		print('\n\33[2A')
		number = prompt([
			('fg:ansired', '█'),
			('fg:ansibrightred bold', ' → ')],
			 placeholder=[placeholder]
		).strip()

		if not number:
			break

		try:
			number = int(number)
			break

		except ValueError:
			sys.stdout.write("\033[1A\r\033[K")
			sys.stdout.flush()
			invalid = True
			# print(f'{BOLD}{RED}→ {DIM}Invalid {RESET}', end='', flush=True)
			# time.sleep(1)
			# sys.stdout.write("\r\033[K")
			# sys.stdout.flush()


	return number

def start_simulating():
	sys.stdout.write("\x1b[1A\r\x1b[2K")
	sys.stdout.write("\x1b[1A\r\x1b[2K")

	sys.stdout.flush()

	print(f'{RED}█ {RESET}{BOLD}Simulating…\n')

	# print_formatted_text(FormattedText([
	#     ("fg:ansired", "█ "),
	#     ("bold", "Simulating…"),
	# ]))

	update_progress(0, 1)


def update_progress(complete, total):

	sys.stdout.write("\033[1A\r\033[K")
	sys.stdout.flush()

	boxes = 25
	num = math.floor(complete / total * boxes)
	complete_boxes = '█' * num
	incomplete_boxes = '█' * (boxes - num)
	bar = f'{RED}█ {RESET}{RED}|{complete_boxes}{RESET}{DIM_RED}{incomplete_boxes}{RESET}{RED}|{RESET}'
	print(f'\r{bar}')

def reset():
	sys.stdout.write("\033[13A\r\033[K")
