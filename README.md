# PyTunes 

PyTunes is a **real time Music recommendation engine** which recommends globally trending Spotify tracks based on your musical taste.

## 1) How to use?: 
1) Open Spotify app or go to https://open.spotify.com/
2) Copy the url to your favourite playlist or album, and paste!
3) Click on Recommend and enjoy the recommendations !

https://user-images.githubusercontent.com/40240678/125155433-75e47480-e17d-11eb-934f-d9798936153a.mp4

### Try it out yourself: 
https://pytunessss.herokuapp.com/


## 2) Data Pipeline and Application Architecture:

1) **Acoustical Data** of the global trending songs is Extracted (via Spotify API calls), Transformed and Loaded daily to **AWS RDS database** instance via the **automated ETL pipeline** deployed on **AWS EC2**. 
2) When user enters the URL of his favourite playlist or album, the corresponding **acoustical data** is extracted using Spotify's Web API.
3) Recommendations are produced using data mining algorithms on the user entered data and the data sitting in the AWS RDS database instance.

![PyTunes Architecture](https://user-images.githubusercontent.com/40240678/123195100-35ba9c00-d4c5-11eb-933c-d8142c2a3335.png)


## 3) Tools, Technologies and Frameworks used:
● Built and deployed an automated ETL data pipeline on AWS to extract acoustic data of trending 
songs daily from Spotify using API calls. AWS EC2 and RDS services were used.

● Implemented a Data mining model in Python(Pandas , Numpy , SkLearn) to generate recommendations from the extracted data. 

● Deployed the model to cloud, as a REST API endpoint using Flask and Heroku.

● Implemented CI/CD using Git and Heroku.
