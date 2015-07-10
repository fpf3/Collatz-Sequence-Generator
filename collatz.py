#!/usr/bin/python
import time
import argparse

VERSION = 0.2

parser = argparse.ArgumentParser(description="Collatz Sequence Calculator", prog="CSG")
parser.add_argument("-m", "--mode", action="store", type=str, dest="mode", help="Set MODE to 'display' for slow output, 'fast' for quick calculation.")
parser.add_argument("-n", "--number", action="store", type=int, dest="input_n", help="Calculate sequence for 'INPUT_N'.")
parser.add_argument("-v", "--version", action="store_true", dest="version", help="Display version number.")
parser.add_argument("-o", "--output", action="store", type=str, dest="file_out", help="Output sequences to FILE. Can't be used with 'MODE=\"fast\"'.")
parser.add_argument("-s", "--start-from", action="store", type=int, dest="start_number", help="Start sequencer from START_NUMBER.")
parser.add_argument("-c", "--count-steps", action="store_true", dest="count_steps", help="Print out number of steps for sequence.")
args = parser.parse_args()

if args.version:
	print("CSG (Collatz Sequence Generator), v" + str(VERSION))
	exit()

if args.file_out:
	output_file = open(args.file_out, "a")

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

if args.input_n and args.mode == "fast":
	print("Error. You can either go fast or log. Not both.")

if args.start_number:
	n = args.start_number
else:
	n = 1

while(True):
	if args.mode != "fast":
		cn = collatz(n)
		n_string = str(n) + ": " + str(cn)
		if args.count_steps:
			n_string += " " + str(len(cn)) + " steps."
		print(n_string)
		if args.file_out:
			output_file.write(n_string)
	if args.mode == "display":
		time.sleep(2)
	n = n + 1
	
	if args.mode == "fast":
		print(n)
	
