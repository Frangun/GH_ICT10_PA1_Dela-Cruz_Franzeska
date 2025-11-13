# Working with Sets
from pyscript import display

comarts_club = {'Yciar', 'Kyla', 'Gino'}
math_club = {'Kyla', 'Clar', 'Fran'}


# students who belong to both: kyla  
# students only in first: yciar & gino
# students only in 2nd: clar & fran
# students who are in exactly one club (according to this): clar, fran, yciar, gino

# ampersand
display(comarts_club & math_club, target='output')

# difference
display(comarts_club - math_club, target='output')

display(math_club - comarts_club, target='output')

# symmetric difference
display(comarts_club ^ math_club, target='output')








