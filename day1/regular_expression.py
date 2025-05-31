import re   #inbuilt library for regular expression -> search(pattern, target), split(), findall(), sub()

pattern = r"anuj"

name = "anuj dangi"

result = re.search(pattern, name)

if result:
    print("Match found!")
else:
    print("Match not found!")

#Example no 2

string = "My phone number is : 1234567890"
pattern = "[0-9]{10}"

result = re.search(pattern, string)

if result:
    print("Phone number found : ", result.group())
else:
    print("No match")

# Special Sequence	Meaning	Example
# \d	Matches any digit character (0-9)	"123" matches "\d\d\d"
# \D	Matches any non-digit character	"hello" matches "\D\D\D\D\D"
# \w	Matches any word character (a-z, A-Z, 0-9, and _)	"hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"
# \W	Matches any non-word character	"@#$%" matches "\W\W\W\W"
# \s	Matches any whitespace character (space, tab, newline, etc.)	"hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"
# \S	Matches any non-whitespace character	"hello_world" matches "\S\S\S\S\S\S\S\S\S\S\S"
# \b	Matches the boundary between a word character and a non-word character	"cat" matches "\bcat\b" in "The cat sat on the mat"
# \B	Matches any position that is not a word boundary	"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"