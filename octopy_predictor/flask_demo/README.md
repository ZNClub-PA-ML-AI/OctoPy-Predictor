# SET UP

# REQUIRED PACKAGES
- Flask

# RUN SERVER

- Windows Server
1. set FLASK_APP=absolute_filepath_with_filename
- OR
- Linux Server
1. export FLASK_APP=absolute_filepath_with_filename
2. flask run
- OR
2. python -m flask run

# DEBUG MODE

- set FLASK_DEBUG=1
- OR
- export FLASK_DEBUG=1

# QUICKIES

- set FLASK_DEBUG=1
- set FLASK_APP=C:\Users\Augus\dev\Projects\OctoPy-Predictor\octopy_predictor\flask_demo\app.py


# LEARNINGS
- DEBUG=1 uses live_reload and has error stack trace displayed directly on web page
- Cannot return Objects, only string