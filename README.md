<pre>


                    ___                                      
                   (   )                                     
  .--.     .--.     | |_       .--.        .-..    ___  ___  
 /    \   /    \   (   __)    /    \      /    \  (   )(   ) 
|  .-. ; |  .-. ;   | |      |  .-. ;    ' .-,  ;  | |  | |  
| |  | | |  |(___)  | | ___  | |  | |    | |  . |  | |  | |  
| |  | | |  |       | |(   ) | |  | |    | |  | |  | '  | |  
| |  | | |  | ___   | | | |  | |  | |    | |  | |  '  `-' |  
| '  | | |  '(   )  | ' | |  | '  | |    | |  ' |   `.__. |  
'  `-' / '  `-' |   ' `-' ;  '  `-' /    | `-'  '   ___ | |  
 `.__.'   `.__,'     `.__.    `.__.'     | \__.'   (   )' |  
                                         | |        ; `-' '  
                                        (___)        .__.'   


</pre>

Generic platform for Prediction using basic machine learning models

## Index

- Structure
- Components
- Architecture
- Technology Stack
- Setup
- Input File Constraints
- Algorithms supported

## Structure


- data: All data to be stored/ loaded
- demo
    - bokeh_demo: Visualizer Component Demo - to be moved out
    - flask_demo: WebInterface Demo - to be moved out
- src: All working component files
- tests

## Components

## Architecture
![Proposed Architecture][logo]


## Setup

## Input File Constraints

## Algorithms supported
- Support Vector Machine

## TODO
- NameError: name 'fetch_all_features' is not defined :: currently converted to self.method_name(). Need to learn about static methods in Python Class	
- Give options as REGRESSION / CLASSIFICATION. Else regression data fails for classification model

[logo]: https://raw.githubusercontent.com/ZNClub-PA-ML-AI/OctoPy-Predictor/master/Octo-Py.png

## SETUP/ CONFIGURATIONS

### GENERAL
#### Setup path variables
- Windows : double check to make sure you see python in your PATH. You can find your path by opening your control panel -> System and Security -> System -> Advanced System Settings -> Environment Variables -> Selecting Path -> Edit ->


#### Find programs running on port number
- netstat -a -o -n | findstr port_number

#### Kill task using PID
- taskkill /F /PID 6136

### FLASK
- python app.py


