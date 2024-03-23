# IEEE-754 Binary-128 Floating Point Converter

This program is an IEEE-754 Binary-128 floating-point converter that takes both binary and decimal numbers as input and converts them to their binary and hexadecimal representations.

## Features

- Accepts decimal (base-10) and binary (base-2) input (e.g., `127.0*10^5` for decimal, `101.01*2^5` for binary)
- Supports special cases such as NaN
- Outputs each section of the binary representation (sign, exponent, mantissa)
- Outputs the binary representation with spaces between sections
- Outputs the hexadecimal equivalent of the binary representation
- Offers an option to save the output to a text file

## Prerequisites

- Python 3.x

## How to Run the Program

1. Clone the repository or download the source code files.
2. Open a terminal or command prompt and navigate to the directory containing the source code files.
3. Run the following command to start the program: `python app.py`

## How to Use the Program

1. Select the input mode:
- Decimal Input: Enter decimal numbers (e.g., `127.0`, `4.0*10^5`)
- Binary Input: Enter binary numbers (e.g., `1111111.0`, `101.01*2^5`)
2. Enter the input number in the input window.
3. Press the "=" button or hit Enter to convert the input number.
4. The program will display the binary output with spaces between sections, its hexadecimal equivalent, and any special cases (if applicable) in the output window.
5. To save the output to a text file, click the "Save Result to .txt" button. Choose a location and filename for the output file and click "Save".
6. To clear the input and output windows, click the "Clear" button.
7. To delete the last character in the input window, click the "Backspace" button.
8. To enter imaginary numbers, use the "i" button.
9. To enter exponents, use the "^" button followed by the exponent value.
10. To enter negative numbers, use the "-" button before the number.
11. To switch between decimal and binary input modes, select the corresponding radio button.

## Special Cases

The program supports the following special cases:

- Positive Zero
- Negative Zero
- Denormalized Numbers
- Positive Infinity
- Negative Infinity
- Quiet NaN
- Signaling NaN

If the input number falls into one of these special cases, the program will display the corresponding output in the output window.

## Saving Output to Text File

To save the output to a text file, click the "Save Result to .txt" button. A file dialog will open, allowing you to choose the location and filename for the output file. Once you have selected the desired location and filename, click "Save" to save the output.

The program will display a success message if the output is saved successfully. If you cancel the save operation, a warning message will be shown.

## Limitations

The program assumes that the input numbers are valid and well-formatted. Inputting invalid or malformed numbers may lead to unexpected behavior or errors.
