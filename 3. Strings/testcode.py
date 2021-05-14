# Python 3 program to find
# n'th term in look and
# say sequence

# Returns n'th term in
# look-and-say sequence
def countnndSay(n):
	
	# Base cases
	if (n == 1):
		return "1"
	if (n == 2):
		return "11"

	# Find n'th term by generating
	# all terms from 3 to n-1.
	# Every term is generated using
	# previous term
	
	# Initialize previous term
	s = "11"
	for i in range(3, n + 1):
		
		# In below for loop,
		# previous character is
		# processed in current
		# iteration. That is why
		# a dummy character is
		# added to make sure that
		# loop runs one extra iteration.
		s += '$'
		l = len(s)

		cnt = 1 # Initialize count
				# of matching chars
		tmp = "" # Initialize i'th
				# term in series

		# Process previous term to
		# find the next term
		for j in range(1 , l):
			
			# If current character
			# does't match
			if (s[j] != s[j - 1]):
				
				# Append count of
				# str[j-1] to temp
				tmp += str(cnt + 0)

				# Append str[j-1]
				tmp += s[j - 1]

				# Reset count
				cnt = 1
			
			# If matches, then increment
			# count of matching characters
			else:
				cnt += 1

		# Update str
		s = tmp
	return s

# Driver Code
N = 9
print(countnndSay(N))

# This code is contributed
# by ChitraNayal
