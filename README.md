# Coupon Estimator

Link to project: https://couponestimator.herokuapp.com/
UCI Dataset: https://archive.ics.uci.edu/ml/datasets/in-vehicle+coupon+recommendation
## ==Description==:

'Coupon Estimator' is an interactive web app deployed on the Heroku platform, using the Plotly-Dash framework.
It attempts to explore the some of the various use-cases that machine learning provides to the world
of marketing. Through predictive modeling, we can extract feature importances among other things, 
making it possible to highlight various demographic combinations that are more responsive to our 
marketing tactics. The goal driving this project, was to offer insight into the robust properties
of machine learning and how 'predictions' can create incentives that improve metrics.

The data that is being utilized has been derived from the UCI Machine Learning Repository, and is
based off of a survey hosted on Amazon Mechanical Turk that offers coupons to various restaurants
after asking certain demographic questions. To trim bias, a particular type of restaurant, the 
coffee houses, were used only. A model pipeline using a random forest and various data transformers
had been utilized to classify whether a participant would reject, or accept a coupon based off of
the demographic information they had entered.

The interactive portion of the app can be observed on the "Predictions" tab, where a pi chart is displaying
the probability predictions of our model in real-time, being fed user-selected values. Only 8 features
had been chosen, based off of how impactful they were for our model's predictive capabilities (feature importances).
The majority class will always be represented by the darker shade of red.
