from binaryninja.interaction import get_open_filename_input, get_text_line_input
from binaryninja.log import log_alert, log_error, log_info, log_warn
from binaryninja.binaryview import BinaryView
import re
import os

def add_header_by_blob(bv, justCause):
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
    typeList = bv.platform.parse_types_from_source(justCause)
    for i in typeList.types:
        curName = i.name[0]
        bv.define_user_type(curName, typeList.types[curName])

def add_header(bv, justCause_name):
    f = open(justCause_name, "r")
    justCause = f.read()
    f.close()
    add_header_by_blob(bv, justCause)

def add_header_p(bv: BinaryView):
    destination_path = get_open_filename_input('target header')
    
    if os.path.exists(destination_path) == False:
        log_error('no header provided')
        return
    
    add_header(bv, destination_path)