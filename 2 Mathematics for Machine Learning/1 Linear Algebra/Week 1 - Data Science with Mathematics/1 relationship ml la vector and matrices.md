<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Linear Aljebra <hr/>
We will see what problem we want to solve, and why linear aljebra can help them

1. One of Price Discovery
Say Buy Apples and Bananas. 
```
2a + 3b = 8
10a + 1b = 13
```
a? b? It is linear in their coeffients. 

We can write it like so
```
((2,3), (10,1)) [a,b] = [a,b]
```

2. Another problem is optimazation problem. fitting equation to some data with some fitting parametters. 

> How to have an equation, that describe some graph

<br>

## Vectors <hr/>
Say we want to fit equation for the distribution of height
- sigma : how wide the/spread the distribution
- miu : the center point of distribution

f(x) = ... # Some equation here<br>
Because there's 100%, it is normalizad so the area of this distribution is 1.

Now, how do we fit this distribution by finding the right mu and sigma?

The manual way :<br>
- Say you overspread the sigma (spread is bigger), but the same miu. 
- We could add up the difference between the measurements. <br>
Find the underestimate height, and overestimate spread. You could add up, or in fact, the squares of them<br>
To get a measure of the goodness/badness of the fit.

We'll look in detail once you done all the vectors work, the calculus work, then we can plot thatgoodness varied as we change thefitting parameters (sigma and miu).  

We cloud plot, for the given value of miu and sigma, what's the difference was. 0,0 means the best since no difference. If you overestimate the miu, you get the difference higher, if you underestimate, you get a minus miu.

You could plot all of the values where we have the same value of goodness/badness for different values of mu and sigma. We'll then have a multiple contours of plot.

How we could get the right miu and sigma faster? Do : 
- if I do a little move, does the sigma and miu get better or worse? If that get's better, you'll want to keep moving in that direction.

You could have a vector of [miu, sigma] and vector of [miu', sigma'] to see direction.

If you could find what the steepest way down the hill was. 

`Vectors` can describe directions along any sorts of axes. <br>

You can write vector like a list of car compositions.<br>
We can write in a vector, all of the things about the car. 
- Cost in euros
- Emissions performance in grams of CO2 per 100 km
- Nox performance, how much t polluted city and killed people due to air pollution
- Euro NCAP star rating, how good it was in a crash
- Top speed

That's more of a science view of vectors.

Whereas the spatial view is more familiar from physics.
- Any alloy being described by a vector. Composition of that alloy. 

Space is 4D. 3D of metres, and 1D of time.

Btw, to minimize SSR, move repulsive to the contour, not along the contour.




