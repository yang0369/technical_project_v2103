# Technical Project
The ability to deep-dive into large volumes of telco data, derive insights and distill complex results into actionable 
items is greatly appreciated as a Data Scientist. 

Inside this test, you are required to choose and solve ONE problem and implement a solution quickly. All candidates 
will be given **5 days** to work on **ONE** problem statement.  

Note that the candidates will be evaluated based on  

1) understanding of data analysis methodology,  

2) implementation skills,  

3) creative & innovative thinking, and  

4) thought process in performing the tasks. 

## Getting started

First of all, select a problem from the following list, develop a solution based on the test data given, and update 
their respective notebook.
Reminder: You just need to work on ONE of the notebooks.

### Problems

#### Problem Statement 1: Develop a dashboard to tell your data story

- Decide on a data story to tell based on the dataset you pick, show 6-8 insights in your story.
- Use an open source dashboard, such as Jupyter Dash, Streamlit, ElasticSearch Kibana etc to visualize your insights.
- The data story should be obvious without needing further verbal presentation.
- In case you need some tips, these are some stories you can tell, but feel free to propose your own topics:
    - Favourite Brands: e-Commerce, bank, social media, news sites etc
    - Life stage: Single, In-a-relationship, Couple, Parent, Retiree etc
    - Life moment: Buying a car, moving a house, expecting a child etc
    - Personas: Food Lover, Movie Goer, Luxury Connoisseaur etc


#### Problem Statement 2: Develop a solution to perform user segmentation

Tasks and requirements:

Develop an unsupervised model to identify clusters of users belong to the same group

###### <u>Ans: I used Kmeans and Agglomerative Clustering methods.</u>

Decide what type of user clusters to build

###### <u> Ans: I try to cluster the users based on their browsing interest or their interested topics</u>

Tell a story about each cluster, eg. describe the dominant attributes of the cluster

###### <u>Ans:</u>

###### <u>- cluster 0: [1, 4, 5, 7, 15, 18, 20, 22, 23, 24, 25, 26, 27, 30, 31]</u>

###### <u>they tend to browse corporate related, such as wellness, reference, technology, so they are probably working adults, and like to post personal life activities on blogs or social media, like playing games and do shopping.</u>  

###### <u>- cluster 1: [3, 21]</u>

######  <u>This group of people seems to be enjoying their life, they browsed art, food, travel, gaming, wellness and even fortunetelling, they browsed education as well, so I guess they are probably school students or young working adults studying part time.</u>  

###### <u>- cluster 2: [2, 6, 8, 9, 10, 11, 17, 19, 28, 29]</u>

###### <u>Similar to group 0, this group of people probably are working in finance-related industry as they browsed banking, finance, technology and education.</u>  

###### <u>- cluster 3: [16]</u>

###### <u>this guy is interested in real estate, cars, homeservices, I guess he probably is buying/bought a house or a car. Also he browsed manga, tavel, ecommerce, jobsearch, education, which implies he is a young adult. he has interests in trading, gambling, which shows he is a risk-taker. In addition, he likes pet apparently. So some stuff related to pets maybe attract his attention.</u>  

###### <u>- cluster 4: [13]</u>

###### <u>compared to the cluster 3 guy, this guy is more conservative as he did not browse any trading or gambling, but he is interested in music, entertainment, sports, gaming and even philanthropic! He is as well interested in real estate and cars, so I suppose he is also an young adult with very healthy hobbies.</u>  

###### <u>- cluster 5: [12]</u>

###### <u>Apart from these common interests, this guy browsed real estate, computer, audtion, cars, fashion, shopping etc. thus I am confident to say that he is going to buy some stuff related to computer, cars or even house. He may be quite happy to receive some promotion for computers or electronics devices.</u>  

###### <u>- cluster 6: [14]</u>

###### <u>this guy is looking for car parking and cars, so I guess he is going to buy a car or change car with very high chance. He/she also likes alcohol and tobacco, and interested in education and jobsearch, so he/she is not old definitely. In addition, he/she likes fashion, eccommerce, travel, shopping, so some e-commerce advertisements maybe can attract his attention.</u>

Tell a story about your result

###### <u>Ans: Based on the users' browsing history, we are able to tell the users' interested topics, their dominant traits and what they may like or dislike, this result of analysis could be applied to find which group of people is more likely to be our tragets for marketing or advertisement campaign.</u>   

Reader should be able to re-create your experiment and understand your story by running the notebook 

###### <u>Ans: For the details of the analysis, please refer to my notebook - "notebooks/2.0_user_segmentation.ipynb".</u>


#### Problem Statement 3: Develop a user embedding

Tasks and requirements:
- Develop a vector representation for each user based on their browsing behaviour
- Given a user ID, identify the top-K similar users 
- Tell a story about your result
- Reader should be able to re-create your experiment and understand your story by running the notebook 


#### Problem Statement 4: Develop a browsing graph

Tasks and requirements:
- Develop a browsing graph using Neo4j community edition and py2neo connector. Feel free to replace Neo4j with other 
  GraphDB that you're more familiar of. 
- Tell a story about your result
- Reader should be able to re-create your experiment and understand your story by running the notebook 


### Test Data

The following dataset(s) is available:

| Dataset name | Path | Description |
|----|----|----|
| Browsing | .src/data/browsing_behavior | Synthetic browsing data of 31 users in Parquet format |

#### Test Data Schema

| Dataset name | Column Name | Description |
|----|----|----|
| Browsing |user_id | Unique identifier for each user |
| Browsing |category_name | Classified category of a domain |
| Browsing |application_name |	Application name of a domain |
| Browsing |domain_tags | Classified tag of a domain |
| Browsing |domain	| Web address |
| Browsing |volume	   | Amount of data upload and download during the session |
| Browsing |duration  | Amount of time take to upload and download data during the session |
| Browsing |server_ip | Destination IP connected during the session |
| Browsing |referer_category |	 Redirected from a domain under this category |
| Browsing |referer_domain | Redirected from this web address |

#### Assumption
1. You may assume that the browsing history of each user has been sessionized and is recorded sequentially across 
   multiple days. Hence there's a sequence order.
   
2. You may assume that referer_category does not link to category_name.



In case necessary, add the following code chunk to your python script in order to access your project package.

```python
import os
import sys
module_path = os.path.realpath(os.path.abspath('../src/'))
if module_path not in sys.path:
    sys.path.append(module_path)
```

### Test

Optionally, provide instruction to run test, API, code coverage.



