from datetime import datetime

age = int(input('How old are you ? '))
year_birth = datetime.now().year-age
print("You was born back in %s"%year_birth)