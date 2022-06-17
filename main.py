from time import sleep
count = 0

while count < 5:
  if count == 0:
    print("Hello.")
  elif count == 1:
    print("Hello?")
  elif count == 2:
    print("Hey dude.")
  elif count == 3:
    print("C\'mon. Hello!")
  elif count == 4:
    print("Ah, there you are.")
  count += 1 ; sleep(1.5)
