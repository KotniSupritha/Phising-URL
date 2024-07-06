from flask import Flask, request, render_template
import pickle

# Load the model
with open('phishing.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    
    # Assuming your model's predict method takes a list of URLs
    prediction = model.predict([url])[0]
    
    # Convert the prediction to a human-readable form
    result = "Phishing" if prediction == 1 else "Not Phishing"
    
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
