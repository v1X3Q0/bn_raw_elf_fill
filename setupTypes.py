Elf32_Sym_struct = types.Structure()
Elf32_Sym_struct.insert(0, Type.int(4, False), name='name')
Elf32_Sym_struct.insert(4, Type.int(4, False), name='value')
Elf32_Sym_struct.insert(8, Type.int(4, False), name='size')
Elf32_Sym_struct.insert(0xc, Type.int(1, False), name='info')
Elf32_Sym_struct.insert(0xd, Type.int(1, False), name='other')
Elf32_Sym_struct.insert(0xe, Type.int(2, False), name='shndx')
Elf32_Sym_typeS = Type.structure_type(Elf32_Sym_struct)
bv.define_user_type("Elf32_Sym", Elf32_Sym_typeS)

#define R_ARM_CALL		28
#define R_ARM_JUMP24		29
#define R_ARM_V4BX		40
#define R_ARM_PREL31		42
#define R_ARM_MOVW_ABS_NC	43
#define R_ARM_MOVT_ABS		44
R_TYPE_enum = types.Enumeration()
R_TYPE_enum.append(name='R_ARM_CALL', value=0x1c)
R_TYPE_enum.append(name='R_ARM_JUMP24', value=0x1d)
R_TYPE_enum.append(name='R_ARM_V4BX', value=0x28)
R_TYPE_enum.append(name='R_ARM_PREL31', value=0x2a)
R_TYPE_enum.append(name='R_ARM_MOVW_ABS_NC', value=0x2b)
R_TYPE_enum.append(name='R_ARM_MOVT_ABS', value=0x2c)
R_TYPE_typeE = Type.enumeration_type(bv.platform.arch, R_TYPE_enum, width=1, sign=False)
bv.define_user_type('R_TYPE', R_TYPE_typeE)

r_info_struct = types.Structure()
r_info_struct.insert(0, R_TYPE_typeE, name='r_type')
r_info_struct.append(Type.int(3, False), name='r_sym')
r_info_typeS = Type.structure_type(r_info_struct)
bv.define_user_type("r_info", r_info_typeS)

Elf32_Rel_struct = types.Structure()
Elf32_Rel_struct.append(Type.int(4, False), name='offset')
Elf32_Rel_struct.append(r_info_struct, name='info')
bv.define_user_type("Elf32_Rel", Elf32_Rel_struct)
