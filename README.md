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
4 $\le$ **N** $\le$ INFINITE <br>
NEGATIVE INFINITE $\le$ **N** $\le$ INFINITE <br>

### Sample Input 1
> 5 <br> 
100 150 <br>
3 150 <br>
100 400 <br>
3 400 <br>
0 0 <br>

### Sample Output 1
> It is possible <br>
One of rectangle: [[1, 1], [1, 2], [9, 1], [9, 2]]

### Sample Input 2
>4 <br>
3 3 <br>
-3 - <br>
4 3 <br>
-4 -3 <br>

### Sample Output 2
> It is not possible <br>
