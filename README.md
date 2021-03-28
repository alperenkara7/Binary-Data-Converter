# Binary-Data-Converter

This program takes a hexadecimal number and the data type to be converted as input and converts the number according to the predefined format and gives the converted data as output.

The size of the input can be 1, 2, 3 and 4 bytes, if input is other than these sizes then an error message will be given.

If the selected data type is signed integer, your program will convert the number using 2’s complement representation.

If the selected data type is unsigned integer, number will be converted using unsigned integer representation.

If the selected data type is floating point number, you will use IEEE-like format. The number of exponent bits according to given data size will be like the following: if 1 byte (i.e., 8 bits), 4 bits will be used for exponent part if 2 bytes (i.e., 16 bits), 6 bits will be used for exponent part if 3 bytes (i.e., 24 bits), 8 bits will be used for exponent part if 4 bytes (i.e., 32 bits), 10 bits will be used for exponent part For each given data size 1 bit will be used for sign and remaining bits will be used for fraction.

While calculating the mantissa to get the floating-point value, you will only use the first 13 bits of the fraction part (If the data size is 3 or 4 bytes).
