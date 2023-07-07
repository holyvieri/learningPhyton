"""The map(int, input().split()) function applies the int() function to each element in the list.
It effectively converts each element from a string to an integer.
So, map(int, input().split()) would return an iterator object that yields the integer values 3, 4, and 5.

Finally, the line a, b, c = map(int, input().split()) uses multiple assignment to assign the values from
the iterator object to the variables a, b, and c.
So, after this line of code, the variables a, b, and c will hold the integer values corresponding to
the side lengths entered by the user.

For example, if the user entered 3 4 5, then a would be 3, b would be 4, and c would be 5.

This approach allows you to conveniently read multiple input values on a single line and
assign them to individual variables for further processing.
"""


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


# Read the input side lengths
a, b, c = map(float, input().split())

if is_triangle(a, b, c):
    print(f'Perimetro = {(a + b + c):.1f}')
else:
    print(f'Area = {((a+b)*c)/2:.1f}')