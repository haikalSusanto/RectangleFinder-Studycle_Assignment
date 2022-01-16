# RectangleFinder - Studycle Assignment

### Scripts description
The goal of this scripts is to find whether it is possible to form a rectangle given **N** numbers of coordinates.

### Returns
If possible it will print **"It is possible"** and the next line will be its possible rectangle <br>
If not possible it will print **"It is not possible"**

### Input Format
The first line contains a single integer, **N**, numbers of coordinates.
The **N** subsequent line contains a single coordinates **X**  **Y**

### Constraints
<img src="https://latex.codecogs.com/svg.image?4\leq&space;\textbf{N}&space;\leq&space;\infty" title="4\leq \textbf{N} \leq \infty" alt="4 <= N <= Inf"/>
<img src="https://latex.codecogs.com/svg.image?-\infty&space;\leq&space;\textbf{X,&space;Y}&space;\leq&space;\infty" title="-\infty \leq \textbf{X, Y} \leq \infty" alt="Negative Inf <= X, Y <= Inf"/>

### Sample Input 1
> 5 <br> 
1 1 <br>
3 150 <br>
9 2 <br>
9 1 <br>
1 2 <br>

### Sample Output 1
> It is possible <br>
One of rectangle: [[1, 1], [1, 2], [9, 1], [9, 2]]

### Sample Input 2
>4 <br>
3 3 <br>
-3 -3 <br>
4 3 <br>
-4 -3 <br>

### Sample Output 2
> It is not possible <br>
