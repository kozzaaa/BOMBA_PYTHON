# Tutaj importujemy sleep aby można było zrobić opóżnienie.

from time import sleep

# Zmiena od inputa np: sendMessage,
# input jest to funkcja dzięki której możemy coś napisać dla zmieniej: sendMessage

sendMessage = input("Podaj tekst który ma się wyświetlać: ")

# Pentla to taki pojemnik w którym przechowujemy informacje i
# możemy go jakoś nazwać np: name.

for name in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
    sleep(1)
    print(name, "sekunda")
print(sendMessage)

# sleep: jest to wcześniej
# zaimportowana funckja która daje opóźnienie.
# print jest to funckja która wyświetla jakieś informacje.

