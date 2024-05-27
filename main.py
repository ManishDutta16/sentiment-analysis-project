# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from flask import Flask, request, jsonify
# import csv
# import pickle
# import os


# from flask import Flask,request, jsonify
# import csv
# import pickle
# import os
# import tensorflow as tf
# from keras.preprocessing import pad_sequences
# from keras.models import load_model

# app = Flask(__name__)

# # Load the model
# try:
#     model = load_model('model.h5')
# except Exception as e:
#     print(f"Error loading model: {e}")

# # Load the tokenizer
# try:
#     with open('tokenizer.pkl', 'rb') as f:
#         tokenizer = pickle.load(f)
# except Exception as e:
#     print(f"Error loading tokenizer: {e}")

# max_length = 100  # Update this according to your model's requirement

# def preprocess(text):
#     # Add your preprocessing steps here
#     return text.lower()

# def predict_custom_input(model, tokenizer, input_text, max_length):
#     cleaned_text = preprocess(input_text)
#     sequence = tokenizer.texts_to_sequences([cleaned_text])
#     padded_sequence = pad_sequences(sequence, maxlen=max_length)
#     prediction = model.predict(padded_sequence)[0][0]
#     sentiment = "Positive" if prediction >= 0.5 else "Negative"
#     return sentiment

# @app.route('/upload', methods=['POST'])
# def upload():
#     try:
#         # Check if the post request has the file part
#         if 'file' not in request.files:
#             return jsonify({'error': 'No file part in the request.'}), 400

#         file = request.files['file']

#         # If user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             return jsonify({'error': 'No selected file.'}), 400

#         # Save the uploaded file
#         file_path = os.path.join(os.getcwd(), 'translated_comments.csv')
#         file.save(file_path)

#         return jsonify({'message': 'File uploaded successfully.'})

#     except Exception as e:
#         print(f"Error uploading file: {e}")
#         return jsonify({'error': 'An error occurred while uploading the file.'}), 500

# @app.route('/predict_negative_comments', methods=['POST'])
# def predict_negative_comments():
#     try:
#         # Load translated comments from the uploaded file
#         translated_comments_path = os.path.join(os.getcwd(), 'translated_comments.csv')
#         # Process translated comments to identify negative ones and save them to negative_comments.csv
#         # Here you would implement the logic to read the translated comments, predict sentiments, and save negative comments to negative_comments.csv
#         return jsonify({'message': 'Prediction of negative comments completed and saved to negative_comments.csv.'})

#     except Exception as e:
#         print(f"Error predicting negative comments: {e}")
#         return jsonify({'error': 'An error occurred while predicting negative comments.'}), 500

# if __name__ == '__main__':
#     try:
#         app.run(debug=True)
#     except Exception as e:
#         print(f"Error running Flask app: {e}")





from flask import Flask, request, jsonify
import os
import pickle
import csv

app = Flask(__name__)

# Load the model
model = None
try:
    with open('model.h5', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {e}")

# Load the tokenizer
tokenizer = None
try:
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
except Exception as e:
    print(f"Error loading tokenizer: {e}")

max_length = 100  # Update this according to your model's requirement

def preprocess(text):
    """Preprocess the input text."""
    return text.lower()

def predict_custom_input(model, tokenizer, input_text, max_length):
    """Predict sentiment of the input text using the loaded model and tokenizer."""
    cleaned_text = preprocess(input_text)
    sequence = tokenizer.texts_to_sequences([cleaned_text])
    prediction = model.predict(sequence)[0][0]
    sentiment = "Positive" if prediction >= 0.5 else "Negative"
    return sentiment

@app.route('/upload', methods=['POST'])
def upload():
    """Handle file upload."""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request.'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file.'}), 400

        file_path = os.path.join(os.getcwd(), 'translated_comments.csv')
        file.save(file_path)

        return jsonify({'message': 'File uploaded successfully.'})

    except Exception as e:
        print(f"Error uploading file: {e}")
        return jsonify({'error': 'An error occurred while uploading the file.'}), 500

@app.route('/predict_negative_comments', methods=['POST'])
def predict_negative_comments():
    """Predict negative comments from the uploaded CSV file."""
    try:
        translated_comments_path = os.path.join(os.getcwd(), 'translated_comments.csv')
        negative_comments_path = os.path.join(os.getcwd(), 'negative_comments.csv')

        if not os.path.exists(translated_comments_path):
            return jsonify({'error': 'Translated comments file not found.'}), 400

        negative_comments = []

        with open(translated_comments_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                username, comment = row
                sentiment = predict_custom_input(model, tokenizer, comment, max_length)
                if sentiment == "Negative":
                    negative_comments.append((username, comment))

        with open(negative_comments_path, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Comment'])
            writer.writerows(negative_comments)

        return jsonify({'message': 'Prediction of negative comments completed and saved to negative_comments.csv.'})

    except Exception as e:
        print(f"Error predicting negative comments: {e}")
        return jsonify({'error': 'An error occurred while predicting negative comments.'}), 500

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error running Flask app: {e}")








# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import preprocessing
# from flask import Flask, request, jsonify
# import os
# import pickle




# app = Flask(__name__)

# # Load the model
# try:
#     model = keras.models.load_model('model.h5', compile=False)
# except Exception as e:
#     print(f"Error loading model: {e}")

# # Load the tokenizer
# try:
#     with open('tokenizer.pkl', 'rb') as f:
#         tokenizer = pickle.load(f)
# except Exception as e:
#     print(f"Error loading tokenizer: {e}")

# max_length = 100  # Update this according to your model's requirement

# # Preprocessing function
# def preprocess(text):
#     # Add your preprocessing steps here
#     return text.lower()

# def predict_custom_input(model, tokenizer, input_text, max_length):
#     cleaned_text = preprocess(input_text)
#     sequence = tokenizer.texts_to_sequences([cleaned_text])
#     padded_sequence = pad_sequences(sequence, maxlen=max_length)
#     prediction = model.predict(padded_sequence)[0][0]
#     sentiment = "Positive" if prediction >= 0.5 else "Negative"
#     return sentiment

# @app.route('/upload', methods=['POST'])
# def upload():
#     try:
#         if 'file' not in request.files:
#             return jsonify({'error': 'No file part in the request.'}), 400

#         file = request.files['file']

#         if file.filename == '':
#             return jsonify({'error': 'No selected file.'}), 400

#         file_path = os.path.join(os.getcwd(), 'translated_comments.csv')
#         file.save(file_path)

#         return jsonify({'message': 'File uploaded successfully.'})

#     except Exception as e:
#         print(f"Error uploading file: {e}")
#         return jsonify({'error': 'An error occurred while uploading the file.'}), 500

# @app.route('/predict_negative_comments', methods=['GET'])
# def predict_negative_comments():
#     try:
#         translated_comments_path = os.path.join(os.getcwd(), 'translated_comments.csv')
#         # Implement the logic to read the translated comments, predict sentiments, and save negative comments to negative_comments.csv
#         return jsonify({'message': 'Prediction of negative comments completed and saved to negative_comments.csv.'})

#     except Exception as e:
#         print(f"Error predicting negative comments: {e}")
#         return jsonify({'error': 'An error occurred while predicting negative comments.'}), 500

# if __name__ == '__main__':
#     try:
#         app.run(debug=False, host='0.0.0.0')
#     except Exception as e:
#         print(f"Error running Flask app: {e}")


