import dash
from dash_core_components.Markdown import Markdown
from plotly.express import colors
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from joblib import load
from app import app
import numpy as np

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions'), 
        dcc.Markdown('#### Monthly Visits'), 
        dcc.Dropdown(
            id='CoffeeHouse', 
            options = [
                {'label': 'Less Than 1', 'value': 'less1'}, 
                {'label': '1 to 3', 'value': '1~3'}, 
                {'label': 'Never', 'value': 'never'}, 
                {'label': '4 to 8', 'value': '4~8'}, 
                {'label': 'More Than 8', 'value': 'gt8'}, 
            ], 
            value = 'never', 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Coupon Expiration'), 
        dcc.Dropdown(
            id='expiration', 
            options = [
                {'label': '2 Hours', 'value': '2h'}, 
                {'label': '1 Day', 'value': '1d'}, 
            ], 
            value = '2h', 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Time of Day'), 
        dcc.Dropdown(
            id='time', 
            options = [
                {'label': '7 AM', 'value': '7AM'}, 
                {'label': '10 AM', 'value': '10AM'}, 
                {'label': '2 PM', 'value': '2PM'}, 
                {'label': '6 PM', 'value': '6PM'}, 
                {'label': '10 PM', 'value': '10PM'}, 
            ], 
            value = '2PM', 
            className='mb-5',
        ),
        dcc.Markdown('#### Trip Destination'), 
        dcc.Dropdown(
            id='destination', 
            options = [
                {'label': 'Home', 'value': 'Home'}, 
                {'label': 'Work', 'value': 'Work'},
                {'label': 'Non-Urgent', 'value': 'No Urgent Place'} 
            ], 
            value = 'Home', 
            className='mb-5', 
        ),   
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('##   ', className='mb-5'),
        dcc.Markdown('#### Income', ), 
        dcc.Dropdown(
            id='income', 
            options = [
                {'label': '$12500 - $24999', 'value': '$12500 - $24999'}, 
                {'label': '$25000 - $37499', 'value': '$25000 - $37499'},
                {'label': '$37500 - $49999', 'value': '$37500 - $49999'}, 
                {'label': '$50000 - $62499', 'value': '$50000 - $62499'}, 
                {'label': '$62500 - $74999', 'value': '$62500 - $74999'}, 
                {'label': '$75000 - $87499', 'value': '$75000 - $87499'}, 
                {'label': '$87500 - $99999', 'value': '$87500 - $99999'},
                {'label': '$100000 or More', 'value': '$100000 or More'},
            ], 
            value = '$50000 - $62499', 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Occupation'), 
        dcc.Dropdown(
            id='occupation', 
            options = [
                {'label': 'Unemployed', 'value': 'Unemployed'}, 
                {'label': 'Student', 'value': 'Student'},
                {'label': 'IT/Mathematical', 'value': 'Computer & Mathematical'}, 
                {'label': 'Sales Related', 'value': 'Sales & Related'}, 
                {'label': 'Management', 'value': 'Management'}, 
                {'label': 'Education/Training/Library', 'value': 'Education&Training&Library'}, 
                {'label': 'Arts/Entertainment/Media', 'value': 'Arts Design Entertainment Sports & Media'},
                {'label': 'Office & Administrative Support', 'value': 'Office & Administrative Support'},
                {'label': 'Retired', 'value': 'Retired'},
                {'label': 'Business & Financial', 'value': 'Business & Financial'},
                {'label': 'Food Preparation/Serving Related', 'value': 'Food Preparation & Serving Related'},
                {'label': 'Transportation/Material Moving', 'value': 'Transportation & Material Moving'},
                {'label': 'Community/Social Services', 'value': 'Community & Social Services'},
                {'label': 'Healthcare Practitioners & Technical', 'value': 'Healthcare Practitioners & Technical'},
                {'label': 'Legal', 'value': 'Legal'},
                {'label': 'Healthcare Support', 'value': 'Healthcare Support'},
                {'label': 'Architecture & Engineering', 'value': 'Architecture & Engineering'},
                {'label': 'Life Physical Social Science', 'value': 'Life Physical Social Science'},
                {'label': 'Protective Service', 'value': 'Protective Service'},
                {'label': 'Personal Care & Service', 'value': 'Personal Care & Service'},
                {'label': 'Construction & Extraction', 'value': 'Construction & Extraction'},
                {'label': 'Installation Maintenance/Repair', 'value': 'Installation Maintenance & Repair'},
                {'label': 'Production Occupations', 'value': 'Production Occupations'},
                {'label': 'Building/Grounds Cleaning/Maintenance', 'value': 'Building & Grounds Cleaning & Maintenance'},
                {'label': 'Farming/Fishing/Forestry', 'value': 'Farming Fishing & Forestry'},

            ], 
            value = 'Unemployed', 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Age'), 
        dcc.Dropdown(
            id='age', 
            options = [
                {'label': 'Under 21', 'value': 'below21'}, 
                {'label': '21', 'value': '21'},
                {'label': '26', 'value': '26'}, 
                {'label': '31', 'value': '31'}, 
                {'label': '36', 'value': '36'}, 
                {'label': '41', 'value': '41'}, 
                {'label': '46', 'value': '46'},
                {'label': '50 or Older', 'value': '50plus'},
            ], 
            value = '21', 
            className='mb-5', 
        ),
        dcc.Markdown('#### Education'), 
        dcc.Dropdown(
            id='education', 
            options = [
                {'label': 'Some High School', 'value': 'Some High School'}, 
                {'label': 'High School Graduate', 'value': 'High School Graduate'},
                {'label': 'Some College - No Degree', 'value': 'Some college - no degree'}, 
                {'label': 'Associates Degree', 'value': 'Associates degree'}, 
                {'label': 'Bachelors Degree', 'value': 'Bachelors degree'}, 
                {'label': 'Graduate Degree (Masters/Doctorate)', 'value': 'Graduate degree (Masters or Doctorate)'}, 
            ], 
            value = 'Some High School', 
            className='mb-5', 
        ),         
    ]
)

column3 = dbc.Col(
    [

    dcc.Graph(id="pie-chart"),

    ]
)

layout = dbc.Row([column1, column2, column3])

@app.callback(
    Output("pie-chart", "figure"), 
    [Input("CoffeeHouse", "value"),
     Input("destination", "value"),
     Input("occupation", "value"),
     Input("income", "value"),
     Input("age", "value"),
     Input("education", "value"), 
     Input("expiration", "value"),
     Input("time", "value"),])
def predict(CoffeeHouse, destination, occupation, income, age, education, expiration, time):
    df = pd.DataFrame(
        columns=['CoffeeHouse', 'destination', 'occupation', 'income','age', 'education','expiration', 'time'], 
        data=[[CoffeeHouse, destination, occupation, income, age, education, expiration, time]]
    )
    pipeline = load('assets/Coupons.joblib')
    y_pred = pipeline.predict_proba(df)[0]*100
    formatd = np.round(y_pred, decimals = 2)
    data = {'one':formatd[0],
            'two':formatd[1]}
    df2 = pd.DataFrame(data = formatd, columns = ['one'])
    fig = px.pie(df2, values= df2['one'], names=['Reject', 'Accept'], color_discrete_sequence=px.colors.sequential.RdBu)
    return fig