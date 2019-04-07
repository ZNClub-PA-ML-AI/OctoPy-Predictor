# OctoPy-Predictor

<pre>
      o__ __o                 o                        o__ __o               
     /v     v\               <|>                      <|     v\              
    />       <\              < >                      / \     <\             
  o/           \o     __o__   |        o__ __o        \o/     o/   o      o  
 <|             |>   />  \    o__/_   /v     v\        |__  _<|/  <|>    <|> 
  \\           //  o/         |      />       <\       |          < >    < > 
    \         /   <|          |      \         /      <o>          \o    o/  
     o       o     \\         o       o       o        |            v\  /v   
     <\__ __/>      _\o__</   <\__    <\__ __/>       / \            <\/>    
                                                                      /      
                                                                     o       
                                                                  __/>       
                                                                  
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

- bokeh_demo: Visualizer Component Demo - to be moved out
- data: All data to be stored/ loaded
- flask_demo: WebInterface Demo - to be moved out
- main: All working component files

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

[logo]: https://raw.githubusercontent.com/ZNevzz/ZNevzz.github.io/master/Octo-Py.png


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


