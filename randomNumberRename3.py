#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: Armin, Baltasar, Claudia
# expert of exercise block 1: teammember 1

import random
import time
import sys
import matplotlib.pyplot as plt

def get_random_number_with_randint(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(outputfilename + ".log", "a")
    f.write("Our randomly generated number is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()


def get_color_by_dice_roll(spots):
    colors = ["blue", "green", 'red', 'yellow', 'purple', 'orange']
    return colors[spots-1]


if __name__ == "__main__":
    outputfilename = "randomNumber"
    roll = get_random_number(1, 6)
    color = get_color_by_dice_roll(roll)
    write_log_file(outputfilename, color)

	rolls2 = []
	for i in range (6):
		roll= get_random_number(1,6)
		rolls2.append(roll)
		print(rolls2)
		sys.stdout.flush
		plt.barh(range(6), rolls)
		plt.show()
