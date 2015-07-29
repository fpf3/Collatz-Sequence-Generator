import Pyro4, argparse

"""
start_number = 1

parser = argparse.ArgumentParser(description="Coordinator for distributed collatz sequence generator", prog="csgd")
parser.add_argument("-s", "--start-from", action="store", type=int, dest="start_number", help="Start sequencer from START_NUMBER.")

args = parser.parse_args()

start_number = args.start_number
"""

class Collatz_Coordinator:
	def __init__(self, start):
		self.position = start
		self.completed_segments = [(0,self.position)]
	
	def get_segment(self, n):
		return (self.position,  self.position + n)

	def register_segment(self, seg):
		if seg[1] < seg[0]:
			return "Error: Malformed segment."

		for i in self.completed_segments:
			if seg[1] >= i[0] and seg[1] <= i[1]:
				if seg[0] < i[0]:
					self.completed_segments.append((seg[0],i[0]-1))
					Print("Added segment {0}".format((seg[0],i[0]-1)))
					return "Added partial segment."
				if seg[0] >= i[0]:
					return "Segment already calculated!"

			elif seg[0] >= i[0] and  seg[0] <= i[1]:
				if seg[1] > i[1]:
					self.completed_segments.append((i[1]+1,seg[1]))
					return "Added partial segment."
				if seg[1] <= i[1]:
					return "Segment already calculated!"
		
		self.completed_segments.append(seg)
		return "Added segment."

	
"""
def main(start_number):
	Pyro4.Daemon.serveSimple(
		{
		Collatz_Coordinator(start_number): "coordinator"
		},
		ns = True)

if __name__ == "__main__":
	main(start_number)

"""




