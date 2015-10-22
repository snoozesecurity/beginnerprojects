# Problem taken from r/beginnerprojects
# Inefficient code by SnoozeSecurity (youtube.com/channel/UCa5QaVWjwFkUNoLtMka1d3w)
# I am not a professional programmer, rather someone trying to learn python :)

text = 'Input the side of a triangle, 0 or negative to quit: '
text2 = 'y to continue, any other character to quit: '
while True:
        hyp = 0
        a = 0
        b = 0
        int1 = input(text)
        if int1 > 0:
                int2 = input(text)
                if int2 > 0:
                        int3 = input(text)
                        if int3 <= 0:
                                print 'Illegal triangle!'
                                break
                else:
                        print 'Illegal triangle!'
                        break
        else:
                print 'Illegal triangle!'
                break
        if int1 > hyp:
                hyp = int1
                a = int2
                b = int3
        if int2 > hyp:
                hyp = int2
                a = int1
                b = int3
        if int3 > hyp:
                hyp = int3
                a = int1
                b = int2
        sum = (a*a) + (b*b)
        c2 = (hyp*hyp)
        if sum == c2:
                print 'Pythagorean Triple!'
        else:
                print 'Not a Pythagorean Triple!'
        proceed = raw_input(text2)
        if proceed != 'y':
                break

print 'Thanks for playing!'
