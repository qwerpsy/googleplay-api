# separator used by search.py, categories.py, ...
SEPARATOR = ";"

LANG            = "en_US" # can be en_US, fr_FR, ...
ACCOUNT = [
	{
		'ANDROID_ID'      : None, # "xxxxxxxxxxxxxxxx" 
		'GOOGLE_LOGIN'    : None, # "username@gmail.com" 
		'GOOGLE_PASSWORD' : None, # "yyyyyyyyy"
		'AUTH_TOKEN'      : None
	} 
]

#proxy setting
proxies = None 	#  { "http":"xxxxxxx", "https":"xxxxxxx" }

# force the user to edit this file
if any([each == None for each in [ACCOUNT[0]['ANDROID_ID']], ACCOUNT[0]['GOOGLE_LOGIN'], ACCOUNT[0]['GOOGLE_PASSWORD']]):
    raise Exception("config.py not updated")


