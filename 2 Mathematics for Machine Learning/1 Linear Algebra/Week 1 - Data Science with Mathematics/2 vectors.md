<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Operations with Vectors <hr/>
What makes a vector, a vector?

`Vector` : Object that moves us around spaces (physical or data). 

In data science, we can think vector as Just a list of attributes of an object. <br>
It can be a thing that describes the object of a house. Like square feet, num of bedrooms, prices.

Vectors is something based on 2 rules : 
- Addition

    First think vector as just an geometric object starting at an origin.<br>
    Say there's vector r and s<br>
    s + r = r + s


- Multiplication by a Scalar Number

    3a means ->->->
    (-) minus number, means we go back the other way. 

### Vector Coordinate System
Vector Bases (equal to one) : <br>
i : horizontal left to right<br>
j : vertical bottom to top

[3, 2] means 3i and 2j.

#### Addition
To add a vector, just add the components for each i and j!
Vector addition must be `Associative` : If we have 3 vector r s and t. It doesnt mater (r+s) + t. Whichever order it's okay.

#### Multiplication by Scalar?
r = [3, 2]<br>
2r = [6, 4]<br>
-r = [-3, -2]<br>
So, r + (-r) = 0