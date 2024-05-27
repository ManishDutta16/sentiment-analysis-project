# from flask import Flask, render_template
# app = Flask(__name__)


# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template('index.html')

# @app.route("/about")
# def about():
#     return render_template('about.html')

# @app.route("/features")
# def features():
#     return render_template('features.html')

# @app.route("/show")
# def show():
#     return render_template('show.html')

# @app.route("/form")
# def form():
#     return render_template('form.html')

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for
import pandas as pd 
import chardet

app = Flask(__name__)

from function.scrapfyt_module import scrapfyt



# `read-form` endpoint  
@app.route('/read-form', methods=['POST']) 
def read_form(): 
  
    # Get the form data as Python ImmutableDict datatype  
    data = request.form 

    url = data['video_link']
    scrapfyt(url)
    
    # Return the extracted information  
    # return { 
    #     'link'     : data['video_link'], 
    # } 

    return redirect(url_for('table'))

@app.route('/table') 
def table(): 

    # df = pd.read_csv('translated_comments.csv') 
    # df.to_csv('translated_comments.csv', index=None)   
    # data = pd.read_csv('translated_comments.csv') 
    # return render_template('table.html', tables=[data.to_html()], titles=['']) 
    def detect_encoding(file_path):
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
            return result['encoding']

    csv_file_path = 'translated_comments.csv'
    encoding = detect_encoding(csv_file_path)
    df = pd.read_csv(csv_file_path, encoding=encoding)
    return render_template('table.html', tables=[df.to_html()], titles=[''])


# @app.route('/table')
# def table():
    
#     try:
#         df = pd.read_csv('translated_comments.csv', encoding='utf-8')
#     except UnicodeDecodeError:
#         df = pd.read_csv('translated_comments.csv', encoding='ISO-8859-1')
#     df.to_csv('translated_comments.csv', index=None)
#     data = pd.read_csv('translated_comments.csv')
#     return render_template('table.html', tables=[data.to_html()], titles=[''])


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/features")
def features():
    return render_template('features.html')

@app.route("/show")
def show():
    return render_template('show.html')

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/handle_youtube_options", methods=["POST"])
def handle_youtube_options():
    choice = request.form.get('choice')
    video_link = request.form.get('video_link')

    # Process the form data based on the user's choice
    if choice == '1':
        # Code to download comments
        print(f"Downloading comments for video: {video_link}")
    elif choice == '2':
        # Code to download translated comments
        print(f"Downloading translated comments for video: {video_link}")
    elif choice == '3':
        # Code to review positive/negative comments
        print(f"Reviewing positive/negative comments for video: {video_link}")
    else:
        # Handle invalid choice
        print("Invalid choice selected")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

