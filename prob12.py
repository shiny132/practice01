firsts = [x for x in range(10)]
crap_count = [3, 6, 9]
crap = ""
for i in firsts[0:]:
    for j in firsts[1:]:
        if i in crap_count:
            crap+= "짝"
        if j in crap_count:
            crap+= "짝"
        if crap is not "":
            print("{}{} {}".format(i,j,crap) if i>0 else "{} {}".format(j,crap))
        crap = ""
