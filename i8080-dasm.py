#!/usr/bin/env python3
import struct, sys, argparse

class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

class writer():
    def __init__(self, _file):
        self.hook = open(_file, 'w')
    def write(self, string):
        self.hook.write(string)
    def close(self):
        self.hook.close()

def case(*args):
    return any((arg == switch.value for arg in args))

def dasm8080(code, pc, _writer, _listing):
    opcode = code[pc]
    bytes = '%02x' % (opcode)
    size = 1
    while switch(opcode):
        if case(0x00):
            mnemonic = 'NOP'
            break
            
        if case(0x01):
            mnemonic = 'LXI\tB, #$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0x02):
            mnemonic = 'STAX\tB'
            break
        
        if case(0x03):
            mnemonic = 'INX\tB'
            break
        
        if case(0x04):
            mnemonic = 'INR\tB'
            break
        
        if case(0x05):
            mnemonic = 'DCR\tB'
            break
        
        if case(0x06):
            mnemonic = 'MVI\tB, #$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0x07):
            mnemonic = 'RLC'
            break
        
        if case(0x08):
            mnemonic = 'DB $%02x\t;ILLEGAL' % (opcode)
            break
        
        if case(0x09):
            mnemonic = 'DAD\tB'
            break
        
        if case(0x0A):
            mnemonic = 'LDAX\tB'
            break
        
        if case(0x0B):
            mnemonic = 'DCX\tB'
            break
        
        if case(0x0C):
            mnemonic = 'INR\tC'
            break
        
        if case(0x0D):
            mnemonic = 'DCR\tC'
            break
        
        if case(0x0E):
            mnemonic = 'MVI\tC, #$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0x0F):
            mnemonic = 'RRC'
            break
        
        if case(0x10):
            mnemonic = 'DB $%02x\t;ILLEGAL' % (opcode)
            break
        
        if case(0x11):
            mnemonic = 'LXI\tD, #$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0x12):
            mnemonic = 'STAX\tD'
            break
        
        if case(0x13):
            mnemonic = 'INX\tD'
            break
        
        if case(0x14):
            mnemonic = 'INR\tD'
            break
        
        if case(0x15):
            mnemonic = 'DCR\tD'
            break
        
        if case(0x16):
            mnemonic = 'MVI\tD, #$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0x17):
            mnemonic = 'RAL'
            break
        
        if case(0x18):
            mnemonic = 'DB $%02x\t;ILLEGAL' % (opcode)
            break
        
        if case(0x19):
            mnemonic = 'DAD\tD'
            break
        
        if case(0x1A):
            mnemonic = 'LDAX\tD'
            break
        
        if case(0x1B):
            mnemonic = 'DCX\tD'
            break

        if case(0x1C):
            mnemonic = 'INR\tE'
            break
        
        if case(0x1D):
            mnemonic = 'DCR\tE'
            break
        
        if case(0x1E):
            mnemonic = 'MVI\tE, #$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0x1F):
            mnemonic = 'RAR'
            break
        
        if case(0x20):
            mnemonic = 'DB $%02x\t;ILLEGAL' % (opcode)
            break
        
        if case(0x21):
            mnemonic = 'LXI\tH, #$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0x22):
            mnemonic = 'SHLD\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0x23):
            mnemonic = 'INX\tH'
            break
            
        if case(0x24):
            mnemonic = 'INR\tH'
            break
        
        if case(0x25):
            mnemonic = 'DCR\tH'
            break
        
        if case(0x26):
            mnemonic = 'MVI\tH, #$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0x27):
            mnemonic = 'DAA'
            break
            
        if case(0x28):
            mnemonic = 'DB $%02x\t;ILLEGAL' % (opcode)
            break
        
        if case(0x29):
            mnemonic = 'DAD\tH'
            break
        
        if case(0x2A):
            mnemonic = 'LHLD\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
            
        if case(0x2B):
            mnemonic = 'DCX\tH'
            break
            
        if case(0x2C):
            mnemonic = 'INR\tL'
            break
        
        if case(0x2D):
            mnemonic = 'DCR\tL'
            break
        
        if case(0x2E):
            mnemonic = 'MVI\tL, #$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0x2F):
            mnemonic = 'CMA'
            break
        
        if case(0x30):
            mnemonic = 'DB $%02x\t;ILLEGAL' % (opcode)
            break
        
        if case(0x31):
            mnemonic = 'LXI\tSP, #$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0x32):
            mnemonic = 'STA\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
            
        if case(0x33):
            mnemonic = 'INX\tSP'
            break
        
        if case(0x34):
            mnemonic = 'INR\tM'
            break
        
        if case(0x35):
            mnemonic = 'DCR\tM'
            break
        
        if case(0x36):
            mnemonic = 'MVI\tM, #$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0x37):
            mnemonic = 'STC'
            break
        
        if case(0x38):
            mnemonic = 'DB $%02x\t;ILLEGAL' % (opcode)
            break
        
        if case(0x39):
            mnemonic = 'DAD\tSP'
            break
        
        if case(0x3A):
            mnemonic = 'LDA\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0x3B):
            mnemonic = 'DCX\tSP'
            break
        
        if case(0x3C):
            mnemonic = 'INR\tA'
            break
        
        if case(0x3D):
            mnemonic = 'DCR\tA'
            break
        
        if case(0x3E):
            mnemonic = 'MVI\tA, #$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
            
        if case(0x3F):
            mnemonic = 'CMC'
            break
        
        if case(0x40):
            mnemonic = 'MOV\tB, B'
            break
        
        if case(0x41):
            mnemonic = 'MOV\tB, C'
            break
        
        if case(0x42):
            mnemonic = 'MOV\tB, D'
            break
        
        if case(0x43):
            mnemonic = 'MOV\tB, E'
            break
        
        if case(0x44):
            mnemonic = 'MOV\tB, H'
            break
        
        if case(0x45):
            mnemonic = 'MOV\tB, L'
            break
        
        if case(0x46):
            mnemonic = 'MOV\tB, M'
            break
        
        if case(0x47):
            mnemonic = 'MOV\tB, A'
            break
        
        if case(0x48):
            mnemonic = 'MOV\tC, B'
            break
        
        if case(0x49):
            mnemonic = 'MOV\tC, C'
            break
        
        if case(0x4A):
            mnemonic = 'MOV\tC, D'
            break
        
        if case(0x4B):
            mnemonic = 'MOV\tC, E'
            break
        
        if case(0x4C):
            mnemonic = 'MOV\tC, H'
            break
        
        if case(0x4D):
            mnemonic = 'MOV\tC, L'
            break
            
        if case(0x4E):
            mnemonic = 'MOV\tC, M'
            break
        
        if case(0x4F):
            mnemonic = 'MOV\tC, A'
            break
        
        if case(0x50):
            mnemonic = 'MOV\tD, B'
            break
        
        if case(0x51):
            mnemonic = 'MOV\tD, C'
            break
        
        if case(0x52):
            mnemonic = 'MOV\tD, D'
            break
        
        if case(0x53):
            mnemonic = 'MOV\tD, E'
            break
        
        if case(0x54):
            mnemonic = 'MOV\tD, H'
            break
        
        if case(0x55):
            mnemonic = 'MOV\tD, L'
            break
        
        if case(0x56):
            mnemonic = 'MOV\tD, M'
            break
        
        if case(0x57):
            mnemonic = 'MOV\tD, A'
            break
        
        if case(0x58):
            mnemonic = 'MOV\tE, B'
            break
        
        if case(0x59):
            mnemonic = 'MOV\tE, C'
            break
        
        if case(0x5A):
            mnemonic = 'MOV\tE, D'
            break
        
        if case(0x5B):
            mnemonic = 'MOV\tE, E'
            break
        
        if case(0x5C):
            mnemonic = 'MOV\tE, H'
            break
        
        if case(0x5D):
            mnemonic = 'MOV\tE, L'
            break
        
        if case(0x5E):
            mnemonic = 'MOV\tE, M'
            break
        
        if case(0x5F):
            mnemonic = 'MOV\tE, A'
            break
        
        if case(0x60):
            mnemonic = 'MOV\tH, B'
            break
        
        if case(0x61):
            mnemonic = 'MOV\tH, C'
            break
        
        if case(0x62):
            mnemonic = 'MOV\tH, D'
            break
        
        if case(0x63):
            mnemonic = 'MOV\tH, E'
            break
        
        if case(0x64):
            mnemonic = 'MOV\tH, H'
            break
        
        if case(0x65):
            mnemonic = 'MOV\tH, L'
            break
        
        if case(0x66):
            mnemonic = 'MOV\tH, M'
            break
            
        if case(0x67):
            mnemonic = 'MOV\tH, A'
            break
            
        if case(0x68):
            mnemonic = 'MOV\tL, B'
            break
        
        if case(0x69):
            mnemonic = 'MOV\tL, C'
            break
        
        if case(0x6A):
            mnemonic = 'MOV\tL, D'
            break
        
        if case(0x6B):
            mnemonic = 'MOV\tL, E'
            break
        
        if case(0x6C):
            mnemonic = 'MOV\tL, H'
            break
        
        if case(0x6D):
            mnemonic = 'MOV\tL, L'
            break
        
        if case(0x6E):
            mnemonic = 'MOV\tL, M'
            break
        
        if case(0x6F):
            mnemonic = 'MOV\tL, A'
            break
        
        if case(0x70):
            mnemonic = 'MOV\tM, B'
            break
        
        if case(0x71):
            mnemonic = 'MOV\tM, C'
            break
            
        if case(0x72):
            mnemonic = 'MOV\tM, D'
            break
        
        if case(0x73):
            mnemonic = 'MOV\tM, E'
            break
        
        if case(0x74):
            mnemonic = 'MOV\tM, H'
            break
        
        if case(0x75):
            mnemonic = 'MOV\tM, L'
            break
        
        if case(0x76):
            mnemonic = 'HLT'
            break
        
        if case(0x77):
            mnemonic = 'MOV\tM, A'
            break
        
        if case(0x78):
            mnemonic = 'MOV\tA, B'
            break
        
        if case(0x79):
            mnemonic = 'MOV\tA, C'
            break
        
        if case(0x7A):
            mnemonic = 'MOV\tA, D'
            break
            
        if case(0x7B):
            mnemonic = 'MOV\tA, E'
            break
            
        if case(0x7C):
            mnemonic = 'MOV\tA, H'
            break
        
        if case(0x7D):
            mnemonic = 'MOV\tA, L'
            break
        
        if case(0x7E):
            mnemonic = 'MOV\tA, M'
            break
        
        if case(0x7F):
            mnemonic = 'MOV\tA, A'
            break
        
        if case(0x80):
            mnemonic = 'ADD\tB'
            break
        
        if case(0x81):
            mnemonic = 'ADD\tC'
            break
        
        if case(0x82):
            mnemonic = 'ADD\tD'
            break
        
        if case(0x83):
            mnemonic = 'ADD\tE'
            break
        
        if case(0x84):
            mnemonic = 'ADD\tH'
            break
        
        if case(0x85):
            mnemonic = 'ADD\tL'
            break
        
        if case(0x86):
            mnemonic = 'ADD\tM'
            break
        
        if case(0x87):
            mnemonic = 'ADD\tA'
            break
        
        if case(0x88):
            mnemonic = 'ADC\tB'
            break
        
        if case(0x89):
            mnemonic = 'ADC\tC'
            break
        
        if case(0x8A):
            mnemonic = 'ADC\tD'
            break
        
        if case(0x8B):
            mnemonic = 'ADC\tE'
            break
        
        if case(0x8C):
            mnemonic = 'ADC\tH'
            break
        
        if case(0x8D):
            mnemonic = 'ADC\tL'
            break
        
        if case(0x8E):
            mnemonic = 'ADC\tM'
            break
        
        if case(0x8F):
            mnemonic = 'ADC\tA'
            break
        
        if case(0x90):
            mnemonic = 'SUB\tB'
            break
            
        if case(0x91):
            mnemonic = 'SUB\tC'
            break
            
        if case(0x92):
            mnemonic = 'SUB\tD'
            break
            
        if case(0x93):
            mnemonic = 'SUB\tE'
            break
        
        if case(0x94):
            mnemonic = 'SUB\tH'
            break
        
        if case(0x95):
            mnemonic = 'SUB\tL'
            break
        
        if case(0x96):
            mnemonic = 'SUB\tM'
            break
        
        if case(0x97):
            mnemonic = 'SUB\tA'
            break
        
        if case(0x98):
            mnemonic = 'SBB\tB'
            break
        
        if case(0x99):
            mnemonic = 'SBB\tC'
            break
        
        if case(0x9A):
            mnemonic = 'SBB\tD'
            break
        
        if case(0x9B):
            mnemonic = 'SBB\tE'
            break
        
        if case(0x9C):
            mnemonic = 'SBB\tH'
            break
        
        if case(0x9D):
            mnemonic = 'SBB\tL'
            break
        
        if case(0x9E):
            mnemonic = 'SBB\tM'
            break
        
        if case(0x9F):
            mnemonic = 'SBB\tA'
            break
        
        if case(0xA0):
            mnemonic = 'ANA\tB'
            break
            
        if case(0xA1):
            mnemonic = 'ANA\tC'
            break
            
        if case(0xA2):
            mnemonic = 'ANA\tD'
            break
            
        if case(0xA3):
            mnemonic = 'ANA\tE'
            break
            
        if case(0xA4):
            mnemonic = 'ANA\tH'
            break
            
        if case(0xA5):
            mnemonic = 'ANA\tL'
            break
            
        if case(0xA6):
            mnemonic = 'ANA\tM'
            break
            
        if case(0xA7):
            mnemonic = 'ANA\tA'
            break
            
        if case(0xA8):
            mnemonic = 'XRA\tB'
            break
        
        if case(0xA9):
            mnemonic = 'XRA\tC'
            break
        
        if case(0xAA):
            mnemonic = 'XRA\tD'
            break
        
        if case(0xAB):
            mnemonic = 'XRA\tE'
            break
        
        if case(0xAC):
            mnemonic = 'XRA\tH'
            break
        
        if case(0xAD):
            mnemonic = 'XRA\tL'
            break
        
        if case(0xAE):
            mnemonic = 'XRA\tM'
            break
        
        if case(0xAF):
            mnemonic = 'XRA\tA'
            break
        
        if case(0xB0):
            mnemonic = 'ORA\tB'
            break
        
        if case(0xB1):
            mnemonic = 'ORA\tC'
            break
        
        if case(0xB2):
            mnemonic = 'ORA\tD'
            break
        
        if case(0xB3):
            mnemonic = 'ORA\tE'
            break
        
        if case(0xB4):
            mnemonic = 'ORA\tH'
            break
        
        if case(0xB5):
            mnemonic = 'ORA\tL'
            break
        
        if case(0xB6):
            mnemonic = 'ORA\tM'
            break
        
        if case(0xB7):
            mnemonic = 'ORA\tA'
            break
        
        if case(0xB8):
            mnemonic = 'CMP\tB'
            break
        
        if case(0xB9):
            mnemonic = 'CMP\tC'
            break
        
        if case(0xBA):
            mnemonic = 'CMP\tD'
            break
        
        if case(0xBB):
            mnemonic = 'CMP\tE'
            break
        
        if case(0xBC):
            mnemonic = 'CMP\tH'
            break
        
        if case(0xBD):
            mnemonic = 'CMP\tL'
            break
        
        if case(0xBE):
            mnemonic = 'CMP\tM'
            break
        
        if case(0xBF):
            mnemonic = 'CMP\tA'
            break
        
        if case(0xC0):
            mnemonic = 'RNZ'
            break
        
        if case(0xC1):
            mnemonic = 'POP\tB'
            break
        
        if case(0xC2):
            mnemonic = 'JNZ\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
            
        if case(0xC3):
            mnemonic = 'JMP\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xC4):
            mnemonic = 'CNZ\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xC5):
            mnemonic = 'PUSH\tB'
            break
            
        if case(0xC6):
            mnemonic = 'ADI\t#$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0xC7):
            mnemonic = 'RST\t0'
            break
        
        if case(0xC8):
            mnemonic = 'RZ'
            break
        
        if case(0xC9):
            mnemonic = 'RET'
            break
            
        if case(0xCA):
            mnemonic = 'JZ\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
            
        if case(0xCB):
            mnemonic = 'DB $%02x\t;ILLEGAL' % (opcode)
            break
        
        if case(0xCC):
            mnemonic = 'CZ\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xCD):
            mnemonic = 'CALL\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xCE):
            mnemonic = 'ACI\t#$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0xCF):
            mnemonic = 'RST\t1'
            break
        
        if case(0xD0):
            mnemonic = 'RNC'
            break
        
        if case(0xD1):
            mnemonic = 'POP\tD'
            break
        
        if case(0xD2):
            mnemonic = 'JNC\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
            
        if case(0xD3):
            mnemonic = 'OUT\t#$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0xD4):
            mnemonic = 'CNC\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xD5):
            mnemonic = 'PUSH\tD'
            break
        
        if case(0xD6):
            mnemonic = 'SUI\t#$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0xD7):
            mnemonic = 'RST\t2'
            break
        
        if case(0xD8):
            mnemonic = 'RC'
            break
        
        if case(0xD9):
            mnemonic = 'DB $%02x\t;ILLEGAL' % (opcode)
            break
        
        if case(0xDA):
            mnemonic = 'JC\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
            
        if case(0xDB):
            mnemonic = 'IN\t#$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0xDC):
            mnemonic = 'CC\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xDD):
            mnemonic = 'DB $%02x\t;ILLEGAL' % (opcode)
            break
        
        if case(0xDE):
            mnemonic = 'SBI\t#$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0xDF):
            mnemonic = 'RST\t3'
            break
        
        if case(0xE0):
            mnemonic = 'RPO'
            break
        
        if case(0xE1):
            mnemonic = 'POP\tH'
            break
            
        
        if case(0xE2):
            mnemonic = 'JPO\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xE3):
            mnemonic = 'XTHL'
            break
        
        if case(0xE4):
            mnemonic = 'CPO\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xE5):
            mnemonic = 'PUSH\tH'
            break
        
        if case(0xE6):
            mnemonic = 'ANI\t#$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0xE7):
            mnemonic = 'RST\t4'
            break
        
        if case(0xE8):
            mnemonic = 'RPE'
            break
        
        if case(0xE9):
            mnemonic = 'PCHL'
            break
        
        if case(0xEA):
            mnemonic = 'JPE\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xEB):
            mnemonic = 'XCHG'
            break
        
        if case(0xEC):
            mnemonic = 'CPE\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xED):
            mnemonic = 'DB $%02x\t;ILLEGAL' % (opcode)
            break
        
        if case(0xEE):
            mnemonic = 'XRI\t#$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0xEF):
            mnemonic = 'RST\t5'
            break
        
        if case(0xF0):
            mnemonic = 'RP'
            break
        
        if case(0xF1):
            mnemonic = 'POP\tPSW'
            break
        
        if case(0xF2):
            mnemonic = 'JP\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xF3):
            mnemonic = 'DI'
            break
        
        if case(0xF4):
            mnemonic = 'CP\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xF5):
            mnemonic = 'PUSH\tPSW'
            break
        
        if case(0xF6):
            mnemonic = 'ORI\t#$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
        
        if case(0xF7):
            mnemonic = 'RST\t6'
            break
        
        if case(0xF8):
            mnemonic = 'RM'
            break
        
        if case(0xF9):
            mnemonic = 'SPHL'
            break
        
        if case(0xFA):
            mnemonic = 'JM\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xFB):
            mnemonic = 'EI'
            break
            
        if case(0xFC):
            mnemonic = 'CM\t$%02x%02x' % (code[pc+2], code[pc+1])
            bytes = '%02x %02x %02x' % (opcode, code[pc+1], code[pc+2])
            size = 3
            break
        
        if case(0xFD):
            mnemonic = 'DB $%02x\t;ILLEGAL' % (opcode)
            break
        
        if case(0xFE):
            mnemonic = 'CPI\t#$%02x' % (code[pc+1])
            bytes = '%02x %02x' % (opcode, code[pc+1])
            size = 2
            break
            
        if case(0xFF):
            mnemonic = 'RST\t7'
            break
        
        mnemonic = 'NOT IMPLEMENTED'
        break
           
    if _listing:
        _writer.write('%04x: %s\t %s\n' % (pc, bytes, mnemonic))
    else:
        _writer.write('\t' + mnemonic + '\n')
    return size

def main():
    parser = argparse.ArgumentParser(description='Disassemble Intel 8080 binaries. Can be recompiled with ZASM.')
    parser.add_argument('-l','--list', help='Output a program listing with memory addresses.', action='store_true')
    parser.add_argument('-o','--output', help='Write source listing to file [OUTPUT]')
    parser.add_argument('filename', help='Program to dissasemble.')
    args = parser.parse_args()
        
    ext = '.lst' if args.list else '.asm'
    out = args.filename if args.output is None else args.output
        
    out = out + ext
        
    image = []
    pc = 0
    
    with open(args.filename, 'rb') as f:
        image = f.read()
    
    wr = writer(out)
    
    if args.list:
        wr.write('0000:            ORG 0000h\n')
    else:
        wr.write('\tORG 0000h\n')
    
    while pc < len(image):
        pc += dasm8080(image, pc, wr, args.list)

if __name__ == '__main__':
    main()
