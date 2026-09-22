import re

# match example
name = 'Prince Gupta'
srh = re.match(r'[pP]', name)
if srh: print('Match Found.')


# search University name
myself = 'Hello! I am Prince, I am Persuing my MCA at Marwadi University gfdg hgfhgh'
university = re.search(r'[mM][\w]+\s[\w]+y', myself)
print('Uni name: ', university.group())

# Date search
dt = 'Current time is 11:02am now.'
timesearch = re.search(r'[0-9]{2}:[0-9]{2}[ap]m', dt)
if timesearch:
    print('Time search: ', timesearch.group())


# findall email
data = "my email is princegupta7698@gmail.com  hgfsefd gfywd ehgey e vivek@yahoomail.com"
# re.compile(r'[a-z0-9]*@[a-z]+.[a-z]+')
search = re.findall(r'[a-z0-9]*@[a-z]+.[a-z]+', data)
print('Email : ',search)

