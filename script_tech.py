import instaloader
import csv
from datetime import datetime, timedelta
L = instaloader.Instaloader()
print("InstaCrawl Script")
print("Input your Instagram username: ", end="")
user = ""
password = ""
L.interactive_login(user, password)
#L.login("ProbEst__", "Pauperedeiros")

print("Input Hashtag: ", end="")
hashtag = "tech"
print("Input number of posts linked to profiles to parse: ", end="")
nposts = 20
print("Input profile followers minimum value: ", end="")
followermin = 10000

print("OK, starting job...")

profiles = []
count = 0
for post in L.get_hashtag_posts(hashtag):
    profile = post.owner_profile
    if profile not in profiles and profile.followers >= followermin:
        profiles.append(profile)
        print("[" + str(count) +"] Selected: " + str(profile.username))
        count = count + 1
        if count >= nposts:
            break
        
date_7_days_ago = datetime.utcnow() - timedelta(days=7)
date_45_days_ago = datetime.utcnow() - timedelta(days = 45)
date_now = str(datetime.now().date()) + '_' + str(datetime.now().time())
with open("instaCrawl_" + hashtag+ "_"+ date_now + ".csv", 'w', newline='') as file:
    output = csv.writer(file)
    output.writerow(["Hashtag", "Username", "Followers", "Post Number (newer First)", "Likes", "Business Category"])
    for profile in profiles:
        username = profile.username
        followers = profile.followers
        is_business_acc = profile.is_business_account
        if is_business_acc:
            category = profile.business_category_name
        else:
            category = "NULL"
        print("{}, {}, {}".format(username, followers, category))
        count = 0
        for post in profile.get_posts():
            if post.date_utc <= date_7_days_ago and hashtag in post.caption_hashtags and post.date_utc >= date_45_days_ago:
                print("[{}] {}".format(count, post.likes))
                output.writerow([hashtag, username, followers, count, post.likes, category])
                if count >= 9:
                    break
                count = count + 1
print("Job done")
print("Script made by Pau Antonio, Pere Tarrida and Oriol Deiros for Statistics subject. Universitat Politècnica de Catalunya 2019-2020")