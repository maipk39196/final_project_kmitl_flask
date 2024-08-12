from flask import Flask, render_template

app = Flask(__name__)

@app.route('/appitizer')
def appitizer():
    return render_template('main.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/dessert')
def dessert():
    return render_template('main.html')

@app.route('/beverage')
def beverage():
    return render_template('main.html')

@app.route('/kitchen_main')
def kitchen_main():
    return render_template('kitchen_main.html')

@app.route('/kitchen_stock_main')
def kitchen_stock_main():
    return render_template('kitchen_stock.html')

@app.route('/kitchen_stock_reserve')
def kitchen_stock_reserve():
    return render_template('kitchen_stock.html')

@app.route('/stock_edit')
def stock_edit():
    return render_template('stock_edit.html')

@app.route('/kitchen_report')
def kitchen_report():
    return render_template('kitchen_report.html')

@app.route('/kitchen_mistake')
def kitchen_mistake():
    return render_template('kitchen_report.html')

@app.route('/recipes_apptizer')
def recipes_apptizer():
    return render_template('kitchen_recipes_main.html')

@app.route('/recipes_main')
def recipes_main():
    return render_template('kitchen_recipes_main.html')

@app.route('/recipes_dessert')
def recipes_dessert():
    return render_template('kitchen_recipes_main.html')

@app.route('/recipes_beverage')
def recipes_beverage():
    return render_template('kitchen_recipes_main.html')

@app.route('/recipe')
def recipe():
    return render_template('view_recipe.html')

if __name__ == '__main__':
    app.run(debug=True)