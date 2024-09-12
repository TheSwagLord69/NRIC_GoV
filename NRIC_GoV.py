#
#    _   _ ____  ___ ____    ____                                 _       
#   | \ | |  _ \|_ _/ ___|  / ___| ___ _ __   ___ _ __ __ _  __ _| |_ ___ 
#   |  \| | |_) || | |     | |  _ / _ \ '_ \ / _ \ '__/ _` |/ _` | __/ _ \
#   | |\  |  _ < | | |___  | |_| |  __/ | | |  __/ | | (_| | (_| | ||  __/
#   |_| \_|_| \_\___\____|  \____|\___|_| |_|\___|_|  \__,_|\__,_|\__\___|
#     ___  _ __  \ \   / /_ _| (_) __| | __ _| |_ ___                     
#    / _ \| '__|  \ \ / / _` | | |/ _` |/ _` | __/ _ \                    
#   | (_) | |      \ V / (_| | | | (_| | (_| | ||  __/                    
#    \___/|_|       \_/ \__,_|_|_|\__,_|\__,_|\__\___|              v0.1  
#
#
#   NRIC_GoV is a tool designed for educational purposes to generate a custom range or validation of National Registration Identity Card (NRIC)/Foreign Identification Number (FIN) number(s).
#
#       By Hentai Salesman 69 @ https://github.com/TheSwagLord69
#
#       The author of this tool is an independent developer and does not represent, endorse, or
#       act on behalf of any organization, company, or government entity, including their current employer.
#
#       NRIC_GoV is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This tool is distributed in the hope that it will be useful for educational purposes, 
#       but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#       See the GNU General Public License for more details.
#
#       The generation of NRIC/FIN numbers via this tool is legal, as the underlying algorithm is publicly available. 
#       However, misuse of NRIC/FIN numbers, including impersonation or fraud, is illegal and constitutes an offense.
#
#       By using this tool, you agree to take full responsibility for any actions you take with the generated numbers. 
#       The author is not liable for any misuse or consequences arising from the use of this tool.
#
#       This tool is provided "as is" and without any warranties of any kind. To the fullest extent permitted by law, 
#       I disclaim all warranties, including but not limited to:
#       - Accuracy, correctness, reliability, or timeliness
#       - Non-infringement, merchantability, or fitness for a particular purpose
#       - That the tool will operate uninterrupted or error-free
#       - That the tool is free of viruses or other harmful components
#
#       USE THIS TOOL AT YOUR OWN RISK:
#       - The author, contributors, or anyone else associated with this tool are not responsible for any consequences 
#         of your use of the information and functionalities provided.
#       - For legal advice, please consult a licensed professional.
#       - No claims for damages can be made against the creators, as this tool is a freely-licensed educational resource 
#         provided without any agreement or obligation beyond the GNU General Public License (GPL).
#
#

import argparse
import sys

def nric_digit_weight(number):
    return ((int(number[0])*2)+(int(number[1])*7)+(int(number[2])*6)+(int(number[3])*5)+(int(number[4])*4)+(int(number[5])*3)+(int(number[6])*2))
    
def generate(rangelist,charlist):
    
    print('[*] Generating valid NRICs starting with ', end='')
    print(*[char.upper() for char in charlist], sep=', ', end=' ')
    print('in the range of ' + rangelist[0] + ' to ' + rangelist[1])

    printlist = []
    
    for i in charlist:
        # Initial is S
        if (str(i).lower() == 's'):
            for n in range(int(rangelist[0]), int(rangelist[1])+1):
                nric_number = '{:0>{}}'.format(n, 7)
                nric_weight = nric_digit_weight(nric_number)
                nric_checksum = 11-(((nric_weight+0)%11)+1)
                if nric_checksum == 0:
                    nric_full = 'S' + str(nric_number) + 'A'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 1:
                    nric_full = 'S' + str(nric_number) + 'B'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 2:
                    nric_full = 'S' + str(nric_number) + 'C'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 3:
                    nric_full = 'S' + str(nric_number) + 'D'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 4:
                    nric_full = 'S' + str(nric_number) + 'E'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 5:
                    nric_full = 'S' + str(nric_number) + 'F'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 6:
                    nric_full = 'S' + str(nric_number) + 'G'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 7:
                    nric_full = 'S' + str(nric_number) + 'H'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 8:
                    nric_full = 'S' + str(nric_number) + 'I'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 9:
                    nric_full = 'S' + str(nric_number) + 'Z'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 10:
                    nric_full = 'S' + str(nric_number) + 'J'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                else:
                    print('[!!!] Something has gone terribly wrong') #debug
                    sys.exit()
                    
        # Initial is T
        if (str(i).lower() == 't'):
            for n in range(int(rangelist[0]), int(rangelist[1])+1):
                nric_number = '{:0>{}}'.format(n, 7)
                nric_weight = nric_digit_weight(nric_number)
                nric_checksum = 11-(((nric_weight+4)%11)+1)
                if nric_checksum == 0:
                    nric_full = 'T' + str(nric_number) + 'A'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 1:
                    nric_full = 'T' + str(nric_number) + 'B'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 2:
                    nric_full = 'T' + str(nric_number) + 'C'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 3:
                    nric_full = 'T' + str(nric_number) + 'D'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 4:
                    nric_full = 'T' + str(nric_number) + 'E'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 5:
                    nric_full = 'T' + str(nric_number) + 'F'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 6:
                    nric_full = 'T' + str(nric_number) + 'G'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 7:
                    nric_full = 'T' + str(nric_number) + 'H'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 8:
                    nric_full = 'T' + str(nric_number) + 'I'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 9:
                    nric_full = 'T' + str(nric_number) + 'Z'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 10:
                    nric_full = 'T' + str(nric_number) + 'J'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                else:
                    print('[!!!] Something has gone terribly wrong') #debug
                    sys.exit()
    
        # Initial is G
        if (str(i).lower() == 'g'):
            for n in range(int(rangelist[0]), int(rangelist[1])+1):
                nric_number = '{:0>{}}'.format(n, 7)
                nric_weight = nric_digit_weight(nric_number)
                nric_checksum = 11-(((nric_weight+4)%11)+1)
                if nric_checksum == 0:
                    nric_full = 'G' + str(nric_number) + 'K'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 1:
                    nric_full = 'G' + str(nric_number) + 'L'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 2:
                    nric_full = 'G' + str(nric_number) + 'M'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 3:
                    nric_full = 'G' + str(nric_number) + 'N'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 4:
                    nric_full = 'G' + str(nric_number) + 'P'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 5:
                    nric_full = 'G' + str(nric_number) + 'Q'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 6:
                    nric_full = 'G' + str(nric_number) + 'R'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 7:
                    nric_full = 'G' + str(nric_number) + 'T'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 8:
                    nric_full = 'G' + str(nric_number) + 'U'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 9:
                    nric_full = 'G' + str(nric_number) + 'W'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 10:
                    nric_full = 'G' + str(nric_number) + 'X'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                else:
                    print('[!!!] Something has gone terribly wrong') #debug
                    sys.exit()
        
        # Initial is F
        if (str(i).lower() == 'f'):
            for n in range(int(rangelist[0]), int(rangelist[1])+1):
                nric_number = '{:0>{}}'.format(n, 7)
                nric_weight = nric_digit_weight(nric_number)
                nric_checksum = 11-(((nric_weight+0)%11)+1)
                if nric_checksum == 0:
                    nric_full = 'F' + str(nric_number) + 'K'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 1:
                    nric_full = 'F' + str(nric_number) + 'L'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 2:
                    nric_full = 'F' + str(nric_number) + 'M'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 3:
                    nric_full = 'F' + str(nric_number) + 'N'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 4:
                    nric_full = 'F' + str(nric_number) + 'P'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 5:
                    nric_full = 'F' + str(nric_number) + 'Q'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 6:
                    nric_full = 'F' + str(nric_number) + 'R'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 7:
                    nric_full = 'F' + str(nric_number) + 'T'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 8:
                    nric_full = 'F' + str(nric_number) + 'U'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 9:
                    nric_full = 'F' + str(nric_number) + 'W'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 10:
                    nric_full = 'F' + str(nric_number) + 'X'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                else:
                    print('[!!!] Something has gone terribly wrong') #debug
                    sys.exit()
        
        # Initial is M
        if (str(i).lower() == 'm'):
            for n in range(int(rangelist[0]), int(rangelist[1])+1):
                nric_number = '{:0>{}}'.format(n, 7)
                nric_weight = nric_digit_weight(nric_number)
                nric_checksum = 11-(((nric_weight+3)%11)+1)
                if nric_checksum == 0:
                    nric_full = 'M' + str(nric_number) + 'K'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 1:
                    nric_full = 'M' + str(nric_number) + 'L'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 2:
                    nric_full = 'M' + str(nric_number) + 'J'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 3:
                    nric_full = 'M' + str(nric_number) + 'N'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 4:
                    nric_full = 'M' + str(nric_number) + 'P'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 5:
                    nric_full = 'M' + str(nric_number) + 'Q'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 6:
                    nric_full = 'M' + str(nric_number) + 'R'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 7:
                    nric_full = 'M' + str(nric_number) + 'T'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 8:
                    nric_full = 'M' + str(nric_number) + 'U'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 9:
                    nric_full = 'M' + str(nric_number) + 'W'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                elif nric_checksum == 10:
                    nric_full = 'M' + str(nric_number) + 'X'
                    print(str(nric_full)) #debug
                    printlist.append(nric_full)
                else:
                    print('[!!!] Something has gone terribly wrong') #debug
                    sys.exit()
                    
    return printlist
    
def validate(testcase):
    
    valid_NRIC = False
    
    # Test for valid length
    if len(testcase) == 9:
        pass
        if (str(testcase[0]).lower() == 's') or (str(testcase[0]).lower() == 't') or (str(testcase[0]).lower() == 'f') or (str(testcase[0]).lower() == 'g') or (str(testcase[0]).lower() == 'm'):
            pass
            if testcase[1:8].isdigit():
                pass
                # Initial is S
                if (str(testcase[0]).lower() == 's'):
                    nric_weight = nric_digit_weight(testcase[1:8])
                    nric_checksum = 11-(((nric_weight+0)%11)+1)
                    if nric_checksum == 0:
                        if testcase[-1].upper() == 'A':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 1:
                        if testcase[-1].upper() == 'B':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 2:
                        if testcase[-1].upper() == 'C':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 3:
                        if testcase[-1].upper() == 'D':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 4:
                        if testcase[-1].upper() == 'E':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 5:
                        if testcase[-1].upper() == 'F':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 6:
                        if testcase[-1].upper() == 'G':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 7:
                        if testcase[-1].upper() == 'H':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 8:
                        if testcase[-1].upper() == 'I':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 9:
                        if testcase[-1].upper() == 'Z':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 10:
                        if testcase[-1].upper() == 'J':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    else:
                        print('[!!!] Something has gone terribly wrong') #debug
                        sys.exit()
                # Initial is T
                elif (str(testcase[0]).lower() == 't'):
                    nric_weight = nric_digit_weight(testcase[1:8])
                    nric_checksum = 11-(((nric_weight+4)%11)+1)
                    if nric_checksum == 0:
                        if testcase[-1].upper() == 'A':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 1:
                        if testcase[-1].upper() == 'B':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 2:
                        if testcase[-1].upper() == 'C':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 3:
                        if testcase[-1].upper() == 'D':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 4:
                        if testcase[-1].upper() == 'E':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 5:
                        if testcase[-1].upper() == 'F':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 6:
                        if testcase[-1].upper() == 'G':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 7:
                        if testcase[-1].upper() == 'H':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 8:
                        if testcase[-1].upper() == 'I':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 9:
                        if testcase[-1].upper() == 'Z':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 10:
                        if testcase[-1].upper() == 'J':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    else:
                        print('[!!!] Something has gone terribly wrong') #debug
                        sys.exit()
                # Initial is F
                elif (str(testcase[0]).lower() == 'f'):
                    nric_weight = nric_digit_weight(testcase[1:8])
                    nric_checksum = 11-(((nric_weight+0)%11)+1)
                    if nric_checksum == 0:
                        if testcase[-1].upper() == 'K':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 1:
                        if testcase[-1].upper() == 'L':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 2:
                        if testcase[-1].upper() == 'M':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 3:
                        if testcase[-1].upper() == 'N':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 4:
                        if testcase[-1].upper() == 'P':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 5:
                        if testcase[-1].upper() == 'Q':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 6:
                        if testcase[-1].upper() == 'R':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 7:
                        if testcase[-1].upper() == 'T':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 8:
                        if testcase[-1].upper() == 'U':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 9:
                        if testcase[-1].upper() == 'W':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 10:
                        if testcase[-1].upper() == 'X':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    else:
                        print('[!!!] Something has gone terribly wrong') #debug
                        sys.exit()
                # Initial is G
                elif (str(testcase[0]).lower() == 'g'):
                    nric_weight = nric_digit_weight(testcase[1:8])
                    nric_checksum = 11-(((nric_weight+4)%11)+1)
                    if nric_checksum == 0:
                        if testcase[-1].upper() == 'K':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 1:
                        if testcase[-1].upper() == 'L':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 2:
                        if testcase[-1].upper() == 'M':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 3:
                        if testcase[-1].upper() == 'N':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 4:
                        if testcase[-1].upper() == 'P':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 5:
                        if testcase[-1].upper() == 'Q':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 6:
                        if testcase[-1].upper() == 'R':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 7:
                        if testcase[-1].upper() == 'T':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 8:
                        if testcase[-1].upper() == 'U':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 9:
                        if testcase[-1].upper() == 'W':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 10:
                        if testcase[-1].upper() == 'X':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    else:
                        print('[!!!] Something has gone terribly wrong') #debug
                        sys.exit()
                # Initial is M
                elif (str(testcase[0]).lower() == 'm'):
                    nric_weight = nric_digit_weight(testcase[1:8])
                    nric_checksum = 11-(((nric_weight+3)%11)+1)
                    if nric_checksum == 0:
                        if testcase[-1].upper() == 'K':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 1:
                        if testcase[-1].upper() == 'L':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 2:
                        if testcase[-1].upper() == 'J':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 3:
                        if testcase[-1].upper() == 'N':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 4:
                        if testcase[-1].upper() == 'P':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 5:
                        if testcase[-1].upper() == 'Q':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 6:
                        if testcase[-1].upper() == 'R':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 7:
                        if testcase[-1].upper() == 'T':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 8:
                        if testcase[-1].upper() == 'U':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 9:
                        if testcase[-1].upper() == 'W':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    elif nric_checksum == 10:
                        if testcase[-1].upper() == 'X':
                            print(str(testcase) + ': Valid NRIC')
                            valid_NRIC = True
                        else:
                            print(str(testcase) + ': Invalid NRIC, final letter is incorrect')
                    else:
                        print('[!!!] Something has gone terribly wrong') #debug
                        sys.exit()
                else:
                    print('[!!!] Somethings wrong!')
            else:
                print(str(testcase) + ': Invalid NRIC, 7 numbers must be followed by the initial alphabet')
        else:
            print(str(testcase) + ': Invalid NRIC, initial alphabet is not S, T, F, G or M')
    else:
        print(str(testcase) + ': Invalid NRIC, length is not 9 characters')
    
    return valid_NRIC
    
def usagemsg(name=None):
    return '''NRIC_GoV.py [-h] -m MODE [-r N N] [-i N [N ...]] [-o OUTPUT] [-ts TESTSINGLE] [-tf TESTFILE]

    Generate NRIC:
        NRIC_GoV.py [-m GENERATE] [-i N [N ...]] [-r N N] [-o OUTPUT]
        E.g.,
        NRIC_GoV.py -M G -I S T F G M -R 0000000 9999999
        NRIC_GoV.py -m g -i s t -r 8900000 9199999 -o myfile.txt
    
    Validate NRIC:
        NRIC_GoV.py [-m VALIDATE] [-ts TESTSINGLE] [-tf TESTFILE] [-o OUTPUT]
        E.g.,
        NRIC_GoV.py -M V -TS s9348715Z
        NRIC_GoV.py -M V -TS Z9876543a --output appendhere.txt
        NRIC_GoV.py -m v -tf myfile.txt -O yourfile.txt
        
'''

def main():
    parser = argparse.ArgumentParser(description='Script to Generate or Validate NRIC', usage=usagemsg())
    parser.add_argument('-m', '-M', '--mode', type=str, required=True,
                    help='Mode of operation, either [G]enerate or [V]alidate')
    parser.add_argument('-r', '-R', '--range', metavar='N', type=str, nargs=2,
                    help='Range of NRIC numbers to be generated')
    parser.add_argument('-i', '-I', '--initial', metavar='N', type=str, nargs='+',
                    help='Initial letter of NRICs to be generated')
    parser.add_argument('-o', '-O', '--output', type=str,
                    help='Writes output to file')
    parser.add_argument('-ts', '-TS', '--testsingle', type=str,
                    help='Singular NRIC to test')
    parser.add_argument('-tf', '-TF', '--testfile', type=str,
                    help='List of NRIC(s) in a file delimited by linebreak(s)')
    
    args = parser.parse_args()
    
    if args.testsingle and args.testfile:
        parser.error('--testsingle and --testfile used. Please choose one.')
    if (str(args.mode).lower() == 'v' or str(args.mode).lower() == 'validate') and args.range:
        parser.error('Validate mode does not use --range.')
    if (str(args.mode).lower() == 'v' or str(args.mode).lower() == 'validate') and args.initial:
        parser.error('Validate mode does not use --initial.')
    if (str(args.mode).lower() == 'g' or str(args.mode).lower() == 'generate') and args.testsingle:
        parser.error('Generate mode does not use --testsingle.')
    if (str(args.mode).lower() == 'g' or str(args.mode).lower() == 'generate') and args.testfile:
        parser.error('Generate mode does not use --testfile.')
    
    if len(sys.argv) == 1:
        print('\n[!] Please add arguments.\n')
        parser.print_help()
        sys.exit()
    
    if str(args.mode).lower() == 'g' or str(args.mode).lower() == 'generate':
        print('[*] Generate mode selected.')
        if args.range:
            if len(args.range) == 2:
                for i in args.range:
                    if i.isdigit() and len(i) == 7:
                        pass
                    else:
                        parser.error('Please use a positive 7 digit integer for the range values')
                        sys.exit()
                if args.range[0] > args.range[1]:
                    parser.error('First value in the range cannot be larger than the second value')
                    sys.exit()
        else:
            print('[!] Please include range')
            sys.exit()
            
        if args.initial:
            if len(args.initial) <= 5:
                for i in args.initial:
                    if (str(i).lower() == 's') or (str(i).lower() == 't') or (str(i).lower() == 'f') or (str(i).lower() == 'g') or (str(i).lower() == 'm'):
                        pass
                    else:
                        parser.error('Please use only characters S, T, F, G or M')
                        sys.exit()
            else:
                parser.error('Too many items')
                sys.exit()
        else:
            parser.error('Please include at least one initial alphabet E.g., S, T, F, G, M')
            sys.exit()
        if args.output:
            print('[*] Writing to ' + str(args.output))
            with open(args.output, 'w') as output_file:
                for i in generate(args.range, args.initial):
                    output_file.write(i+'\n')
        else:
            generate(args.range, args.initial)
    elif str(args.mode).lower() == 'v' or str(args.mode).lower() == 'validate':
        print('[*] Validate mode selected.')
        validated_dict = {}
        if args.testsingle:
            print('[*] Singular NRIC: ' + str(args.testsingle) + ' to be validated')
            validated_dict.update({args.testsingle: validate(args.testsingle)})
            if args.output:
                print('[*] Appending to ' + str(args.output))
                with open(args.output, 'a') as output_file:
                    for key, value in validated_dict.items():
                        output_file.write(str(key)+','+str(value)+'\n')
            else:
                pass
        elif args.testfile:
            with open(args.testfile, 'r') as input_file:
                lines = input_file.readlines()
                for line in lines:
                    validated_dict.update({str(line).strip(): validate(str(line).strip())})
            if args.output:
                print('[*] Writing to ' + str(args.output))
                with open(args.output, 'w') as output_file:
                    output_file.write('Testcases,Valid\n')
                    for key, value in validated_dict.items():
                        output_file.write(str(key)+','+str(value)+'\n')
            else:
                pass
        else:
            parser.error('No NRIC to validate. Pleas use either --testsingle or --testfile')
            sys.exit()
    else:
        parser.error('Please use [G]enerate or [V]alidate.')
        sys.exit()

if __name__ == '__main__':
    main()