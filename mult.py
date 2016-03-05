# Problem taken from r/beginnerprojects
# Code written by SnoozeSecurity (youtube.com/channel/UCa5QaVWjwFkUNoLtMka1d3w)

import sys

# Initialize nums list and get amount of terms to display from user

nums = []
getNums = raw_input("How many terms in the multiplication table? Enter 1-15: ")

# Verify valid integer entry, 1-15

try:
	getNums = int(getNums)
except (TypeError, NameError, ValueError):
	print "Invalid entry - Goodbye!"
	sys.exit(1)
	
if (getNums < 1 or getNums > 15):
	print "Invalid entry - Goodbye!"
	sys.exit(1)
	
# Create incrementing nums list

for i in range(getNums):
	nums.append(i)

print "\t", # Spacing

# Horizontal print

for i in range(len(nums)):
	print "\t", nums[i],

print "\n", # Spacing

# Separation of numbers in multiplication table

print "________", 
for i in range(len(nums)):
	sys.stdout.write("________")
	
print "" # Spacing

# Prints results in multiplication table, accounts for spacing

for i in range(len(nums)):
	print nums[i], "\t|\t",
	for j in range(len(nums)):
		print nums[i] * nums[j], "\t",
	print "\n\t|"