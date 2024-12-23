import zipfile
import os

# Creating a folder to store the files
folder_name = '/mnt/data/flask_keylogger_project'
os.makedirs(folder_name, exist_ok=True)

# Content for app.py
app_py_content = '''from flask import Flask, request

app = Flask(__name__)

# হোমপেজে একটি ফর্ম দেখাবে
@app.route('/')
def home():
    return '''
    <form action="/log" method="post">
        Enter something: <input type="text" name="data">
        <button type="submit">Submit</button>
    </form>
    '''

# ডেটা গ্রহণ ও সংরক্ষণ
@app.route('/log', methods=['POST'])
def log_data():
    data = request.form['data']
    with open('log.txt', 'a') as file:
        file.write(data + '\\n')
    return "Data logged! Thank you."

if __name__ == '__main__':
    app.run(debug=True)
'''

# Content for requirements.txt
requirements_txt_content = '''Flask==2.3.2
'''

# Content for .gitignore
gitignore_content = '''log.txt
'''

# Create the files in the folder
with open(os.path.join(folder_name, 'app.py'), 'w') as file:
    file.write(app_py_content)

with open(os.path.join(folder_name, 'requirements.txt'), 'w') as file:
    file.write(requirements_txt_content)

with open(os.path.join(folder_name, '.gitignore'), 'w') as file:
    file.write(gitignore_content)

# Create a zip file of the folder
zip_filename = '/mnt/data/flask_keylogger_project.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_name))

zip_filename
