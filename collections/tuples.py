# sets and tuples are immutable
t = "a", "b", "c"  # tuple ('a', 'b', 'C')
print(t)
print(type(t))

l = ["a", "b", "c"]  # list ['a', 'b', 'C']
print(l)
print(type(l))

print("a", "b", "c")  # string a b c
print(("a", "b", "c"))  # tuple

t2 = ("a", "b", "c")  # tuple
print(t2)
print(type(t2))

welcome = "Welcom to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974  # notice theres no coma between first two parameters
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
# metallica[0]="Reload" # error, tuples are immutable
# correct way to modify tuple - create a new one with old params
metallica = "Reload", metallica[1], metallica[2]
print(metallica)
metallica2 = metallica  # error too
print(metallica == metallica2)
print(metallica is metallica2)

print()
# multiple initialization
a = b = c = d = 12
print(c)
# assigned different values to different variables
a, b = 12, 13
print("a={}, b={}".format(a, b))
# easy swap!
a, b = b, a
print("a={}, b={}".format(a, b))

# that way you can extract parameters from tuples (called unpacking)
title, artist, year = metallica
print("title={}\nartist={}\nyear={}".format(title, artist, year))

# You can also unpack lists
rammstein = ["Sehnsucht", "Rammstein", 1997]
title, artist, year = rammstein
print()
print("title={}\nartist={}\nyear={}".format(title, artist, year))
rammstein.append("Neue Deutsche Harte")
# title, artist, year = rammstein # error! not enough variables to unpack a list!

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)
print(imelda)
# unpack
title, artist, years, tracks = imelda
print(title)
print(artist)
print(years)
print(tracks)  # tuple of tuples
for song in tracks:
    track, title = song
    # print("\t", song)
    print("\tTack number {}, Title: {}".format(track, title))

imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")]
)

# now tracks is tuple that contains list of tuples
# thus it can be now edited (list)
title, artist, years, tracks = imelda
print(tracks)
tracks.append((5, "Du Hast"))
print(tracks)
