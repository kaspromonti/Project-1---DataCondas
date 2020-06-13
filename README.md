# Project-1---DataCondas

Impact to YouTube data over XXX period as compared to XXX

OBJECTIVE: 
How has covid-19 impacted YouTube Usage?
  1. Upload volume by category
  2. # Views
  3. Volume by region
  4. Monetized?
  
RESOURCES:

youtube api video category id list
https://gist.github.com/dgp/1b24bf2961521bd75d6c

noncovid_time = April 1, 2019 - May 31, 2019
covid_time = April 1, 2020 - May 31, 2020

HOW:
Using YouTube Data API, pulling in data from for the two identified time frames for comparison.

viewership time of day
total views
by category
trends on search topics 

publish date
category
statistics
view count like


JSON()SAMPLE:
"kind": "youtube#videoListResponse",
 "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/sDAlsG9NGKfr6v5AlPZKSEZdtqA\"",
 "videos": [
  {
   "id": "7lCDEYXw3mM",
   "kind": "youtube#video",
   "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/iYynQR8AtacsFUwWmrVaw4Smb_Q\"",
   "snippet": { 
    "publishedAt": "2012-06-20T22:45:24.000Z",
    "channelId": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    "title": "Google I/O 101: Q&A On Using Google APIs",
    "description": "Antonio Fuentes speaks to us and takes questions on working with Google APIs and OAuth 2.0.",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/default.jpg"
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/mqdefault.jpg"
     },
     "high": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/hqdefault.jpg"
     }
    },
    "categoryId": "28"
   },
   "contentDetails": {
    "duration": "PT15M51S",
    "aspectRatio": "RATIO_16_9"

Category"categoryId": "28"
description
statistics": {
    "viewCount": "3057",
    "likeCount": "25",
    "dislikeCount": "0",
    "favoriteCount": "17",
    "commentCount": "12"

