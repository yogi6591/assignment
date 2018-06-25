#ques-1
print("What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).\n")
Overview

The Access Token is a credential that can be used by an application to access an API.

It can be any type of token (such as an opaque string or a JWT) and is meant for an API. Its purpose is to inform the API that 
the bearer of this token has been authorized to access the API and perform specific actions (as specified by the scope that has
 been granted).

The Access Token should be used as a Bearer credential and transmitted in an HTTP Authorization header to the API.

How to get an Access Token

Access Tokens are issued via Auth0's OAuth 2.0 endpoints: /authorize and /oauth/token. You can use any OAuth 2.0-compatible 
library to obtain Access Tokens. If you do not already have a preferred OAuth 2.0 library, Auth0 provides libraries for many 
languages and frameworks that work seamlessly with our endpoints.

#ques2-
print("Get the IP address of some common sites like Google, Facebook by using DNS lookup.\n")

$ nslookup google.com
Non-authoritative answer:
Server:  google-public-dns-a.google.com
Address:  8.8.8.8

Name:    google.com
Addresses:  2404:6800:4002:803::200e
          172.217.24.238
		  
		  
$ nslookup youtube.com
Non-authoritative answer:
Server:  google-public-dns-a.google.com
Address:  8.8.8.8

Name:    youtube.com
Addresses:  2404:6800:4002:803::200e
          172.217.24.238

$ nslookup twitter.com
Non-authoritative answer:
Server:  google-public-dns-a.google.com
Address:  8.8.8.8

Name:    twitter.com
Addresses:  104.244.42.65
          104.244.42.193

		  
		  
#ques-3
print("Using Tweepy library try to extract tweets from Twitter.\n")


import tweepy

consumer_key="Pqq8YLHx7pqttSmRT7ELHw7WR"
consumer_secret="n4eyt60QOpUuofNykxD6kvrmq1GwM9Q72Y65hHBsfOS6ZD7a7A"

access_token="897094313330434048-Tkl2xp3MolrChfKSZ4i6HjEAr8xijRy"
access_token_secret="wA5I7HuCfe0e4lRVDXCVoZ6YGKVaplkA8eSpwOeLGySfK"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
tweets=api.search('#NotWithOutMyDog',lang='en',count=10,tweet_mode='extended')

# print(tweets)
for tweet in tweets:
	print("________________________")
	print(tweet.full_text)
	print("________________________")

print("\n*******************************\n")
	
	
#ques-4
print("What is a difference between library and API . Figure it out with examples.\n")
A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of 
projects. (Various specialized services in our case)

An API is an interface for other programs to interact with your program or library  without having direct access. ( giving
 specifications for our need to various vendors in our case)