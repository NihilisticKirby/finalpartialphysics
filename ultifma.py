import math ### Because I will need math. functions

def line(): ### Just prints a line to make the code look better
    print('-------------------------------------------------')
### The function that takes the user's input to calculate the different variables needed
def force():
    f = int(input('Valor de la fuerza: '))
    d = int(input('Valor del ángulo: '))
    if d < 90:
        q = int(input('Cuadrante del ángulo (1,2,3,4): '))
        if q == 2:
            d += 90
        if q == 3:
            d += 180
        if q == 4:
            d += 270
        else:
            d = d
    compx = float(f*math.cos(math.radians(d)))
    compy = float(f*math.sin(math.radians(d)))
    return (compx,compy)

### Main code below this point
sum_forcesX = 0
sum_forcesY = 0
### This variable followed by the loop indicates how many times the function "force()" will be executed
sd = int(input('Forces: '))
line()
for n in range(0, sd):
    forces = force()
    sum_forcesX += forces[0]
    sum_forcesY += forces[1]
    line()
### This part will calculate the sum of the forces as a single vector and the inclination in degrees, in order to print them
total_force = math.sqrt((sum_forcesX**2)+(sum_forcesY**2))
degrees = math.degrees((math.atan(sum_forcesY/sum_forcesX)))
print('The summatory of the forces is:',total_force)
print('with an inclination in degrees of',str(degrees)+'°')

### Even if this code is posted on public, I rather keep it to myself until the due date of it, so don't copy it
### I know is not the biggest deal, but as I said, I'm the creator of it, and it costed me a lot to make it work :c
