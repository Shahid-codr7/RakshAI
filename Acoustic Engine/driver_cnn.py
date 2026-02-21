import tensorflow as tf
import numpy as np
import librosa

def load_model_and_predict(file_path, model_path='deepfake_audio_detector_CNN.h5'):
    """
    Loads a saved DeepFake Audio Detector model and predicts the class of an audio file.

    Args:
        file_path (str): Path to the audio file (e.g., .wav, .mp3).
        model_path (str): Path to the saved Keras model file.

    Returns:
        str: Prediction result (e.g., 'REAL (Confidence: 0.95)', 'FAKE (Confidence: 0.88)').
    """
    try:
        # 1. Load the model
        loaded_model = tf.keras.models.load_model(model_path)
        print(f"Model loaded successfully from {model_path}")

        # 2. Extract features using the existing function
        feature = extract_features(file_path)
        if feature is None:
            return "Error: Could not extract features from the audio file."

        # 3. Add batch dimension for prediction
        feature = np.expand_dims(feature, axis=0) # Add batch dimension

        # 4. Make prediction
        prediction = loaded_model.predict(feature)[0][0]

        # 5. Interpret result
        label = "FAKE" if prediction > 0.5 else "REAL"
        confidence = prediction if prediction > 0.5 else 1 - prediction
        return f"{label} (Confidence: {confidence:.2f})"

    except Exception as e:
        return f"An error occurred during prediction: {e}"
