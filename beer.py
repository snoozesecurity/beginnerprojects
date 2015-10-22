# Problem taken from r/beginnerprojects
# Inefficient code by SnoozeSecurity (youtube.com/channel/UCa5QaVWjwFkUNoLtMka1d3w)
# I am not a professional programmer, rather someone trying to learn python :)

lyrics = 'bottles of beer on the wall! '
lyrics2 = 'bottles of beer! Take one down, pass it around, '
lyrics3 = 'bottle of beer on the wall! '
lyrics4 = 'bottle of beer! Take it down, pass it around, '

now = 99
next = 98

while now < 100:
        if next > 1:
                print now, lyrics, now, lyrics2, next, lyrics
                now = next
                next = next - 1
        elif next == 1:
                print now, lyrics, now, lyrics2, next, lyrics3
                now = next
                next = next - 1
        elif next == 0:
                print now, lyrics3, now, lyrics4, next, lyrics
                break


