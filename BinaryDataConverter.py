import tkinter

hex_to_bin = { '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
'8': '1000', '9': '1001', 'a': '1010', 'A': '1010', 'b': '1011', 'B': '1011', 'c': '1100', 'C': '1100', 'd': '1101',
'D': '1101', 'e': '1110', 'E': '1110', 'f': '1111', 'F': '1111'}

exp, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9, exp10, exp11, exp12, exp13, exp14, exp15, exp16, exp17, exp18, exp19, \
exp20, exp21, exp22= -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22

def unsigned_converter():
    x = (entry_var.get())
    n = x.strip()
    for i in range(len(n)):
        if n[i] in hex_to_bin:
            func()
        else:
            invalid = 'Please enter hexadecimal letter between A and F'
            process_status.set(invalid)

def func():
    x = (entry_var.get())
    binary = ''

    for character in x:
        binary += hex_to_bin[character]

    if len(binary) > 32:
        invalid2 = 'You entered invalid number!'
        process_status.set(invalid2)
    else:
        binary_label.set(binary)
        n = binary.strip()
        binary_to_decimal = 0
        for i in range(len(n)):
            binary_to_decimal += int(n[i]) * 2 ** abs((i - (len(n) - 1)))
        decimal_of_float_label.set(binary_to_decimal)
        valid = 'Converted!'
        process_status.set(valid)
        sign = binary[0]
        sign_label.set(sign)

def twos_complement():
    x = (entry_var.get())
    n = x.strip()
    for i in range(len(n)):
        if n[i] in hex_to_bin:
            func2()
        else:
            invalid = 'Please enter hexadecimal letter between A and F'
            process_status.set(invalid)

def func2():
    x = (entry_var.get())
    binary = ''

    for character in x:
        binary += hex_to_bin[character]

    if len(binary) > 32:
        invalid2 = 'You entered invalid number!'
        process_status.set(invalid2)
    else:
        binary_label.set(binary)
        n = binary.strip()
        binary_to_decimal = 0

        if n[0] == '0':
            for i in range(len(n)):
                binary_to_decimal += int(n[i]) * 2 ** abs((i - (len(n) - 1)))
        else:
            for i in range(len(n)):
                binary_to_decimal += int(n[i]) * 2 ** abs((i - (len(n) - 1)))
            binary_to_decimal = binary_to_decimal - (2 ** len(n))
        valid = 'Converted!'
        process_status.set(valid)
        decimal_of_float_label.set(binary_to_decimal)
        sign = binary[0]
        sign_label.set(sign)

def float():
    x = (entry_var.get())
    n = x.strip()
    for i in range(len(n)):
        if n[i] in hex_to_bin:
            func3()
        else:
            invalid = 'Please enter hexadecimal letter between A and F'
            process_status.set(invalid)

def func3():
    x = (entry_var.get())
    binary = ''

    for character in x:
        binary += hex_to_bin[character]

    if len(binary) > 32:
        invalid2 = 'You entered invalid number!'
        process_status.set(invalid2)

    else:
        binary_label.set(binary)

        if len(x) == 1:
            x = '0' + x
        if len(x) == 3:
            x = '0' + x[0] + ' ' + x[1] + x[2]
        if len(x) == 4:
            x = x[0]+ x[1] + ' ' + x[2] + x[3]
        if len(x) == 5:
            x = '0' + x[0] + ' ' + x[1] + x[2] + ' ' + x[3] + x[4]
        if len(x) == 6:
            x = x[0]+ x[1] + ' ' + x[2] + x[3] + ' ' + x[4] + x[5]
        if len(x) == 7:
            x = '0' + x[0] + ' ' + x[1] + x[2] + ' ' + x[3] + x[4] + ' ' + x[5] + x[6]
        if len(x) == 8:
            x = x[0]+ x[1] + ' ' + x[2] + x[3] + ' ' + x[4] + x[5] + ' ' + x[6] + x[7]
        float_label.set(x)

        while len(binary) < 8:
            binary = '0' + binary
        while 8 < len(binary) < 16:
            binary = '0' + binary
        while 16 < len(binary) < 24:
            binary = '0' + binary
        while 24 < len(binary) < 32:
            binary = '0' + binary

        else:
            exponent = ''
            fraction = ''
            binary_label.set(binary)

            if len(binary) == 8:
                sign = binary[0]
                exponent += binary[1:5]
                fraction += binary[5:8]
                sign_label.set(sign)
                exponent_label.set(exponent)
                fraction_label.set(fraction)

                n = binary.strip()
                binary_to_decimal = 0
                for i in range(len(n)):
                    binary_to_decimal += int(n[i]) * 2 ** abs((i - (len(n) - 1)))
                decimal_of_float_label.set(binary_to_decimal)

                if exponent == '0000':
                    a = 0
                else:
                    a = 1

                b = fraction[0]
                c = fraction[1]
                d = fraction[2]

                n2 = exponent.strip()
                exponent_to_decimal = 0
                for i in range(len(n2)):
                    exponent_to_decimal += int(n2[i]) * 2 ** abs((i - (len(n2) - 1)))
                decimal_of_exponent_label.set(exponent_to_decimal)

                mantissa = int(a) * (2 ** 0) + int(b) * (2 ** exp) + int(c) * (2 ** exp2) + int(d) * (2 ** exp3)
                z = len(exponent)
                bias = 2 ** (z - 1) - 1
                ee = (int(exponent_to_decimal) - int(bias))
                two_exponent = 2 ** int(ee) + 0.0
                decimal = (int(exp) ** (int(sign)) * (mantissa * (two_exponent)))
                # decimal = decimal[:5]
                valid = 'Converted!'
                process_status.set(valid)

                # if sign == '0':
                #     decimal = binary_to_decimal
                if binary == '01111000':
                    decimal = '∞'
                if binary == '11111000':
                    decimal = '-∞'
                if exponent == '1111' and fraction != '000':
                    decimal = 'NaN'
                else:
                    decimal = decimal
                decimal_of_final_label.set(decimal)

            elif len(binary) == 16:
                sign = binary[0]
                exponent += binary[1:7]
                fraction += binary[7:16]
                sign_label.set(sign)
                exponent_label.set(exponent)
                fraction_label.set(fraction)

                n = binary.strip()
                binary_to_decimal = 0
                for i in range(len(n)):
                    binary_to_decimal += int(n[i]) * 2 ** abs((i - (len(n) - 1)))
                decimal_of_float_label.set(binary_to_decimal)

                if exponent == '000000':
                    a = 0
                else:
                    a = 1
                b, c, d, e, f, g, h, i, j = fraction[0], fraction[1], fraction[2], fraction[3], \
                                               fraction[4], fraction[5], fraction[6], fraction[7], fraction[8]

                n2 = exponent.strip()
                exponent_to_decimal = 0
                for i in range(len(n2)):
                    exponent_to_decimal += int(n2[i]) * 2 ** abs((i - (len(n2) - 1)))
                decimal_of_exponent_label.set(exponent_to_decimal)

                mantissa = int(a) * (2 ** 0) + int(b) * (2 ** exp) + int(c) * (2 ** exp2) + int(d) * (2 ** exp3) \
                                                                                            * int(e) * (2 ** exp4) \
                                                                                            * int(f) * (2 ** exp5) \
                                                                                            * int(g) * (2 ** exp6) \
                                                                                            * int(h) * (2 ** exp7) \
                                                                                            * int(i) * (2 ** exp8) \
                                                                                            * int(j) * (2 ** exp9)

                z = len(exponent)
                bias = 2 ** (z - 1) - 1
                ee = (int(exponent_to_decimal) - int(bias))
                two_exponent = 2 ** int(ee) + 0.0
                decimal = (int(exp) ** (int(sign)) * (mantissa * (two_exponent)))
                # decimal = decimal[:5]
                valid = 'Converted!'
                process_status.set(valid)

                # if sign == '0':
                #     decimal = binary_to_decimal
                if binary == '0111111000000000':
                    decimal = '∞'
                if binary == '1111111000000000':
                    decimal = '-∞'
                if exponent == '111111' and fraction != '000000000':
                    decimal = 'NaN'
                else:
                    decimal = decimal
                decimal_of_final_label.set(decimal)

            elif len(binary) == 24:
                sign = binary[0]
                exponent += binary[1:9]
                fraction += binary[9:24]
                sign_label.set(sign)
                exponent_label.set(exponent)
                fraction_label.set(fraction)

                n = binary.strip()
                binary_to_decimal = 0
                for i in range(len(n)):
                    binary_to_decimal += int(n[i]) * 2 ** abs((i - (len(n) - 1)))
                decimal_of_float_label.set(binary_to_decimal)

                if exponent == '00000000':
                    a = 0
                else:
                    a = 1
                b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = fraction[0], fraction[1], fraction[2], \
                                                                 fraction[3], fraction[4], fraction[5], fraction[6], \
                                                                 fraction[7], fraction[8], fraction[9], fraction[10], \
                                                                 fraction[11], fraction[12], fraction[13], fraction[14]

                n2 = exponent.strip()
                exponent_to_decimal = 0
                for i in range(len(n2)):
                    exponent_to_decimal += int(n2[i]) * 2 ** abs((i - (len(n2) - 1)))
                decimal_of_exponent_label.set(exponent_to_decimal)

                mantissa = int(a) * (2 ** 0) + int(b) * (2 ** exp) + int(c) * (2 ** exp2) + int(d) * (2 ** exp3) * int(
                    e) * (2 ** exp4) * int(f) * (2 ** exp5) * int(g) * (2 ** exp6) * int(h) * (2 ** exp7) * int(i) * (
                                                                                                2 ** exp8) * int(j) * (
                                                                                                2 ** exp9) * int(k) * (
                                                                                                2 ** exp10) * int(l) * (
                                                                                                2 ** exp11) * int(m) * (
                                                                                                2 ** exp12) * int(n) * (
                                                                                                2 ** exp13) * int(o) * (
                                                                                                2 ** exp14) * int(p) * (
                                                                                                2 ** exp15)

                z = len(exponent)
                bias = 2 ** (z - 1) - 1
                ee = (int(exponent_to_decimal) - int(bias))
                two_exponent = 2 ** int(ee) + 0.0
                decimal = (int(exp) ** (int(sign)) * (mantissa * (two_exponent)))
                # decimal = decimal[:5]

                # if sign == '0':
                #     decimal = binary_to_decimal
                if binary == '011111111000000000000000':
                    decimal = '∞'
                if binary == '111111111000000000000000':
                    decimal = '-∞'
                if exponent == '11111111' and fraction != '000000000000000':
                    decimal = 'NaN'
                else:
                    decimal = decimal
                decimal_of_final_label.set(decimal)
                valid = 'Converted!'
                process_status.set(valid)

            elif len(binary) == 32:
                sign = binary[0]
                exponent += binary[1:11]
                fraction += binary[11:32]
                sign_label.set(sign)
                exponent_label.set(exponent)
                fraction_label.set(fraction)

                n = binary.strip()
                binary_to_decimal = 0
                for i in range(len(n)):
                    binary_to_decimal += int(n[i]) * 2 ** abs((i - (len(n) - 1)))
                decimal_of_float_label.set(binary_to_decimal)

                if exponent == '000000':
                    a = 0
                else:
                    a = 1
                b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v = fraction[0], fraction[1], \
                                                                                   fraction[2], fraction[3], fraction[4], \
                                                                                   fraction[5], fraction[6], fraction[7], \
                                                                                   fraction[8], fraction[9], fraction[10], \
                                                                                   fraction[11], fraction[12], fraction[13], \
                                                                                   fraction[14], fraction[15], fraction[16], \
                                                                                   fraction[17], fraction[18], fraction[19], \
                                                                                   fraction[20]

                n2 = exponent.strip()
                exponent_to_decimal = 0
                for i in range(len(n2)):
                    exponent_to_decimal += int(n2[i]) * 2 ** abs((i - (len(n2) - 1)))
                decimal_of_exponent_label.set(exponent_to_decimal)

                mantissa = int(a) * (2 ** 0) + int(b) * (2 ** exp) + int(c) * (2 ** exp2) + int(d) * (2 ** exp3) * int(
                    e) * (2 ** exp4) * int(f) * (2 ** exp5) * int(g) * (2 ** exp6) * int(h) * (2 ** exp7) * int(i) * (
                                                                                                2 ** exp8) * int(j) * (
                                                                                                2 ** exp9) * int(k) * (
                                                                                                2 ** exp10) * int(l) * (
                                                                                                2 ** exp11) * int(m) * (
                                                                                                2 ** exp12) * int(n) * (
                                                                                                2 ** exp13) * int(o) * (
                                                                                                2 ** exp14) * int(p) * (
                                                                                                2 ** exp15) * int(q) * (
                                                                                                2 ** exp16) * int(r) * (
                                                                                                2 ** exp17) * int(s) * (
                                                                                                2 ** exp18) * int(t) * (
                                                                                                2 ** exp19) * int(u) * (
                                                                                                2 ** exp20) * int(v) * (
                                                                                                2 ** exp21)

                z = len(exponent)
                bias = 2 ** (z - 1) - 1
                ee = (int(exponent_to_decimal) - int(bias))
                two_exponent = 2 ** int(ee) + 0.0
                decimal = (int(exp) ** (int(sign)) * (mantissa * (two_exponent)))
                # decimal = decimal[:5]
                valid = 'Converted!'
                process_status.set(valid)

                # if sign == '0':
                #     decimal = binary_to_decimal
                if binary == '01111111111000000000000000000000':
                    decimal = '∞'
                if binary == '11111111111000000000000000000000':
                    decimal = '-∞'
                if exponent == '1111111111' and fraction != '000000000000000000000':
                    decimal = 'NaN'
                else:
                    decimal = decimal
                decimal_of_final_label.set(decimal)

def converter():
    empty = ''
    float_label.set(empty)
    binary_label.set(empty)
    decimal_of_float_label.set(empty)
    sign_label.set(empty)
    exponent_label.set(empty)
    decimal_of_exponent_label.set(empty)
    fraction_label.set(empty)
    decimal_of_final_label.set(empty)
    process_status.set(empty)

    y = (entry_var2.get())
    if y == 'S':
        twos_complement()
    if y == 's':
        twos_complement()
    if y == 'U':
        unsigned_converter()
    if y == 'u':
        unsigned_converter()
    if y == 'F':
        float()
    if y == 'f':
        float()
    else:
        invalid = 'Please enter the data type correctly!'
        process_status.set(invalid)

top = tkinter.Tk()
top.title("Converter")

float_frame = tkinter.Frame(top)
first = tkinter.Frame(top)
second = tkinter.Frame(top)
third = tkinter.Frame(top)
fourth = tkinter.Frame(top)
fifth = tkinter.Frame(top)
sixth = tkinter.Frame(top)
last = tkinter.Frame(top)
status = tkinter.Frame(top)

entry_frame=tkinter.Frame(top)
entry_var = tkinter.StringVar()
labelhex = tkinter.Label(entry_frame, width=10, height=2, text='Enter your hexadecimal number:')
entry = tkinter.Entry(entry_frame, textvariable=entry_var)
entry.bind("<Return>")
labelhex.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
entry.pack(side=tkinter.LEFT,fill=tkinter.BOTH, expand=1)
entry_frame.pack(fill=tkinter.BOTH, expand=1)

entry_frame2=tkinter.Frame(top)
entry_var2 = tkinter.StringVar()
labeltype = tkinter.Label(entry_frame2, width=10, height=2, text='Enter the type (F, S, U:)')
entry2 = tkinter.Entry(entry_frame2, textvariable=entry_var2)
entry2.bind("<Return>")
labeltype.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
entry2.pack(side=tkinter.LEFT,fill=tkinter.BOTH, expand=1)
entry_frame2.pack(fill=tkinter.BOTH, expand=1)

start_frame = tkinter.Frame(top)
start_button = tkinter.Button(start_frame, text="Convert", height=2, width=13, bg='Aqua', command=converter)
start_button.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
start_frame.pack(fill=tkinter.BOTH, expand=1)

float_label = tkinter.StringVar()
binary_label = tkinter.StringVar()
decimal_of_float_label = tkinter.StringVar()
sign_label = tkinter.StringVar()
exponent_label = tkinter.StringVar()
decimal_of_exponent_label = tkinter.StringVar()
fraction_label = tkinter.StringVar()
decimal_of_final_label = tkinter.StringVar()
process_status = tkinter.StringVar()

label = tkinter.Label(float_frame, width=30, height=2, text='Floating point number:')
label2 = tkinter.Label(float_frame, width=40, textvariable=float_label)
label.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
label2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
float_frame.pack(fill=tkinter.BOTH, expand=1)

label3 = tkinter.Label(first, width=30, height=2, text='Binary value of entered number:')
label4 = tkinter.Label(first, width=40, height=2, textvariable=binary_label)
label3.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
label4.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
first.pack(fill=tkinter.BOTH, expand=1)

label5 = tkinter.Label(second, width=30, height=2, text='Decimal value of entered number:')
label6 = tkinter.Label(second, width=40, textvariable=decimal_of_float_label)
label5.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
label6.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
second.pack(fill=tkinter.BOTH, expand=1)

label7 = tkinter.Label(third, width=30, height=2, text='Sign bit:')
label8 = tkinter.Label(third, width=40, height=2, textvariable=sign_label)
label7.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
label8.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
third.pack(fill=tkinter.BOTH, expand=1)

label9 = tkinter.Label(fourth, width=30, height=2, text='Exponent:')
label10 = tkinter.Label(fourth, width=40, height=2, textvariable=exponent_label)
label9.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
label10.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
fourth.pack(fill=tkinter.BOTH, expand=1)

label11 = tkinter.Label(fifth, width=30, height=2, text='Decimal value of exponent:')
label12 = tkinter.Label(fifth, width=40, height=2, textvariable=decimal_of_exponent_label)
label11.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
label12.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
fifth.pack(fill=tkinter.BOTH, expand=1)

label13 = tkinter.Label(sixth, width=30, height=2, text='Fraction:')
label14 = tkinter.Label(sixth, width=40, height=2, textvariable=fraction_label)
label13.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
label14.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
sixth.pack(fill=tkinter.BOTH, expand=1),

label15 = tkinter.Label(last, width=30, height=2, text='Decimal value of converted number:')
label16 = tkinter.Label(last, width=40, height=2, textvariable=decimal_of_final_label)
label15.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
label16.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
last.pack(fill=tkinter.BOTH, expand=1)

label17 = tkinter.Label(status, width=40, height=2, textvariable=process_status, bg='Aqua')
label17.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
status.pack(fill=tkinter.BOTH, expand=1)

tkinter.mainloop()