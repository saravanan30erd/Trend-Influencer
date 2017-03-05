# Trend-Influencer
Python application to find the top twitter Influencers and trends in India(twitter data mining).

  Influencers - Twitter user who have more followers.

# Notes
I am using two set of twitter keys for this project due to twitter search API restrictions.
Please update your own twitter application secret keys in app/config.ini file.
I used docker to run this application, so I seperated this appliation as backend and frontend.
Backend - It will scrawl the twitter data and store it in Mongodb.
Frontend - It will show the twitter data from Mongodb using Flask.

Docker compose will start three containers, one for backend app, second for frontend app and third for mongodb.

# Steps
  - Install the docker in your machine.
  - Clone this repo.
  - Update your own twitter application secret keys in app/config.ini file.
  - Run the below docker compose command, docker-compose up -d
  
  Refer: https://docs.docker.com/compose/





