chose = input('Which way do you want to convert, Celsius into Fahrenheit or conversely?')
if chose != 'Celsius into Fahrenheit' and chose != 'Fahrenheit into Celsius' :
	print('please write Celsius into Fahrenheit or Fahrenheit into Celsius and restart')
if chose == 'Celsius into Fahrenheit' :
	cel = input('please input the value of Celsius')
	cel = float(cel)
	fah = cel * 1.8 + 32
	print(cel, 'Celsius is', fah, 'Fahrenheit')
if chose == 'Fahrenheit into Celsius' :
	fah = input('please input the value of Fahrenheit')
	fah = float(fah)
	cel = (fah-32)/1.8
	print(fah, 'Fahrenheit is', cel, 'Celsius')
