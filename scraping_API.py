import pandas as pd
from tqdm import tqdm
from google_play_scraper import Sort, reviews

app_packages = [
  # Graphics & Design
  'com.canva.editor', #Canva
  'com.delgeo.desygner', #Desygner
  'com.brakefield.idfree', #Inifite Design
  'com.design.studio', #Design Studio
  'com.dephotos.crello', #Crello'
  'com.houzz.app', #Houzz
  'com.adobe.spark.post', #Adobe Spark Post
  'com.logopit.logoplus', #Logo Maker Plus
  # Entertainment
  'com.amazon.avod.thirdpartyclient', #Amazon Prime Video - Entertainment
  'com.netflix.mediaclient', #Netflix
  'com.disney.datg.videoplatforms.android.watchdc', #Disney
  'com.hbo.hbonow', #HBO Max
  'com.mtvn.mtvPrimeAndroid', #MTV
  'com.hulu.plus', #HULU
  'com.cbs.app', #Paramount
  'com.nick.android.nickjr', #Nick. Jr.
  'com.cw.fullepisodes.android', #The CW
  'com.rhythmnewmedia.tmz', #TMZ
  'com.kiloo.subwaysurf', #Subway Surfers
  #Photo & Videos
  'com.adobe.psmobile', #Adobe Photoshop
  'com.niksoftware.snapseed', #Snapseed
  'com.adobe.lrmobile', #Adobe Lightroom
  'photo.editor.photoeditor.photoeditorpro', #Photo Editor Pro
  'com.picsart.studio', #Picsart
  'vsin.t16_funny_photo', #Photo Lab Picture Editor
  'photo.editor.photoeditor.filtersforpictures', #Photo Editor
  #Travel
  'com.tripadvisor.tripadvisor', #Tripadvisor
  'com.expedia.bookings', #Expedia
  'com.booking', #Booking
  'ctrip.english', #Trip.com
  'com.trivago', #Trivago
  'com.kayak.android', #Kayak
  'com.airbnb.android', #Airbnb
  'com.couchsurfing.mobile.android', #Couchsurfing
  #Finance
  'com.yahoo.mobile.client.android.finance', #Yahoo Finance - Finance
  'com.bloomberg.android.plus', #Bloomberg
  'com.fusionmedia.investing', #Investing.com
  'com.mint', #Mint
  'com.bookmark.money', #Money Lover
  'com.microsoft.amp.apps.bingfinance', #MSN Money
  #Health & Fitness
  'com.huawei.health', #Huawei Health
  'com.sec.android.app.shealth', #Samsung Health
  'com.google.android.apps.fitness', #Google Fit
  'com.fitbit.FitbitMobile', #Fitbit
  'com.myfitnesspal.android', #Calorie Counter
  'homeworkout.homeworkouts.noequipment', #Home Workout
  #Music
  'com.google.android.apps.youtube.music', #Youtube Music
  'com.spotify.music', #Spotify
  'com.apple.android.music', #Apple Music
  'com.soundcloud.android', #SoundCloud
  'com.amazon.mp3', #Amazon Music
  'com.musixmatch.android.lyrify', #Musixmatch
  'deezer.android.app', #Deezer
  'com.shazam.android', #Shazam
  #Productivity
  'cc.forestapp', #Forest
  'com.ticktick.task', #TickTick
  'com.monday.monday', #Monday
  'co.thefabulous.app', #Fabulous
  'com.superelement.pomodoro', #Focus To-Do
  'com.microsoft.todos', #Microsoft To Do
  'com.todoist', #Todoist
  'com.google.android.calendar', #Google Calendar
  'com.sillens.shapeupclub', #Lifesum - Lifestyle 
  #Social Networking
  'com.twitter.android', #Twitter
  'com.snapchat.android', #Snapchat
  'com.instagram.android', #Instagram
  #Unclassified
  'com.nianticlabs.pokemongo', #Pokemon Go - Games
  'com.nordvpn.android', #NordVPN - Utilities
  'org.khanacademy.android', #Khan Academy - Education
  'com.google.android.apps.magazines', #Google News - News
  'com.handmark.sportcaster', #CBS Sport - Sport
  'com.accuweather.android', #Accuweather - Weather
  'com.lydia' #Lydia Wire Transfers - Banking
]

app_reviews = []
for ap in tqdm(app_packages):
  for score in [1,2,3,4,5]:
    for sort_order in [Sort.MOST_RELEVANT, Sort.NEWEST]:
      rvs, _ = reviews(
        ap,
        lang='en',
        country='us',
        sort=sort_order,
        count= 200,
        filter_score_with=score
      )
      for r in rvs:
        r['sortOrder'] = 'most_relevant' if sort_order == Sort.MOST_RELEVANT else 'newest'
        r['appId'] = ap
      app_reviews.extend(rvs)

app_reviews_df = pd.DataFrame(app_reviews)

app_reviews_df.to_csv('reviews.csv')