import re

# search University name
myself = 'Hello! I am Prince, I am Persuing MCA at Marwadi University and...'
university = re.search(r'[mM][\w]+\s[\w]+y', myself)
print(university.group())
