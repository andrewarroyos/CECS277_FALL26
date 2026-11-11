# Group 16
# Andrew Arroyos
# Michael Sena
# CECS 277 - Lab 11 - Factory Method

import phone
import email

def main():
  # p = phone.Phone()
  # v = "1234567890"
  # print(p.clean(v))
  
  e = email.EmailValidator()
  em1 = "  coKe@bUsIn eSs.com "
  cleaned = e.clean(em1)
  print(e.validate(cleaned))
  

main()