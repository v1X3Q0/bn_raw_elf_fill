justCause = """
enum e_type : uint16_t
{
    ET_NONE = 0x0,
    ET_REL = 0x1,
    ET_EXEC = 0x2,
    ET_DYN = 0x3,
    ET_CORE = 0x4,
    ET_NUM = 0x5
};

enum e_machine : uint16_t
{
    EM_NONE = 0x0,
    EM_M32 = 0x1,
    EM_SPARC = 0x2,
    EM_386 = 0x3,
    EM_68K = 0x4,
    EM_88K = 0x5,
    EM_860 = 0x7,
    EM_MIPS = 0x8,
    EM_S370 = 0x9,
    EM_MIPS_RS3_LE = 0xa,
    EM_PARISC = 0xf,
    EM_VPP500 = 0x11,
    EM_SPARC32PLUS = 0x12,
    EM_960 = 0x13,
    EM_PPC = 0x14,
    EM_PPC64 = 0x15,
    EM_S390 = 0x16,
    EM_V800 = 0x24,
    EM_FR20 = 0x25,
    EM_RH32 = 0x26,
    EM_RCE = 0x27,
    EM_ARM = 0x28,
    EM_FAKE_ALPHA = 0x29,
    EM_SH = 0x2a,
    EM_SPARCV9 = 0x2b,
    EM_TRICORE = 0x2c,
    EM_ARC = 0x2d,
    EM_H8_300 = 0x2e,
    EM_H8_300H = 0x2f,
    EM_H8S = 0x30,
    EM_H8_500 = 0x31,
    EM_IA_64 = 0x32,
    EM_MIPS_X = 0x33,
    EM_COLDFIRE = 0x34,
    EM_68HC12 = 0x35,
    EM_MMA = 0x36,
    EM_PCP = 0x37,
    EM_NCPU = 0x38,
    EM_NDR1 = 0x39,
    EM_STARCORE = 0x3a,
    EM_ME16 = 0x3b,
    EM_ST100 = 0x3c,
    EM_TINYJ = 0x3d,
    EM_X86_64 = 0x3e,
    EM_PDSP = 0x3f,
    EM_FX66 = 0x42,
    EM_ST9PLUS = 0x43,
    EM_ST7 = 0x44,
    EM_68HC16 = 0x45,
    EM_68HC11 = 0x46,
    EM_68HC08 = 0x47,
    EM_68HC05 = 0x48,
    EM_SVX = 0x49,
    EM_ST19 = 0x4a,
    EM_VAX = 0x4b,
    EM_CRIS = 0x4c,
    EM_JAVELIN = 0x4d,
    EM_FIREPATH = 0x4e,
    EM_ZSP = 0x4f,
    EM_MMIX = 0x50,
    EM_HUANY = 0x51,
    EM_PRISM = 0x52,
    EM_AVR = 0x53,
    EM_FR30 = 0x54,
    EM_D10V = 0x55,
    EM_D30V = 0x56,
    EM_V850 = 0x57,
    EM_M32R = 0x58,
    EM_MN10300 = 0x59,
    EM_MN10200 = 0x5a,
    EM_PJ = 0x5b,
    EM_OPENRISC = 0x5c,
    EM_ARC_A5 = 0x5d,
    EM_XTENSA = 0x5e,
    EM_ALTERA_NIOS2 = 0x71,
    EM_AARCH64 = 0xb7,
    EM_TILEPRO = 0xbc,
    EM_MICROBLAZE = 0xbd,
    EM_TILEGX = 0xbf,
    EM_NUM = 0xc0
};

enum p_flags : uint32_t
{
    PF_X = 0x1,
    PF_W = 0x2,
    PF_R = 0x4
};

enum p_type : uint32_t
{
    PT_NULL = 0x0,
    PT_LOAD = 0x1,
    PT_DYNAMIC = 0x2,
    PT_INTERP = 0x3,
    PT_NOTE = 0x4,
    PT_SHLIB = 0x5,
    PT_PHDR = 0x6,
    PT_TLS = 0x7,
    PT_NUM = 0x8,
    PT_LOOS = 0x60000000,
    PT_GNU_EH_FRAME = 0x6474e550,
    PT_GNU_STACK = 0x6474e551,
    PT_GNU_RELRO = 0x6474e552,
    PT_LOSUNW = 0x6ffffffa,
    PT_SUNWBSS = 0x6ffffffb,
    PT_SUNWSTACK = 0x6ffffffa,
    PT_MIPS_REGINFO = 0x70000000,
    PT_MIPS_RTPROC = 0x70000001,
    PT_MIPS_OPTIONS = 0x70000002,
    PT_MIPS_ABIFLAGS = 0x70000003
};

enum sh_flags : uint32_t
{
    SHF_WRITE = 0x1,
    SHF_ALLOC = 0x2,
    SHF_EXECINSTR = 0x4,
    SHF_MERGE = 0x10,
    SHF_STRINGS = 0x20,
    SHF_INFO_LINK = 0x40,
    SHF_LINK_ORDER = 0x80,
    SHF_OS_NONCONFORMING = 0x100,
    SHF_GROUP = 0x200,
    SHF_TLS = 0x400,
    SHF_COMPRESSED = 0x800,
    SHF_MASKOS = 0xff00000,
    SHF_ENTRYSECT = 0x10000000,
    SHF_COMDEF = 0x80000000
};

enum sh_type : uint32_t
{
    SHT_NULL = 0x0,
    SHT_PROGBITS = 0x1,
    SHT_SYMTAB = 0x2,
    SHT_STRTAB = 0x3,
    SHT_RELA = 0x4,
    SHT_HASH = 0x5,
    SHT_DYNAMIC = 0x6,
    SHT_NOTE = 0x7,
    SHT_NOBITS = 0x8,
    SHT_REL = 0x9,
    SHT_SHLIB = 0xa,
    SHT_DYNSYM = 0xb,
    SHT_LOUSER = 0x80000000,
    SHT_HIUSER = 0xffffffff,
    SHT_LOPROC = 0x70000000,
    SHT_HIPROC = 0x7fffffff
};

struct Elf32_Ident
{
    char signature[0x4];
    uint8_t file_class;
    uint8_t encoding;
    uint8_t version;
    uint8_t os;
    uint8_t abi_version;
    char pad[0x7];
};

struct Elf32_Header
{
    struct Elf32_Ident ident;
    enum e_type type;
    enum e_machine machine;
    uint32_t version;
    uint32_t entry;
    uint32_t program_header_offset;
    uint32_t section_header_offset;
    uint32_t flags;
    uint16_t header_size;
    uint16_t program_header_size;
    uint16_t program_header_count;
    uint16_t section_header_size;
    uint16_t section_header_count;
    uint16_t string_table;
};

struct Elf32_ProgramHeader
{
    enum p_type type;
    uint32_t offset;
    uint32_t virtual_address;
    uint32_t physical_address;
    uint32_t file_size;
    uint32_t memory_size;
    enum p_flags flags;
    uint32_t align;
};

struct Elf32_SectionHeader
{
    uint32_t name;
    enum sh_type type;
    enum sh_flags flags;
    uint32_t address;
    uint32_t offset;
    uint32_t size;
    uint32_t link;
    uint32_t info;
    uint32_t align;
    uint32_t entry_size;
};

"""

from .macro_to_enum import macro_to_enum_lines
from .add_header_binaryninja import add_header, add_header_by_blob
import os
import sys

def fix_linuxHeadTypes_h():
    setupprefix = os.path.dirname(os.path.realpath(__file__))
    lht = '{}linuxHeadTypes.h'.format(setupprefix + '/')
    f = open(lht, 'r')
    g = f.read()
    f.close()
    # simple tell if its already been configured
    g = macro_to_enum_lines(g, 'e_type', 'uint16_t', startdelim='ET_NONE', stopdelim='ET_HIPROC')
    g = macro_to_enum_lines(g, 'e_machine', 'uint16_t', startdelim='EM_NONE', stopdelim='EM_NUM')
    g = macro_to_enum_lines(g, 'p_flags', 'uint32_t', startdelim='PF_X', stopdelim='PF_R')
    g = macro_to_enum_lines(g, 'p_type', 'uint32_t', startdelim='PT_NULL', stopdelim='PT_HIPROC')
    g = macro_to_enum_lines(g, 'sh_flags', 'uint32_t', startdelim='SHF_WRITE', stopdelim='SHF_EXCLUDE')
    g = macro_to_enum_lines(g, 'sh_type', 'uint32_t', startdelim='SHT_NULL', stopdelim='SHT_HIUSER')
    g = macro_to_enum_lines(g, 'arm_relocs', 'uint8_t', startdelim='R_ARM_NONE', stopdelim='R_ARM_RBASE')
    g = macro_to_enum_lines(g, 'st_vis', 'uint8_t', startdelim='STV_DEFAULT', stopdelim='STV_PROTECTED')
    g = macro_to_enum_lines(g, 'st_bind', 'uint8_t', startdelim='STB_LOCAL', stopdelim='STB_HIPROC')
    g = macro_to_enum_lines(g, 'st_type', 'uint8_t', startdelim='STT_NOTYPE', stopdelim='STT_HIPROC')

    f = open(lht, 'w')
    f.write(g)
    f.close()

    return g

def grabLinuxElfTypes(bv):
    linuxdef_blob = fix_linuxHeadTypes_h()
    # we haven't imported our necessary structs yet, so import them.
    if bv.get_type_by_name("Elf_Ident") == None:
        add_header_by_blob(bv, linuxdef_blob)

# # would be awesome to have, unfortunately the width is 4 and binja enum types can't be smaller than 8
#     # ST_TYPE_enum = types.Enumeration()
#     # ST_TYPE_enum.append(name='R_ARM_CALL', value=0x1c)
#     # ST_TYPE_enum.append(name='R_ARM_JUMP24', value=0x1d)
#     # ST_TYPE_enum.append(name='R_ARM_V4BX', value=0x28)
#     # ST_TYPE_enum.append(name='R_ARM_PREL31', value=0x2a)
#     # ST_TYPE_enum.append(name='R_ARM_MOVW_ABS_NC', value=0x2b)
#     # ST_TYPE_enum.append(name='R_ARM_MOVT_ABS', value=0x2c)
#     # ST_TYPE_typeE = Type.enumeration_type(bv.platform.arch, ST_TYPE_enum, width=1, sign=False)
#     # bv.define_user_type('ST_TYPE', ST_TYPE_typeE)

#     Elf32_Sym_struct = types.Structure()
#     Elf32_Sym_struct.packed = True
#     Elf32_Sym_struct.alignment = 1
#     Elf32_Sym_struct.insert(0, Type.int(4, False), name='name')
#     Elf32_Sym_struct.insert(4, Type.int(4, False), name='value')
#     Elf32_Sym_struct.insert(8, Type.int(4, False), name='size')
#     Elf32_Sym_struct.insert(0xc, Type.int(1, False), name='info')
#     Elf32_Sym_struct.insert(0xd, Type.int(1, False), name='other')
#     Elf32_Sym_struct.insert(0xe, Type.int(2, False), name='shndx')
#     Elf32_Sym_typeS = Type.structure_type(Elf32_Sym_struct)
#     bv.define_user_type("Elf32_Sym", Elf32_Sym_typeS)

#     #define R_ARM_CALL		28
#     #define R_ARM_JUMP24		29
#     #define R_ARM_V4BX		40
#     #define R_ARM_PREL31		42
#     #define R_ARM_MOVW_ABS_NC	43
#     #define R_ARM_MOVT_ABS		44
#     R_TYPE_enum = types.Enumeration()
#     R_TYPE_enum.append(name='R_ARM_CALL', value=0x1c)
#     R_TYPE_enum.append(name='R_ARM_JUMP24', value=0x1d)
#     R_TYPE_enum.append(name='R_ARM_V4BX', value=0x28)
#     R_TYPE_enum.append(name='R_ARM_PREL31', value=0x2a)
#     R_TYPE_enum.append(name='R_ARM_MOVW_ABS_NC', value=0x2b)
#     R_TYPE_enum.append(name='R_ARM_MOVT_ABS', value=0x2c)
#     R_TYPE_typeE = Type.enumeration_type(bv.platform.arch, R_TYPE_enum, width=1, sign=False)
#     bv.define_user_type('R_TYPE', R_TYPE_typeE)

#     r_info_struct = types.Structure()
#     r_info_struct.packed = True
#     r_info_struct.alignment = 1
#     r_info_struct.insert(0, R_TYPE_typeE, name='r_type')
#     r_info_struct.append(Type.int(3, False), name='r_sym')
#     r_info_typeS = Type.structure_type(r_info_struct)
#     bv.define_user_type("r_info", r_info_typeS)

#     Elf32_Rel_struct = types.Structure()
#     Elf32_Rel_struct.packed = True
#     Elf32_Rel_struct.alignment = 1
#     Elf32_Rel_struct.append(Type.int(4, False), name='offset')
#     Elf32_Rel_struct.append(r_info_typeS, name='info')
#     Elf32_Rel_typeS = Type.structure_type(Elf32_Rel_struct)
#     bv.define_user_type("Elf32_Rel", Elf32_Rel_typeS)

#     Elf32_Vers_struct = types.Structure()
#     Elf32_Vers_struct.packed = True
#     Elf32_Vers_struct.alignment = 1
#     Elf32_Vers_struct.append(Type.int(4, False), name='CRC')
#     Elf32_Vers_struct.append(Type.array(Type.char(), 0x40 - 4), name='ext_name')
#     Elf32_Vers_typeS = Type.structure_type(Elf32_Vers_struct)
#     bv.define_user_type("Elf32_Vers", Elf32_Vers_typeS)
