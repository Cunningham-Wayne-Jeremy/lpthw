#python doesnt need to say what complier to use like bash
#Thought of this because html does and bash has a specific code to
#enter at the top like #!/bin/bash and DOCTYPE
#ANYWAY lets do some more practive with sys argv
#AS WELL AS COMBINING IT WITH inputs
from sys import argv
prompt = ">"

firstnumber = input(f"Enter the first number:{prompt} ")
operator = input(f"Enter the operator: {prompt} ")
secondnumber = input(f"Enter the second number:{prompt} ")


script, firstnumber, operator, secondnumber = argv

print(f"""Ok you entered {firstnumber} {operator} {secondnumber}.
That equals: """, eval(f'{firstnumber} {operator} {secondnumber}'))

#Ok eval works just be sure to use the escape character when using * otherwise
#It will pop uot an ERROR
