# dama = int(input())


# if dama < -273:
#     print("")
# elif dama > 6000:
#     print("")
# elif dama >= 101:
#     print("Steam")
# elif dama <= 0:
#     print("Ice")
# elif dama >= 1:
#     print("Water")
# elif dama <= 100:
#     print("Water")

dama = int(input())

if dama < 0:
    print("Ice")
else:
    if dama <= 100:
        print("Water")
    else:
        print("Steam")
