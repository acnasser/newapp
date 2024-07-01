from flask import Flask, render_template, request, redirect, url_for
from user import User

app = Flask(__name__, template_folder='templates')

# Dummy data store
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    errors = {}
    
    if request.method == 'POST':
        user_name_field = request.form['user_name']
        first_name_field = request.form['first_name']
        last_name_field = request.form['last_name']
        phone_number_field = request.form['phone_number']
        user_email_field = request.form['user_email']
        user_dob_field = request.form['user_dob']
        
        # Create an instance of User
        user_instance = User(
            user_name=user_name_field,
            phone_number=phone_number_field,
            user_email=user_email_field,
            first_name=first_name_field,
            last_name=last_name_field,
            user_dob=user_dob_field
        )
        
        # Validate the user input
        validation_passed, validation_errors = user_instance.input_err_av()
        
        if validation_passed:
            # Store user data (for demonstration, you can save to database or file)
            users.append(user_instance)
            return redirect(url_for('index'))
        else:
            # Collect errors into a dictionary for easier display
            errors = {key: value for key, value in validation_errors.items() if value}

    # Ensure 'errors' is defined even if there are no errors
    if 'errors' not in locals():
        errors = {}

    return render_template('create_account.html', errors=errors)

if __name__ == '__main__':
    app.run(debug=True)
