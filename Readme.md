# Sum Model using TensorFlow

This project consists of two Python scripts (`fit.py` and `app.py`) that implement a simple machine learning model using TensorFlow to add two randomly generated numbers.

## Project Files

- `fit.py`: This script is used to generate and train the model.
- `app.py`: Here the previously trained model is loaded to make sum predictions.
- `modelo_suma.h5`: File where the trained model is saved.

## Requirements

The project requirements are found in the `requirements.txt` file. Make sure you have the necessary packages installed by running the following command:

```bash
pip install -r requirements.txt
```

## Use

### Model Training
1. Run `fit.py` to train the model.
     ```bash
     python fit.py
     ```

### Make Predictions
1. Use the `app.py` file to load the trained model and make predictions.
     ```bash
     python app.py
     ```

The model loaded in `app.py` predicts the sum of given pairs of numbers.

## Training Data Example

The `fit.py` script generates 10,000 examples of adding two random numbers between 0 and 100.

## Prediction Example

The `app.py` script uses the pre-trained model to make sum predictions with predefined examples.

## Note
Make sure you have TensorFlow and other dependencies installed as specified in the `requirements.txt` file to run the scripts.

Enjoy modeling with TensorFlow! 🚀
