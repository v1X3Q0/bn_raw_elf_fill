import re
def macro_to_enum(line):
    argindex = 0
    param = False
    lp = re.search(r'(#define[\ \t]+)([a-zA-Z0-9_]+)[\ \t]+((0x)?[a-fA-F0-9]+)[\ \t]*(.*)', line)
    if lp == None:
        lp = re.search(r'(#define[\ \t]+)([a-zA-Z0-9_]+)[\ \t]+(\((.+)\))[\ \t]*(.*)', line)
        if lp == None:
            return line
        param = True
    lpgs = lp.groups()
    
    # take care of #define
    argindex += 1

    enumname = lpgs[argindex]
    # take care of the enumname
    argindex += 1

    if param == False:
        if '0x' in lpgs[argindex]:
            # had a hex prefix, add to get the real value
            enumvalue = int(lpgs[argindex], 0x10)
            argindex += 1
        else:
            enumvalue = int(lpgs[argindex], 10)
            argindex += 1
    else:
        # just pull the paranthesis
        enumvalue = lpgs[argindex]
        argindex += 1

    # take care of the enum value
    argindex += 1

    enumcomment = lpgs[argindex]

    linefinal = '\t{} = {}, {}'.format(enumname, enumvalue, enumcomment)

    return linefinal

def macro_to_enum_lines(blob, enum_type, enum_size=None, startdelim=None, stopdelim=None):
    lines = blob.split('\n')
    parse_active = False
    opencomment = False
    indexcount = 0
    filelist = []
    if enum_size == None:
        enum_size = 'uint32_t'
    for line in lines:
        if parse_active == False:
            if (startdelim != None) and (startdelim in line):
                enum_type_line = 'enum {} : {}'.format(enum_type, enum_size)
                filelist.append(enum_type_line)
                filelist.append('{')
                parse_active = True
            else:
                filelist.append(line)
        if parse_active == True:
            mae = macro_to_enum(line)
            filelist.append(mae)
            if (stopdelim != None) and (stopdelim in line):
                parse_active = False
                indexcount += 1
                # make sure we close comment before closing braket
                if ('/*' in mae) and ('*/' not in mae):
                    while(indexcount < len(lines)):
                        filelist.append(lines[indexcount])
                        if '*/' in lines[indexcount]:
                            indexcount += 1
                            break
                        indexcount += 1
                filelist.append('};')
                filelist = filelist + lines[indexcount:]
                break
        indexcount += 1
    else:
        if parse_active == True:
            filelist.append('};')
            parse_active = False
    return filelist

def macro_to_enum_file(filein, enum_type, enum_size=None, fileout=None, startdelim=None, stopdelim=None):
    if fileout == None:
        fileout = filein
    f = open(filein, 'r')
    g = f.read()
    f.close()
    newmaelines = macro_to_enum_lines(g, enum_type, enum_size, startdelim, stopdelim)
    f = open(fileout, 'w')
    for line in newmaelines:
        f.write('{}\n'.format(line))
    f.close()