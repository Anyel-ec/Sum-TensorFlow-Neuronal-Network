import numpy as np
import tensorflow as tf

# Cargar el modelo entrenado para hacer predicciones
loaded_model = tf.keras.models.load_model("modelo_suma.h5")

# Load the trainer model to make predictions
test_data = np.array([[10, 70], [44, 20], [10, 90]])  # Addition examples to try
predictions = loaded_model.predict(test_data)
for i in range(len(test_data)):
    print(f"Predicción para {test_data[i]}: {predictions[i][0]}")