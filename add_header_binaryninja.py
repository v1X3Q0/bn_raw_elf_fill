import re
def add_header(justCause_name):
    f = open(justCause_name, "r")
    justCause = f.read()
    justCauseNew = ""
    for i in justCause.split("\n"):
        i = ' ' + i
        i = i.replace('\t', ' ')
        i = re.sub(' +', ' ', i)
        if i[0] == ' ':
            i = i[1:]
        spaced_i = i.split(' ')
        if ('struct' in spaced_i) and (';' not in i):
            if ("__nopack" not in i):
                spaced_i.append(' __packed')
        justCauseNew += " ".join(spaced_i) + '\n'
    # print(justCauseNew)
    justCause = justCauseNew    
    f.close()
    typeList = bv.platform.parse_types_from_source(justCause)
    for i in typeList.types:
        curName = i.name[0]
        bv.define_user_type(curName, typeList.types[curName])
