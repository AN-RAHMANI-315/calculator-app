"""
Flask Web Application for Calculator.
"""

from flask import Flask, render_template, request, jsonify, session
from calculator import Calculator
import os


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')


def get_calculator():
    """Get calculator instance from session."""
    if 'calculator_history' not in session:
        session['calculator_history'] = []
    
    calc = Calculator()
    calc.history = session['calculator_history']
    return calc


def save_calculator(calc):
    """Save calculator history to session."""
    session['calculator_history'] = calc.history
    session.modified = True


@app.route('/')
def index():
    """Main calculator page."""
    return render_template('index.html')


@app.route('/api/calculate', methods=['POST'])
def calculate():
    """API endpoint for calculations."""
    try:
        data = request.get_json()
        operation = data.get('operation')
        a = data.get('a')
        b = data.get('b')
        
        calc = get_calculator()
        
        if operation == 'add':
            result = calc.add(float(a), float(b))
        elif operation == 'subtract':
            result = calc.subtract(float(a), float(b))
        elif operation == 'multiply':
            result = calc.multiply(float(a), float(b))
        elif operation == 'divide':
            result = calc.divide(float(a), float(b))
        elif operation == 'power':
            result = calc.power(float(a), float(b))
        elif operation == 'modulo':
            result = calc.modulo(float(a), float(b))
        elif operation == 'percentage':
            result = calc.percentage(float(a), float(b))
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        save_calculator(calc)
        
        return jsonify({
            'result': result,
            'history': calc.get_history()[-5:]  # Last 5 operations
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Calculation error'}), 500


@app.route('/api/calculate-single', methods=['POST'])
def calculate_single():
    """API endpoint for single-value calculations."""
    try:
        data = request.get_json()
        operation = data.get('operation')
        value = data.get('value')
        
        calc = get_calculator()
        
        if operation == 'sqrt':
            result = calc.square_root(float(value))
        elif operation == 'factorial':
            result = calc.factorial(int(value))
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        save_calculator(calc)
        
        return jsonify({
            'result': result,
            'history': calc.get_history()[-5:]
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Calculation error'}), 500


@app.route('/api/history')
def get_history():
    """Get calculation history."""
    calc = get_calculator()
    return jsonify({'history': calc.get_history()})


@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    """Clear calculation history."""
    calc = get_calculator()
    calc.clear_history()
    save_calculator(calc)
    return jsonify({'message': 'History cleared'})


@app.route('/health')
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({
        'status': 'healthy',
        'service': 'calculator-app',
        'version': '1.0.0'
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
