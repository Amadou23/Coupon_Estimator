# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            
            A major power that machine learning provides us, is the ability to consume large
            quantities of information, and derive models that can guide us towards a proper desired usage of that information.
            The dataset I've used for this project can be found at: http://archive.ics.uci.edu/ml/datasets/in-vehicle+coupon+recommendation.
            The dataframe constructed contains 22 features, and the target variable "Y", which contains binary values
            indicating whether a coupon offer was accepted (1), or rejected (0).

            You may have noticed that this project deals with coffee house coupons in particular, that is because there were
            three other coupon values: 'Carry out & Take away', 'Bar' and 'Restaurant($20-$50)' that I had omitted for the 
            sake of regularizing our target feature to one class variety.

            We must build a model that will estimate our target as accurately as possible. Since this is a classification
            problem, we will build a pipeline with a classifier estimator. As will be explained in the 'Process' section,
            I had opted to fit a random forest classifier, as it had yielded a higher accuracy score than the
            XGBoost model. 

            Since the data was assembled through a survey, the features are each essentially questions, which
            offer insight into how we can categorize our participants. The goal from this point onward,
            is to use our model to determine which questions correspond to a higher likelihood of positive response to the
            coupon offers given particular answers and as a result, potential sales incentives:
             """
        ),
        html.Img(src='assets/Permutation_importance.png', className='img-fluid'),
        dcc.Markdown(
            """
        
            Permutation importance ranks features by how drastically the model's accuracy changes after each feature's set of
            values is corrupted (shuffled). Feature importance is a more straight-forward ranking based on how the model is
            initially fit. Our "CoffeeHouse" feature clearly has the highest predictive power when ranking feature importances 
            through either method. This can be observed through the interractive portion of this app--try changing the corresponding
            dropbar value ('Monthly Visits') from 'Never' to '1 to 8'. Regardless of how you set your other feature values,
            a significant shift in estimation is likely to occur. 

            I wouldn't call this data leakage, however, since its pull-dominance isn't overbearing and it isn't directly
            explaining variance in our target variable. I had weighted permutation importance more seriously, only after testing
            both sets of features and discovering that the model's accuracy score was compromised more so through using only
            the 'feature importances'. I also reduced the interractive model to 8 features (from 20 post-wrangling), for the sake of space efficiency,
            and after determining that the model's accuracy was compromised by only about 3%.
            
            
             """
        ),

        html.Img(src='assets/shapely2.png', className='img-fluid'),
        html.Img(src='assets/shapely.png', className='img-fluid'),
        dcc.Markdown(
            """
        
            Above, I've included a few Shapely force plots, which detail the individual impact each of our features had on a 
            estimation made for a particular instance. We can observe a similar trend here, in which features like
            "CoffeeHouse" and "estimation" push our estimation strongly to a "rejection" decision. 
            
            Overall, a clear takeaway would be that the expiration of our coupons and whether or not the customer
            already frequents the coffee house are by far the most impactful features. This makes sense, as a consumer
            that already places value in a product, will likely be more opportunistic when it comes to discounts. However, the
            expiration date being extended from 2 hours to a full day likely ensured more consumers were able to utilize it.
            If I were trying to incentivize sales through deploying coupons, I would initially make sure the window of time
            the potential customer would have to use them would be substantial. The driving destination also played a seemingly 
            huge part in orienting our pie chart. I would experiment with making offers to consumers at particular
            times of day, in order to find a window which should be utilized more aggressively.
             """
        ),

    ],
)

layout = dbc.Row([column1])