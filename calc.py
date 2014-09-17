#!/usr/bin/python
import cgi
import cgitb
import string
import sys

cgitb.enable()
form = cgi.FieldStorage()

#Function to convert decimal to binary
def binary_to_decimal(binary):
       decimal=0
       for i in range(len(str(binary))):
           power=len(str(binary))-(i+1)
           decimal+=int(str(binary)[i])*(2**power)
       return decimal

#Function to convert binary to decimal
def decimal_to_binary(arr,decimal):
       if decimal ==1:
           arr.append(1)
       else:
           rem = decimal%2
           arr.append(rem)
           rev = decimal/2
           decimal_to_binary(arr,rev)
       string=""
       for i in arr[::-1]:
           string+=str(i)
       return string


#Function first convert bianry to decimal and then add the two numbers and then convert back the sum to binary
def add(x,y):
		decimaladd = 0
		
		maxlen = max(len(x), len(y))
		
		maxlen = maxlen + 1
		
		decimalx = binary_to_decimal(x)
		
		decimaly = binary_to_decimal(y)
	
		decimaladd = decimalx + decimaly
	
		result = decimal_to_binary([],decimaladd)
		
		my_string = str(result)
	
		if my_string[:1] == '0':return result[1:]
		else: return result[0:]

#Function to get 1's complement of number
def onescomp(binstr):
    return ''.join('1' if b=='0' else '0' for b in binstr)

#Function to get 2's complement of number
def twoscomp(binstr):
    return bin(int(onescomp(binstr),2)+1)[2:]

#Function first convert second number to 2's complement and then call the add function on both the numbers and the result is shown in binary format
def sub(x,y):
		
		maxlen = max(len(x), len(y))
		
		decimalx = binary_to_decimal(x)
		
		decimaly = binary_to_decimal(y)
		
		result = add(x,twoscomp(y))
			
		decimaladd = decimalx + decimaly

		if decimalx > decimaly:return result[1:]
		else: return result[0:]
		
#Function that performs logical AND operation according to the bits in first and second number
def and_oper(x,y):
        maxlen = max(len(x), len(y))

        #Normalize lengths
        x = x.zfill(maxlen)
        y = y.zfill(maxlen)

        result = ''
       
	for i in range(maxlen-1, -1, -1):
	 if x[i] == '1' and y[i] == '1':result = '1' + result
	 elif x[i] == '0' and y[i] == '0':result = '0' + result
	 elif x[i] == '0' and y[i] == '1':result = '0' + result
	 else: result = '0' + result

	return result.zfill(maxlen)

#Function that performs logical OR operation according to the bits in first and second number
def or_oper(x,y):
        maxlen = max(len(x), len(y))

        #Normalize lengths
        x = x.zfill(maxlen)
        y = y.zfill(maxlen)

        result = ''
       
	for i in range(maxlen-1, -1, -1):
	 if x[i] == '1' and y[i] == '1':result = '1' + result
	 elif x[i] == '0' and y[i] == '0':result = '0' + result
	 elif x[i] == '0' and y[i] == '1':result = '1' + result
	 else: result = '1' + result

	return result.zfill(maxlen)

#Function that performs logical XOR operation according to the bits in first and second number
def xor_oper(x,y):
        maxlen = max(len(x), len(y))

        #Normalize lengths
        x = x.zfill(maxlen)
        y = y.zfill(maxlen)

        result = ''
       
	for i in range(maxlen-1, -1, -1):
	 if x[i] == '1' and y[i] == '1':result = '0' + result
	 elif x[i] == '0' and y[i] == '0':result = '0' + result
	 elif x[i] == '0' and y[i] == '1':result = '1' + result
	 else:result = '1' + result

	return result.zfill(maxlen)

x = '0'
y = '0'
z = '0'
result = '0'


o = form.getvalue("output")
p = form.getvalue("val")
op = form.getvalue("op")
val = form.getvalue("Language")

op1 = form.getvalue("op1")

mem = form.getvalue("mem")
#This is the actual control flow according to the event user performs

if op == "+": z=op;op1=z;x = o;val = x;result = ""
elif op == "-": z=op;op1=z;x = o;val = x;result = ""
elif op == "AND": z=op;op1=z;x = o;val = x;result = ""
elif op == "OR": z=op;op1=z;x = o;val = x;result = ""
elif op == "XOR": z=op;op1=z;x = o;val = x;result = ""
elif op == "=":
	if op1 == "+": y = o;x = val;result = add(x,y)
	elif op1 == "-": y = o;x = val;result = sub(x,y)
	elif op1 == "AND": y = o;x = val;result = and_oper(x,y)
	elif op1 == "OR": y = o;x = val;result = or_oper(x,y)
	else: y = o;x = val;result = xor_oper(x,y)
elif op == "C": result = ""
elif op == "MC": 
	mem = "";
	if o is not None:result = o
	else: result = ""
elif op == "MS": 
	if o is not None:mem = o; result = ""
	else: mem = "" ;result = ""	
elif op == "MR": 
	if mem is not None:result = mem
	else: result = ""
else:
	if o is not None and  p is not None:result = o + str(p)
	elif o is not None and p is None: result = o
	elif o is None and p is not None:result = str(p)
	elif o is None and p is None:result = ""


out = str(result)

print "Content-type: text/html"
print

#This is the actual html code

print '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">'
	   
print "<html><head><title>BINARY CALCULATOR</title></head>"
print "<body style=\"margin-top: 100px; margin-left: 100px; margin-right: 100px;margin-bottom:100px;\" bgcolor=#154734>"
print "<p style=\"font:40px arial,sans-serif,centre;color:#CC6666;text-align:left;\">    BINARY CALCULATOR</p>"
print "<form action=http://harvey2.cc.binghamton.edu/~pmore2/cgi-bin/calc.py method=post>"
print "<table>"
print "<tr>" 
print "<td colspan = 4><input readonly style = \"background: #33CC99; height:55px; width: 600px;text-align:right;font-size:35px; border-radius: 2em; border:6px solid #339999;border-radius:29px; color: #fff; padding-left: 1.5em; outline: none; box-shadow: 0 4px 6px -5px hsl(0, 0%, 40%), inset 0px 4px 6px -5px hsl(0, 0%, 2%) \" maxlength=8 pattern=[0-1.]+ title=Only_8_bit_value(0or1) placeholder=Only_8_bit_value(0or1) name=output value="+out+" >"
print "<tr>"
print "<td><input type=submit name=op value=MC style=\"background-color: #2e466e; color: #fff; border-radius: 10px;border:6px solid #1f2f47;border-radius:29px;padding:16px 57px;text-shadow:0px 1px 0px #263666;font-size:20px;\"\>"
print "<td><input type=submit name=op value=MR style=\"background-color: #2e466e; color: #fff; border-radius: 10px;border:6px solid #1f2f47;border-radius:29px;padding:16px 57px;text-shadow:0px 1px 0px #263666;font-size:20px;\"\>"
print "<td><input type=submit name=op value=MS style=\"background-color: #2e466e; color: #fff; border-radius: 10px;border:6px solid #1f2f47;border-radius:29px;padding:16px 57px;text-shadow:0px 1px 0px #263666;font-size:20px;\"\>"
print "<td><input type=submit name=op value=C style=\"background-color: #2e466e; color: #fff; border-radius: 10px;border:6px solid #1f2f47;border-radius:29px;padding:16px 57px;text-shadow:0px 1px 0px #263666;font-size:20px;\"\>"
print "<tr>"
print "<td><input type=submit name=val value=0 style=\"background-color: #2e466e; color: #fff; border-radius: 10px;border:6px solid #1f2f47;border-radius:29px;padding:16px 57px;text-shadow:0px 1px 0px #263666;font-size:20px;\"\>"
print "<td><input type=submit name=val value=1 style=\"background-color: #2e466e; color: #fff; border-radius: 10px;border:6px solid #1f2f47;border-radius:29px;padding:16px 57px;text-shadow:0px 1px 0px #263666;font-size:20px;\"\>"
print "<td><input type=submit name=op value=+ style=\"background-color: #2e466e; color: #fff; border-radius: 10px;border:6px solid #1f2f47;border-radius:29px;padding:16px 57px;text-shadow:0px 1px 0px #263666;font-size:20px;\"\>"
print "<td><input type=submit name=op value=- style=\"background-color: #2e466e; color: #fff; border-radius: 10px;border:6px solid #1f2f47;border-radius:29px;padding:16px 57px;text-shadow:0px 1px 0px #263666;font-size:20px;\"\>"
print "<tr>"
print "<td><input type=submit name=op value=AND style=\"background-color: #2e466e; color: #fff; border-radius: 10px;border:6px solid #1f2f47;border-radius:29px;padding:16px 57px;text-shadow:0px 1px 0px #263666;font-size:20px;\"\>"
print "<td><input type=submit name=op value=OR style=\"background-color: #2e466e; color: #fff; border-radius: 10px;border:6px solid #1f2f47;border-radius:29px;padding:16px 57px;text-shadow:0px 1px 0px #263666;font-size:20px;\"\>"
print "<td><input type=submit name=op value=XOR style=\"background-color: #2e466e; color: #fff; border-radius: 10px;border:6px solid #1f2f47;border-radius:29px;padding:16px 57px;text-shadow:0px 1px 0px #263666;font-size:20px;\"\>"
print "<td><input type=submit name=op value== style=\"background-color: #2e466e; color: #fff; border-radius: 10px;border:6px solid #1f2f47;border-radius:29px;padding:16px 57px;text-shadow:0px 1px 0px #263666;font-size:20px;\"\>"
print "</table>"
print "<input type=hidden name=Language value="+str(val)+">"
print "<input type=hidden name=op1 value="+str(op1)+">"
print "<input type=hidden name=mem value="+str(mem)+">"
print "</form>"
print "</body></html>"




