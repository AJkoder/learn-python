#regex- to find a pattern
import re
text = "My email is aj123@gmail.com and my phone is 9876543210"
phone=re.search(r"\d{10}",text)
email=re.search("[\w,-]+@[\w.-]",text)
print(phone.group(),email.group())