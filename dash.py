from flask import Flask, jsonify, send_from_directory
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

# Mock data
mock_logins = [
    {"loginAt": datetime.now() - timedelta(hours=1), "isCompleted": False, "department": "HR", "leave_days": 2},
    {"loginAt": datetime.now() - timedelta(hours=2), "isCompleted": True, "department": "HR", "leave_days": 2},
    {"loginAt": datetime.now() - timedelta(hours=3), "isCompleted": False, "department": "IT", "leave_days": 1},
    {"loginAt": datetime.now() - timedelta(hours=4), "isCompleted": True, "department": "IT", "leave_days": 1},
    {"loginAt": datetime.now() - timedelta(days=1, hours=1), "isCompleted": False, "department": "Finance", "leave_days": 3},
    {"loginAt": datetime.now() - timedelta(days=1, hours=2), "isCompleted": True, "department": "Finance", "leave_days": 3},
    # Add more entries as needed for testing and also use  your data base when run on realtime projects
]

@app.route('/api/analytics/today', methods=['GET'])
def get_today_analytics():
    """API endpoint to retrieve today's analytics data."""
    today = datetime.now().date()

    # Convert mock data to DataFrame
    df = pd.DataFrame(mock_logins)

    # Convert 'loginAt' to datetime
    df['loginAt'] = pd.to_datetime(df['loginAt'])

    # Filter for today's logins
    df_today = df[df['loginAt'].dt.date == today]

    # Extract hour of day
    df_today['hour'] = df_today['loginAt'].dt.hour

    # Separate check-ins and check-outs
    check_ins_by_hour = df_today[df_today['isCompleted'] == False]['hour'].value_counts().sort_index()
    check_outs_by_hour = df_today[df_today['isCompleted'] == True]['hour'].value_counts().sort_index()

    # Return check-in and check-out counts
    return jsonify({
        'check_ins': check_ins_by_hour.to_dict(),
        'check_outs': check_outs_by_hour.to_dict(),
    })

@app.route('/api/analytics/department-leave', methods=['GET'])
def get_department_leave_counts():
    """API endpoint to retrieve leave counts by department."""
    df = pd.DataFrame(mock_logins)

    # Group by department and sum leave days
    leave_counts = df.groupby('department')['leave_days'].sum().reset_index()
    leave_counts_dict = {row['department']: row['leave_days'] for index, row in leave_counts.iterrows()}

    return jsonify(leave_counts_dict)


@app.route('/api/analytics/login-frequency', methods=['GET'])
def get_login_frequency():
    """API endpoint to retrieve login frequency by day of the week."""
    df = pd.DataFrame(mock_logins)

    # Convert 'loginAt' to datetime
    df['loginAt'] = pd.to_datetime(df['loginAt'])

    # Extract day of the week
    df['day_of_week'] = df['loginAt'].dt.day_name()

    # Count logins per day of the week
    login_by_day = df['day_of_week'].value_counts()

    return jsonify(login_by_day.to_dict())

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
