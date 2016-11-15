import math

def line(): #### Just prints a line
    print('-------------------------------------------------')

def force(): ### This function is what generates new values for each force
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

### Main below this point
sum_forcesX = 0
sum_forcesY = 0

sd = int(input('Forces: '))
line()

for n in range(0, sd): ### Instead of creating new variables for each new values of forces(), this loop sums each compx and compy
    forces = force()
    sum_forcesX += forces[0]
    sum_forcesY += forces[1]
    line()
### The previous compx and compy are used for this new calculation
total_force = math.sqrt((sum_forcesX**2)+(sum_forcesY**2))
degrees = math.degrees(math.atan(math.radians(sum_forcesY/sum_forcesX)))
print('The summatory of the forces is:',total_force)
print('with',degrees,'degrees')

### Even if this code is posted on public, I rather keep it to myself until the due date of it, so don't copy it
### I know is not the biggest deal, but as I said, I'm the creator of it, and it costed me a lot to make it work :c
