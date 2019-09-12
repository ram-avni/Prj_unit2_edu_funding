# Prj_unit2_edu_funding
Using Multiple Linear Regression to Analyze the Impact of Funding on U.S. Graduation Rates

Xristos Katsaros and Ram Avni



# **Overview**

The purpose of this project was to use a linear regression model in order to predict U.S. high school graduation rates. Obviously, there are many factors and vast data, and initially we wanted to focus on school performance across all states. However, different states have different mandatory exams and evaluation matrices, so we chose a data set with high school graduation rates, in order to measure and compare all states on a uniform scale. Initially ,our independent variables were types of funding (federal, local, etc.) and types of expenditure (instructional, administrative, etc.). Thus, we aimed at deriving a model that can show correlation between amount / type of funding and school performance, measured by graduation rates, for all 50 states.



# **EDA and Feature Engineering**

* We used the following data sets:
* Kaggale - U.S. Education Datasets: Unification Project:
 * https://www.kaggle.com/noriuk/us-education-datasets-unification-project/version/5
* City-Data.com - Cost of living by U.S. state (2015):
 * http://www.city-data.com/forum/city-vs-city/2582388-cost-living-u-s-state-2015-a.html#ixzz5xMemrtzn
* High School Graduation Rates by State:
 * https://www.governing.com/gov-data/high-school-graduation-rates-by-state.html


We combined the raw data sets to cover 5o states for a period of 5 years, 2010-2015. As mentioned above, math and English scores were missing from many states, so we eliminated those columns and added the graduation rates instead. 


Exploring the cleaned data, it was unsurprising to find huge variance among the states, not just in the predictor variable, but also in terms of the total dollar amount due to the state and population size. Thus, we tried to standardize the model by adjusting for cost of living in each state; dividing the total budget by the number of students per state (enrollment variable); and creating new variables of funding percent instead of total funding. We also realized that the large states show similar trends, so we created a categorical variable (states with populations greater than 10 million):

  * Cost of living adjustment & Revenue per student (dividing by state enrollment)
  * Percentages of each revenue level out of the total revenue 
  * Outliers are small states
  * Grouping by population size: > 10m and under 10m

The plots below show the percent of local and government funding per each state:
(image url)

# **Percent of Local Revenue per State:**
(image url)

# **Percent of Gov’t (State and Federal) Revenue per State:**
(image url)

The pairplots graphs below show the patterns of revenue percent for states with a population below 10m and above 10m:
(image url)

# **Percent Funding vs. Graduation Rates (States with population < 10m)**
(image url)

# **Percent Funding vs. Graduation Rates (States with population < 10m)**
(image url)

# **Percent Funding vs. Graduation Rates - Normalized (States with population < 10m)**
(image url)

# **Model**

Since all our dependent variables were a derivative of the total funding, there was a high degree of multicollinearity; however by scaling and creating new variables (percent of funding), we managed to get low correlation between our final model variables:

(image url)
# **Correlation Matrix (checking for collinearity)**

The final variables we included in our model are:
  * Local revenue percent
  * Federal revenue percent
  * State size
  
Even though we found some clear trends between the percent of local and government funding and graduation rates in the large states, it was tricky to achieve high correlation. There are many more factors that need to be considered, but with our simplified model we can conclude that If schools rely on local funding more than state/federal, then graduation rates would increase. At the same time, by relying heavily on federal revenue, graduation rates tend to go down. That does not mean the federal funding is causing lower graduation rates, and further studies should explore whether the solution may be relying more on local funding, increasing total federal funding, or other factors.

(img url)
# **MLR Model**

As can be seen in the plot below, the model’s residuals show a clear relationship. We tried to use log transform but it didn’t minimize the residuals.

(image url)
# **Distribution of Target Variable and Residuals Plot**

**Libraries used:**

  * Matplotlib and Seaborn for visualization
  * Pandas for dataframes
  * Statsmodels for OLS model
  * scipy.stats for statistical functions
  * Numpy mainly for transformation functions
  * Sklearn.preprocessing for scaling
