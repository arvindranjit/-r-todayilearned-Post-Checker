import json
from time import sleep
import urllib.request
from urllib.error import URLError, HTTPError


print("Today I Learned Post Watcher\n")

print('This script will display the latest TIL post every 30 seconds (if a new one has been posted)\n')



titleprev = None

url = "https://www.reddit.com/r/todayilearned/new/.json"

words = ['TIL that ', 'TIL about ', 'TIL That ', 'TIL That ', 'TIL About ', 'TIL ']




while True:

    

    request = urllib.request.Request(url, headers={'user-agent':'bot by arvindranjit'})


    print('Checking for new posts.........\n')


    urlflag = 0
    

    try:
        response = urllib.request.urlopen(request)

    except HTTPError as e:
        # do something
        print('\nError code: ', e.code)
        urlflag = 1
    except URLError as e:
        # do something (set req to blank)
        print('\nReason: ', e.reason)
        urlflag = 1


    if urlflag == 1:
        print('Please check your internet connection. Trying Again in 30 seconds\n')
        sleep(30.2)
        continue

    data = json.loads(response.read())



    datadictionary = data["data"]["children"][0]
    title = str(datadictionary["data"]["title"])

    titleformatted = None

    if titleprev != title:
        print('Latest TIL:')

        for word in words:
            if word in title:

             titleformatted = title.replace(word,"")
             titleformatted = titleformatted.replace(titleformatted[0], titleformatted[0].capitalize(), 1)
             break
             


        print(titleformatted)
        print()
    else:
        print('No new posts.\n')

    titleprev = title
    sleep(30.2)