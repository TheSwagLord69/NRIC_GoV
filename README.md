[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![GitHub release](https://img.shields.io/github/release/TheSwagLord69/NRIC_GoV)](https://github.com/TheSwagLord69/NRIC_GoV/releases/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/TheSwagLord69/NRIC_GoV/graphs/commit-activity)
[![GitHub commits](https://badgen.net/github/commits/TheSwagLord69/NRIC_GoV)](https://github.com/TheSwagLord69/NRIC_GoV)
[![GitHub latest commit](https://badgen.net/github/last-commit/TheSwagLord69/NRIC_GoV)](https://github.com/TheSwagLord69/NRIC_GoV/commit/)
[![Github all releases](https://img.shields.io/github/downloads/TheSwagLord69/NRIC_GoV/total.svg)](https://github.com/TheSwagLord69/NRIC_GoV/releases/)

# NRIC/FIN Generation or Validation

**NRIC_GoV.py** is a tool capable of generating a _custom range_ of NRIC/FIN number(s) or validating a _list_ of NRIC/FIN number(s).

## Requirements

Machine (Powered On) capable of running Python 3.9.0

## Usage

### Arguments

#### Help

Views the manual for the script.

```
-h
```
```
--help
```

#### Mode

Changes the mode of operation of either generate or validation. This argument is required.

```
-m
```
```
-M
```
```
--mode
```

#### Range

The range of NRIC/FIN numbers to be generated. This argument is required for generating NRIC/FIN numbers.

```
-r
```
```
-R
```
```
--range
```

#### Initial Alphabet

The initial character of NRIC/FIN numbers to be generated. At least one is required for generating NRIC/FIN numbers. Multiple may be used. 

```
-i
```
```
-I
```
```
--initial
```

#### Output

Designate a file for output of the results. If an absolute file path is not provided, the current working directory will be used.

```
-o
```
```
-O
```
```
--output
```

#### Test Single

Used for validating a single NRIC/FIN number. This argument is required for validating a single NRIC/FIN number.

```
-ts
```
```
-TS
```
```
--testsingle
```

#### Test File

Used for validating multiple NRIC/FIN number from a file delimited by line breaks. This argument is required for validating multiple NRIC/FIN numbers from a file. If an absolute file path is not provided, the current working directory will be used.

```
-tf
```
```
-TF
```
```
--testfile
```

---

### GENERATE

> Allows the generation of **algorithmically valid** NRIC/FIN numbers with a custom defined range.

View below for example usage.

#### Generate with a Singular inital alphabet

Generates a range of valid NRIC numbers (8400000 to 9799999 in this case) starting with the character "S" and prints the results to the terminal.

```bash
python NRIC_GoV.py -M G -I S -R 8400000 9799999
```

#### Generate with Mulitple inital alphabet

Generates a range of valid NRIC numbers (0000000 to 9999999 in this case) starting with the character "S", "T", "M", "F" and "G" and prints the results to the terminal.

```bash
python NRIC_GoV.py -m generate -i s t m f g -R 0000000 9999999
```

#### Generate Output to a file in the current working directory

Generates a range of valid NRIC numbers (0974760 to 0986177 in this case) starting with the character "T" and "G" to a file named "yeahscience.txt" and prints the result to the terminal.

```bash
python NRIC_GoV.py -M g -I t G -R 0974760 0986177 -o yeahscience.txt
```

#### Generate Output to a file in a specific directory

Generates a range of valid NRIC numbers (0000000 to 0000999 in this case) starting with the character "S" and "F" to a file named "validnrics.txt" to the "C:\Users\mynameisjeff\Desktop\" directory and prints the result to the terminal.

```bash
python NRIC_GoV.py -M g -i S F -R 0000000 0000999 -o "C:\Users\mynameisjeff\Desktop\validnrics.txt"
```

---

### VALIDATE

> Allows the **algorithmic validation** of NRIC/FIN numbers.

View below for example usage.

#### Validate Single NRIC/FIN number

Validates a singular of NRIC number (T1769106B in this case) and prints the result to the terminal.

```bash
python NRIC_GoV.py -m V -ts T1769106B
```

#### Validate Single NRIC/FIN number and appending/writing to a file in the current working directory

Validates a singular of NRIC number (M0269106Z in this case), appends the result to a file named "filewithdata.txt" (and creates it if not present) and prints the result to the terminal.

```bash
python NRIC_GoV.py -m V -ts M0269106Z --output filewithdata.txt
```

#### Validate List of NRIC/FIN number from a file delimited by linebreak(s) from the current working directory

Validates multiple NRIC numbers from a file and prints the result to the terminal.

```bash
python NRIC_GoV.py --mode valiDATE -tf somenumbers.txt
```

#### Validate List of NRIC/FIN number from a file delimited by linebreak(s) from a specific directory

Validates multiple NRIC numbers from a file and prints the result to the terminal.

```bash
python NRIC_GoV.py -M v -tf "C:\Users\mynameisjeff\Desktop\validnrics.txt"
```

#### Validate List of NRIC/FIN number from a file delimited by linebreak(s) and writing to a file in the current working directory

Validates multiple NRIC numbers from a file, writes the result to a file named "filewithdata.txt" (and replaces it if already existing) and prints the result to the terminal.

```bash
python NRIC_GoV.py -M v -tf "C:\Users\mynameisjeff\Desktop\validnrics.txt" -o yeahscience.txt
```

