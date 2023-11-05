from colorama import Fore 
import sys 
import time
degrees='degrees:' 
def delay_function(subseconds):
    time.sleep(subseconds)
    
triangle_msg='Enter 3 angles which add up 180 degrees in any type of triangle\n'
for n in triangle_msg:
    sys.stderr.flush()
    delay_function(0.1)
    sys.stderr.write(f'{Fore.GREEN+n}')
else:
 while True:
    try:
        reset_to_default_color=Fore.RESET
        print(f'{reset_to_default_color}')
        first_angle=int(input(f'{degrees}'))
        delay_function(0.2)
        second_angle=int(input(f'{degrees}'))
        delay_function(0.2)
        third_angle=int(input(f'{degrees}'))
        total_degrees=[first_angle,second_angle,third_angle]
        if sum(total_degrees)>180:
            delay_function(0.2)
            print(Fore.RED+'Not a triangle')
            print(f'{reset_to_default_color}')
        else:
            if sum(total_degrees)==180:
                if total_degrees[0]==60 and total_degrees[1]==60 and total_degrees[2]:
                    print('Your triangle is an equilateral triangle')
                elif total_degrees[0]==90 or total_degrees[1]==90 or total_degrees[2]==90:
                    print('Your triangle is a right angle triangle')
                else:
                    print('Your triangle is a scalene triangle')
    except ValueError:
        pass