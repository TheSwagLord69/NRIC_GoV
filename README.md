# NRIC_GoV
Generate a custom range or validate NRIC/FIN number(s).

## Requirements
Machine (Powered On) capable of running Python 3.9.0

## Usage

### GENERATE

> Allows the generation of **algorithmically valid** NRIC/FIN numbers with a custom defined range.

View below for example usage.

#### Generate with a Singular inital alphabet
Generates a range of valid NRIC numbers (8400000 to 9799999 in this case) starting with the character "S" and prints the results to the terminal
```bash
python NRIC_GoV.py -M G -I S -R 8400000 9799999
```

#### Generate with Mulitple inital alphabet
Generates a range of valid NRIC numbers (0000000 to 9999999 in this case) starting with the character "S", "T", "M", "F" and "G" and prints the results to the terminal
```bash
python NRIC_GoV.py -m generate -i s t m f g -R 0000000 9999999
```

#### Generate Output to a file in the current working directory
Generates a range of valid NRIC numbers (0974760 to 0986177 in this case) starting with the character "T" and "G" to a file named "yeahscience.txt" and prints the result to the terminal
```bash
python NRIC_GoV.py -M g -I t G -R 0974760 0986177 -o yeahscience.txt
```

#### Generate Output to a file in a specific directory
Generates a range of valid NRIC numbers (0000000 to 0000999 in this case) starting with the character "S" and "F" to a file named "validnrics.txt" to the "C:\Users\mynameisjeff\Desktop\" directory and prints the result to the terminal
```bash
python NRIC_GoV.py -M g -i S F -R 0000000 0000999 -o "C:\Users\mynameisjeff\Desktop\validnrics.txt"
```

### VALIDATE

> Allows the **algorithmic validation** of NRIC/FIN numbers.

View below for example usage.

#### Validate Single NRIC/FIN number
Validates a singular of NRIC number (T1769106B in this case) and prints the result to the terminal
```bash
python NRIC_GoV.py -m V -ts T1769106B
```

#### Validate Single NRIC/FIN number and appending/writing to a file in the current working directory
Validates a singular of NRIC number (M0269106Z in this case), appends the result to a file named "filewithdata.txt" (and creates it if not present) and prints the result to the terminal
```bash
python NRIC_GoV.py -m V -ts M0269106Z --output filewithdata.txt
```

#### Validate List of NRIC/FIN number from a file delimited by linebreak(s) from the current working directory
Validates multiple NRIC numbers from a file and prints the result to the terminal
```bash
python NRIC_GoV.py --mode valiDATE -tf somenumbers.txt
```

#### Validate List of NRIC/FIN number from a file delimited by linebreak(s) from a specific directory
Validates multiple NRIC numbers from a file and prints the result to the terminal
```bash
python NRIC_GoV.py -M v -tf "C:\Users\mynameisjeff\Desktop\validnrics.txt"
```

#### Validate List of NRIC/FIN number from a file delimited by linebreak(s) and writing to a file in the current working directory
Validates multiple NRIC numbers from a file, writes the result to a file named "filewithdata.txt" (and replaces it if already existing) and prints the result to the terminal
```bash
python NRIC_GoV.py -M v -tf "C:\Users\mynameisjeff\Desktop\validnrics.txt" -o yeahscience.txt
```

