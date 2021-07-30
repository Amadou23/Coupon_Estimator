# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictive Marketing Power


           One of the big questions within retail, is how to use resources to communicate with a proper target demographic
           as efficiently and effectively as possible. This is often a trial and error process, involving a wide variety of
           marketing tactics and feedback analysis. Hosting discount events, or offering reduced pricing
           in the form of coupons, has the ability to draw an audience that exceeds a regular consumer-base.
           This can be seen on Black Friday, where near store-wide discounts can incur levels of traffic
           that may even appear chaotic in certain scenarios. 

           But apart from the discount seasons, how exactly would a producer be able to consistently approach
           potential customers, and turn them into regular shoppers? Through predictive modeling!
           By looking at the response rates to discounts offered through coupons, it is possible to market
           towards particular demographics more aggressively, driving sales. Although discounts offer items at
           abnormal pricing, thriving businesses can use them to pique the interests of future buyers. Perhaps
           it's discovered through an event, that demographic features pertaining to age-group, occupation, 
           or even the time of day the discount is offered, behave as strong predictive elements for successful sales.
           This model uses data from a coupon-based survey offered on Amazon Mechanical Turk to predict
           whether participants would accept, or reject a coupon offering coffee house discounts while driving. 

            """
        ),
        dcc.Link(dbc.Button('Let\'s Get Started!', color='primary'), href='/predictions')
    ],
    md=4,
)

#gapminder = px.data.gapminder()
#fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           #hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        html.Img(src='assets/board.jpg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2  ])