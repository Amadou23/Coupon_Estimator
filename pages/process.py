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
        
        ## Process

        To start, I had read in the relevant csv file and stored it into a Pandas dataframe object. This particular dataframe
        initially had 26 attributes or "features" and a total of 12,684 rows. After establishing the dataframe, I needed
        to wrangle it, such that it would be formatted reasonably for modeling and exploratory analysis. Because I was 
        only working with the section of the dataframe that contained 'coupon' values equal to "CoffeeHouse", the rows values
        were cut down to 3,996. Afterwards, I had incorporated methods to remove unrelated columns, and also ones  like
        'toCoupon_GEQ5min' that had high cardinality.
            """
        ),
            html.Img(src='assets/wrangle_df.png', className='img-fluid', style={'height':'12%'}),
        dcc.Markdown(
            """
        
        After this was accomplished, I designated our feature matrix used for prediction to the variable "X" and
        our target vector to the variably "y". After doing so, I had used a train_test_split method from the scikit-learn
        library to split our data into training and testing data. Next, I established a baseline score, as a 
        reference point for model evaluation. It so turns out that our classes are almost completely balanced,
        not just within our training data, but the entire dataframe. This means that the accuracy score metric is 
        highly relevant in assessing our model's capabilities.
            """
        ),
        html.Img(src='assets/data_split.png', className='img-fluid', style={'height':'12%'}),
        html.Img(src='assets/baseline2.png', className='img-fluid', style={'height':'12%'}),
        dcc.Markdown(
            """
        
        

        Now we're ready to start fitting our models! I had started with a pipeline incorporating an sklearn 
        RandomForestClassifier() estimator. The model also had an OrdinalEncoder() for categorical features 
        (which were the vast majority) and SimpleImputer() (for NaN values). Next, I had fit a pipeline with an 
        XGBoost() estimator. Upon extensively tuning the hyperparameters of both models, I had discovered that the 
        random forest had done surprisingly better:
            """
        ),
        html.Img(src='assets/rf_pipe.png', className='img-fluid', style={'height':'12%'}),
        html.Img(src='assets/acc_score.png', className='img-fluid', style={'height':'12%'}),
        dcc.Markdown(
            """
        
        At this point, after having chosen the proper model and judged it to sufficiently be better than my 
        baseline after tuning, I needed to see exactly how the features were influencing estimations. As portrayed
        in the "Insights" section of this app, I had ranked features by their permutation importances and feature 
        importances. Doing this would allow me to identify the categories that should be paid attention to during
        marketing, giving this project use-value. 
            """
        ),
        html.Img(src='assets/joblib2.png', className='img-fluid', style={'height':'5%'}),
        dcc.Markdown(
            """
        
        This was the final step necessary to deploy the model to the webapp. As a 'joblib' file, the model is now
        capable of taking inputs given in the "Predictions" section and producing an estimation.
            """
        ),

    ],
)

layout = dbc.Row([column1])