
year = int(input())


if year % 4 ==0:
  if year%100 ==0:
    if year%400 == 0:
      print('Leap year')
    else:
      print('Not eap year')   
 
  else:
    print('Leap year')      
else:
  print('Not leap year')
1546