print("source")

for i in range(256):
    print("{0:>3} in binary is {0:08b} and in hex is {0:>02x}".format(i))

print()

x = 0x20;  # hex number
print(x)  # 32
y = 0x0a
print(y)  # 10

a = 0b00101010  # binary
print(a)  # 42
print("{:08b}".format(a))
a = a << 2  # left shift
print(a)
print("{:08b}".format(a))
a = a >> 1  # right shift
print("{:08b}".format(a))

print()
# Challenge
powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)
print(powers)

x = int(input("Please enter a number: "))
printing = False
# convert to binary
for power in powers:
    bit = x // power
    if bit != 0:
        printing = True  # start printing after first non-zero
    if printing:
        print(bit, end='')
    x %= power
