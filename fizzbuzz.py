minRange : int = 1
maxRange : int = 30
step : int = 1
        
for number in range(minRange, maxRange, step):
    if number % 15 == 0:
        print("fizzbuzz", end =" ")
    else if number % 3 == 0:
        print("fizz", end = " ")
    else 
        print(number, end = " ")
