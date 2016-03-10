# -*- coding: utf-8 -*-
import tweepy

#authentication gia to api
consumer_key= 'HCX6egNFulxjd25JjJ49xOgH7'
consumer_secret= '	XhbYR58eCMWiUfImqoSvD2UoqSC35ikdUIFHNgU79UKU6UGVyX'
access_token= '882153175-C1QB4nuEyMvVLk0kSSdjT9WpwedOfehvXbX1HCVs'
access_token_secret= 'mNGNdBBAxkRGJcLmULTs1YgSL6cQ7eDbmw7bRxPgqYSbk'



if __name__ == '__main__':
    user1 = raw_input("Dwse prwto username") # prwtos user
    user2 = raw_input("Dwse deytero username")#deyteros user
    # Dhmiourgia ton authication tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    
    print ("Dedomena gia tous 2 user")

    # Pernw ta info gia twn prwto user
    data = api.get_user(user1)
    #Followers=Followers/Tweets=Tweets/Like= Like/Friends= the number of the person that the user follows
    print 'Followers tou Prwtou: ' + str(data.followers_count)
    print 'Tweets tou Prwtou: ' + str(data.statuses_count)
    print 'Like tou Prwtou: ' + str(data.favourites_count)
    print 'Friends tou Prwtou: ' + str(data.friends_count)
    #apothikevw gia xrhsh
	user1F = data.followers_count
	user1T = data.statuses_count
	user1L = data.favourites_count
	user1FR = data.friends_count
	# pernw a dedomena gia ton deytero user
	
	data1 = api.get_user(user2)
	print 'Followers tou Deyterou:' + str(data1.followers_count)
	print 'Tweets tou Deuterou:' + str(data1.statuses_count)
	print 'Like tou Deyterou:' + str(data1.favourites_count)
	print ' Friends tou Deyterou:' + str(data1.friends_count)
	# apothikevw gia user 2
	user2F = data1.followers_count
	user2T = data1.statuses_count
	user2L = data1.favourites_count
	user2FR = data1.friends_count
	
	skor1 = 0
	skor2 = 0
	if user2F > user1F :
	 skor2 +=1
	else :
	 akor1 +=1
    if user2T > user1T :
	 skor2 +=1
    else :
	 skor1 +=1
    if user2L > user1L :
	 skor2 +=1
    else :
	 skor1 +=1
    if user2FR > user1FR :
	 skor2 +=1
    else :
	 skor1 +=1
   print "Skor %d-%d"%(
   skor1,skor2)
	
	
	
