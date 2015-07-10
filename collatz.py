#!/usr/bin/python
import time
import argparse

VERSION = 0.2

parser = argparse.ArgumentParser(description="Collatz Sequence Calculator", prog="CSG")
parser.add_argument("-m", "--mode", action="store", type=str, dest="mode", help="Set mode to 'display' for slow output, 'fast' for quick calculation")
parser.add_argument("-n", "--number", action="store", type=int, dest="input_n", help="Calculate sequence for 'INPUT_N'")
parser.add_argument("-v", "--version", action="store_true", dest="version", help="Display version number.")

args = parser.parse_args()

if args.version:
	print("CSG (Collatz Sequence Generator), v" + str(VERSION))
	exit()

def collatz(n):
	start_n = n
	sequence = []
	while(True):
		sequence.append(n)
		if n == 1:
			return sequence
		if n < start_n and args.mode == "fast":
			sequence.append("...")
			return sequence
		if n % 2 == 1:
			n = int((n * 3) + 1)
			continue
		if n % 2 == 0:
			n = int(n / 2)

if args.input_n:
	print(str(args.input_n) + ": " + str(collatz(args.input_n)))
	exit()

n = 1

while(True):
	if args.mode != "fast":
		print(str(n) + ": " + str(collatz(n)))
	if args.mode == "display":
		time.sleep(2)
	n = n + 1
	
	if args.mode == "fast":
		print(n)
	
