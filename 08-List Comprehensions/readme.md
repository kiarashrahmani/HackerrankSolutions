<h2>list comprehensions</h2>

<p>You are given three integers <code>x</code>, <code>y</code>, and <code>z</code> representing the dimensions of a cuboid, along with an integer <code>n</code>. You need to print a list of all possible coordinates <code>(i, j, k)</code> on a 3D grid where the sum of <code>i + j + k</code> is not equal to <code>n</code>. Here, <code>0 ≤ i ≤ x</code>, <code>0 ≤ j ≤ y</code>, and <code>0 ≤ k ≤ z</code>. Please use list comprehensions rather than multiple loops, as a learning exercise.</p>

<p><strong>Example:</strong></p>

<pre><code>x = 1
y = 1
z = 2
n = 3

# All permutations of (i, j, k) are:
# [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2)]

# Print an array of the elements that do not sum to n.
coordinates = [(i, j, k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
print(coordinates)
</code></pre>

<p><strong>Input Format:</strong></p>

<p>Four integers <code>x</code>, <code>y</code>, <code>z</code>, and <code>n</code>, each on a separate line.</p>

<p><strong>Constraints:</strong></p>

<ul>
<li>Print the list in lexicographic increasing order</li>
</ul>

<p><strong>Output Format:</strong></p>

<p>Print the list of coordinates in lexicographic increasing order.</p>