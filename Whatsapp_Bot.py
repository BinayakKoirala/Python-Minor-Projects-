import pywhatkit
from datetime import datetime

now = datetime.now()

print("-----------Welcome to Binayak Whatsapp Chat BOT------------")
chour = now.strftime("%H")
mobile = input('Enter Mobile No of Receiver along with country code : ')
message = input('Enter Message you wanna send : ')
hour = int(input('Enter hour in 24hr format: '))
minute = int(input('Enter minute : '))

pywhatkit.sendwhatmsg(mobile,message,hour,minute)