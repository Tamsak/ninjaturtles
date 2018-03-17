from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html') 

@app.route('/ninja')
def all():
  return render_template('ninjas.html')

@app.route('/ninja/<color>')
def ninja(color):
  if color=='blue':
    filename = 'leonardo.jpg'
  elif color == 'purple':
    filename = 'donatello.jpg'
  elif color == 'orange':
    filename = 'michelangelo.jpg'
  elif color == 'red':
    filename = 'raphael.jpg'
  else:
    filename = 'notapril.jpg'
  return render_template('ninja.html', color=filename)
  
app.run(debug=True)