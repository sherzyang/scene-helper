import tensorflow as tf

# Create a simple tensor
tensor = tf.constant([[1, 2], [3, 4]])
print('Tensor:', tensor)
# Perform a simple operation
result = tf.add(tensor, 10)
print('Tensor after addition:', result)