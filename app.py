from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Template
template = """
<!doctype html>
<title>Sum Calculator</title>
<h1>Enter Two Numbers to Add</h1>
<form method="POST">
    First Number: <input type="number" name="num1"><br><br>
    Second Number: <input type="number" name="num2"><br><br>
    <input type="submit" value="Calculate">
</form>
{% if result is not none %}
    <h2>The sum is: {{ result }}</h2>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        # Store result in a text file
        with open('results.txt', 'a') as f:
            f.write(f"{num1} + {num2} = {result}\n")
    return render_template_string(template, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
