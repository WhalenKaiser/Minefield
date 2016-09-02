# write the function is_anagram
def is_anagram(test, original):
    grp1 = list(test)
    grp2 = list(original)

    for x in grp1:
        for y in grp2:
            if x == y:
                grp1.remove(x)
                grp2.remove(y)
        print (grp1, grp2)
            #if len(grp1)== 0 and len(grp2) == 0:
            #    return True
            #else:
            #    return False

is_anagram("creative","reactive")
