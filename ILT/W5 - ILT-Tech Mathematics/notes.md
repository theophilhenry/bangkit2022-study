## Outline Session
- Introduction t Linear Algebra & Calculus
- Basic Statistics of Data
- PCA

By `Kevin Filmawan`

## Introduction to Linear Algebra
You can view data-point as vectors. List of numbers,<br>
Basically a single vector. However have many dat apoints. We can extends in mutiple vector to have a 2d vector. 

- What does dot product relate with projection, 
- how to understand the concequence of non-orthogonal/orthogonal to a determinant
- What does it mean normalizing a vector? 
Rupiah, one rupiah to 100 rupiah. <br>
This big number might be overwhelming, you might want to transform it. From a billion to 10, much more scalable.
like orthonormal?
- What does it mean to be normal on a plane?

<br>

- What does eigen-basis means? and why we can find it using diagonal eigen-values vector? I don't understand the projection of the T matrix, to a diagonal matrix.
- Why eigen values and eigen values useful, to a diagonal transformation?

## Examples of Linear Algebra in Machine Learning
How do PageRank works?<br>
Popularity means visit. How does the website are connected to each other. Much connected, more popular. 

You can writes all the probability of connected websites. Transform the graph into a matrix. 
Say we start with A, How can A go to B? A->C->D, A->D->B, A->B. right?.<br>
How do we map the probabilities? Find the smallest step.

Say we have a transformation matrix. And we want to multiply a matrix v, with that A multiple times. 

## Introduction to Calculus
Gradient 
https://www.coursera.org/learn/multivariate-calculus-machine-learning/resources/2Cv5P

## Statistics for Machine Learning
All skewness of data distribution depends on the population.

- Why in some equation we use variance, why sometimes we use Standard Deviation. 

Variance : How much should we trust the mean value. 

`Covariance` : Relationship between variance between 2 dataset.<br>
- Positive Correlation :  1 goes up, the other goes up
- Negative : 1 goes up, the other goes down.
- Zero : No relation at all,

What happen with 2 data have zero?

## Outliers
To detect Outlier, we can use IQR or STD.

<hr>

## PCA
Pricipal Component Analysis

Data often high in dimensionality. Working with High Dimension comes with prices. We can reduce it with `Dimensionality Reduction` like `PCA`.

PCA : Pick feature where maintain the level of accuracy, while doing it faster!

We will project a point, to a line. We change the data from spreading, into 1 linear line.

### When you should use PCA
When we have weight and age. If I supressed it to 1 dimensional space. This will be a completely non-describable data points. There is column name for it. It is basically aggregation of the previous (weight and age).

The transformation cannot be identify. But it shares the sanme property, which you can use in the model.

> Why mark is unhealthy?? You cannot to tell why. The features has been aggregated.

If you want to variables are independnt of one another. This is part of the covariance.

- Choosing Eigenvectors, the most interesting. You must choose wisely. Say 10Dimension. To what dimension though? 3D? 2D? what number is the best. 1 Idea is to brute-force, and see what the best. However it takes a lot of time. 

> Do we need to apply PCA to an Image?

> Why PCA improve the classification model? It shares the same property as the original data right?

This is not guaranteed, can be worse or better. Why it can be better?<br>
You can actually clean up a column that is irrelevant. Delete the data points that's not beneficial to the data.<br>
It is not guaranteed improvement. 

Actually the most common uses is about to visualize the data. 10D data right? now we can visualize in 2D.

How to handles the downside of PCA?
- For visualization : No downside
- You can maintain data variance. The variance of the data, should be as similar as possible to the original data. The behaviour and distribution should kurleb the sane.

Multicolinearity : Depends on the data, when you use to detect features that are not really relevant. They don't have relationship between the label. 


### Demo from a Class
Demo PCA from scratch & use scikit-learn: https://colab.research.google.com/drive/1tqCvpEcDDB9_kZ0PihRLDg8ZWmyJCDcg?usp=sharing 

Demo Improve the Accuracy of the Classification Model using PCA : https://colab.research.google.com/drive/1qKSszYc3TMTEP7xsHbq0X-i_AluJqNtw?usp=sharing 

- `Stadardization` : 

- `Normalization` : 