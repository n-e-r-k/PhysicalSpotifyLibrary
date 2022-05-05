#PSL Writer

from PSL import PSL

main = PSL('/home/pi/credentials.csv', connect = False)
main.load()

amount = int(input("How many cards are being written?:"))
for i in range(amount):
    uri = input(f"Please enter the uri for card {i}.:")
    main.write(uri)
    print(f"Card {i} write complete.\n")

main.save()