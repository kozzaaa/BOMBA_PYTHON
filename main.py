# Tutaj importujemy sleep aby można było zrobić opóżnienie.

from time import sleep

# Zmiena od inputa np: sendMessage,
# input jest to funkcja dzięki której możemy coś napisać dla zmieniej: sendMessage

sendMessage = input("Podaj tekst który ma się wyświetlać: ")

# Pentla to taki pojemnik w którym przechowujemy informacje i
# możemy go jakoś nazwać np: name.

# Range czyli: Podaje sekwencję liczb na podstawie podanego indeksu początku i końca

for name in range(1,11):
    sleep(1)
    print("Za", name)
print(sendMessage)

# sleep: jest to wcześniej
# zaimportowana funckja która daje opóźnienie.
# print jest to funckja która wyświetla jakieś informacje.

