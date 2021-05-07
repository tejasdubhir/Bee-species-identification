from flask import Flask, render_template, request, Markup, url_for
from bees import find_ranks

app = Flask(__name__)

html_file = 'index.html'

@app.route('/')
def main():
    return render_template(html_file)

@app.route('/search', methods=['POST','GET'])
def send(sum=sum):  
    res = 'Please Enter a Valid Query'  
    if request.method == 'GET':
        return render_template(html_file, sum=res)

    if request.method == 'POST':       
        query = request.form['query']    
        if not query:
            return render_template(html_file, sum=res)    
        sum = find_ranks(query)   
        res = "" 
        for i in range(len(sum)):
            res += Markup(str(i+1) + str('. ')+ str(sum[i]) + '<br>')    
        return render_template(html_file, sum=res)