import re
def das(inp):
    ref = ""
    par = re.compile(r"[A-Z][a-z]+")
    wrd = par.findall(inp)
    for i, w in enumerate(wrd):
        if i == 0:
            res += w.casefold()
        else:
            res += "_" + w.casefold()
    return res