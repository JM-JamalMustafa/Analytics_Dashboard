# Flask Analytics Dashboard API

## Overview

This project is a Flask-based API designed to serve analytics data for a dashboard. It processes login and check-in/check-out data, calculates leave statistics by department, and aggregates login frequency by day of the week. The API can be easily connected to a front-end application for real-time data visualization.

## Features

- **Check-ins and Check-outs**: Provides real-time check-in and check-out statistics aggregated by hour.
- **Department Leave Counts**: Returns the total number of leave days taken by each department.
- **Login Frequency**: Aggregates and displays the frequency of logins per day of the week.
- **Front-End Integration**: Serves an HTML page to visualize data through JavaScript libraries (e.g., Plotly).

## Technology Stack

- **Backend**: Flask
- **Data Processing**: Pandas
- **Frontend**: HTML, JavaScript (with Plotly for visualizations)
- **Database**: MongoDB (not included in the project, but implied)

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JM-JamalMustafa/Analytics_Dashboard.git
   cd Analytics_Dashboard
