# This method will disect any string input and check for commonly used SQL
# injection statements.
# name = raw_input("Hi. What's your name? ")
# print name

if ("," or "OR" or "'1'") in [STRING_TO_BE_TESTED]:
	print """\tYou are using , in your id.
	Why are you tring to hack me?"""
else:
	print "Your ID is ok"

# input("\n\nPress the enter key to exit.")