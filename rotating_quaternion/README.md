# Rotating Quaternion

This project demonstrates the use of quaternions for 3D rotations.

## Requirements

- Python 3.x
- NumPy

## Usage

The main script `main.py` contains an example of quaternion rotations. You can modify this example to experiment with different rotations and vectors.

### Modifying the Rotation Example

To experiment with different rotations, you can modify the following parameters in `main.py`:

1. Quaternion creation:
   - Change the axis and angle for `q1` and `q2`
   - Example: `q1 = quaternionTransformed((0, 1, 0), 30)` rotates 30 degrees around the y-axis

2. Initial vector:
   - Modify the `v` vector to start with a different point
   - Example: `v = np.array([0, 1, 1])`

3. Combining rotations:
   - The `q1q2` variable combines the rotations of `q1` and `q2`
   - You can add more quaternions or change the order of multiplication

Here's an example of how you could modify the rotation code:

```python
q1 = quaternionTransformed((0, 1, 0), 30)  # Rotate 30 degrees around y-axis
q2 = quaternionTransformed((0, 0, 1), 60)  # Rotate 60 degrees around z-axis
v = np.array([0, 1, 1])  # Change the initial vector

q1q2 = multiplyQuaternions(q1, q2)
print("Rotation with q1:", rotatePoint(q1, v))
print("Rotation with q2:", rotatePoint(q2, v))
print("Combined rotation q1q2:", rotatePoint(q1q2, v))
