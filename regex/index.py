
import re
txt = "The rain in spain"
x = re.split("\s",txt) # returns a list where the string has been split at each match
print(x)

y= re.sub("\s","9",txt) #replaces the matches with the text of your choice
print(y)
print(re.search("ain",txt).start())