#!/bin/python3
import sys
import argparse

def mrcCompile(stdin):
    record = stdin
    split_record = record.replace('\x1f','$').replace('\x1d','\n').split('\x1e')
    split_record = split_record[:-1]
    LDR = split_record[0][:24]
    recordDIR = split_record[0][24:]
    print("=LDR  " + LDR)
    directory = []
    j = 0
    for i in range(12, len(recordDIR)+12, 12):
        directory.append(recordDIR[j:i])
        j = i
    # Print out the display record
    for i in range(len(directory)):
        print("=" + directory[i][:3] + "  " + split_record[i+1])

def mrcDisplay(stdin):
    display_record = stdin
    display_list = display_record.split('\n')

    field_len = []
    field_tag = []

    for i in range(len(display_list[1:])):
        # Convert to utf-8 to get the correct ASCII character length
        field_len.append(len(display_list[i+1][5:].encode('utf-8')))
        field_tag.append(display_list[i+1][1:4])

    field_len = field_len[:-1]
    total_offset = 0
    field_offset = []
    for i in range(len(field_len)):
        field_offset.append(total_offset)
        total_offset += field_len[i]

    # Make Header
    # Make Payload
    recordDIR = ""
    for j in range(len(field_offset)):
        recordDIR += field_tag[j] + str(field_len[j]).zfill(4) + str(field_offset[j]).zfill(5)

    # CALCULATED
    LDR = display_list[0][6:]
    LDR += recordDIR

    compiled_record = ''
    eof_delimiter = '\x1d' #^]
    field_delimiter = '\x1e' #^^
    subfield_delimiter = '\x1f' #^_

    for k in range(1, len(display_list)-1):
        compiled_record += display_list[k].replace('$', subfield_delimiter)[6:] + field_delimiter

    compiled_record += eof_delimiter
    compiled_record = LDR + field_delimiter + compiled_record

    print(compiled_record)

parser = argparse.ArgumentParser()
parser.add_argument("-c",dest="mrcCompile",default=False,action="store_true")
parser.add_argument("-d",dest="mrcDisplay",default=False,action="store_true")
args = parser.parse_args()

if args.mrcCompile:
    for line in sys.stdin:
        mrcCompile(line)
elif args.mrcDisplay:
    sline = ''
    for line in sys.stdin:
       sline += line 
    mrcDisplay(sline)
