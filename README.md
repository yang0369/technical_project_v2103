# technical_project_v2103



# Intro:

My tentative analytical works for a technical assignment.



In this assignment, I was given 31 users with their telco browsing records data, and asked to come out any idea or findings based on this datasets. I decided to guess their interest by clustering these users using unsupervised learning models. I think this kind of analysis work may be helpful for advertisement or marketing campaigns, of course, a  good learning opportunity for me as well.  



# Quick Tour:

all the analysis and modelling works -> notebooks/2.0_user_segmentation.ipynb

To create an anaconda environment with all the required packages -> open terminal, cd to this project' directory, then run 

```
conda env create --file my_conda_env.yml
```

```py
conda activate starhub 
```

run basic testcase for notebook -> open terminal, cd your directory to "tests/", type

```
 pytest test_notebook.py
```



# Project Structure:

<img src="./images/image-20220110130444318.png" alt="image-20220110130444318" style="zoom:25%;" />

There are 4 problem statements in this assignment, I have tried problem statement 2 - notebooks/2.0_user_segmentation.ipynb, Thus all the analysis can be found in this notebook only.



# Interesting Sharings

The dataset contains categorical variables, and most of them are highly correlated.

![image-20220110123431520](./images/image-20220110123431520.png)

For example, "category_name" and "domain_tags", "referee_domain" and "referer_category". By their names suggest, they carries similar information. In order to get some meaningful features, I tried to feature engineering them,  also impute the missing values. Finally I derived this wide table as below: 

![image-20220110124043604](./images/image-20220110124043604.png)

Now, we are ready to proceed to fit our ML model, but before that, we need to standardize our data as we are going to apply distance-based model.

![image-20220110124200711](./images/image-20220110124200711.png)

The features now have the same range and variation, time to train models. (*all data here are synthetic data)

Firstly I have tried K-Means model, as K-Means is relatively memory efficient, but seems the result is not as good as I expected, most of the users are grouped into cluster 0, while only very few users are grouped individually. Apparently we cannot get any useful information based on their groupings. I guess this is probably due to the high dimensionality of our dataset, because we have too many categories in total. 

Next, I have tried Agglomerative + Dendrogram method, I think this time the result is more convicing in terms of interpretability. I think this is because Agglomerative is using max distance to group the similar users, so it is more sensitive to the features in sparse data. For example, user_A has a very rare interest that other users dont have, at the same time, user_B also has this interest, then in terms of this feature, the distance between A and B is very short while the distance with other user shall be very large. For K-Means, it uses average distance to group the users, thus this rare feature may not affect the overall groupings if the rest of features are similar enough.

For the details of this analysis, please refer to my notebook - "notebooks/2.0_user_segmentation.ipynb".

### Reference:

 - Spark: https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.DataFrame.html
 - SOM： https://medium.com/analytics-vidhya/self-organizing-map-customer-segmentation-in-banking-9d7ce96bd3ec
 - dendrogram: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html