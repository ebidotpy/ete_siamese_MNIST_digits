import tensorflow as tf

# Create a function to parse the MNIST dataset files
def parse_mnist(image_file, label_file):
    image = tf.io.decode_raw(tf.io.read_file(image_file), tf.uint8)
    image = tf.reshape(image, [-1, 28, 28, 1])
    image = tf.cast(image, tf.float32) / 255.0

    label = tf.io.decode_raw(tf.io.read_file(label_file), tf.uint8)
    label = tf.reshape(label, [-1])
    label = tf.cast(label, tf.int32)

    return image, label

# Define the paths to the downloaded MNIST dataset files
train_images_file = "MNIST/train-images-idx3-ubyte"
train_labels_file = "MNIST/train-labels-idx1-ubyte"
test_images_file = "MNIST/t10k-images-idx3-ubyte"
test_labels_file = "MNIST/t10k-labels-idx1-ubyte"

# Create TensorFlow datasets for training and testing
train_dataset = tf.data.Dataset.from_tensor_slices((train_images_file, train_labels_file))
test_dataset = tf.data.Dataset.from_tensor_slices((test_images_file, test_labels_file))

# Parse the dataset files and apply any desired transformations
train_dataset = train_dataset.map(parse_mnist)
test_dataset = test_dataset.map(parse_mnist)

# Perform any additional preprocessing or augmentation if needed

# Shuffle and batch the datasets
batch_size = 32
train_dataset = train_dataset.shuffle(buffer_size=10000).batch(batch_size)
test_dataset = test_dataset.batch(batch_size)

# Use the datasets for training and evaluation
model = tf.keras.models.Sequential()
# Build and compile your model

model.fit(train_dataset, epochs=10)
model.evaluate(test_dataset)
