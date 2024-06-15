# Offline-YouTube-Playlist-Sorter
A Python tool that automatically renames your downloaded videos to match the original order of a YouTube playlist. Using the YouTube Data API and fuzzy matching, it organizes your videos perfectly, even if filenames aren't exact matches. Ideal for content creators, educators, and anyone needing an easy way to keep their video collections in order.

Have you ever downloaded a YouTube playlist using a tool like jDownloader2 so you could watch them offline. I have done this many times, but when doing this the downloaded videos will be downloaded in alphebetical order, not the order of the playlist. This can be a problem if the downloaded videos are apart of a series and need to be watched in order. This simple python script will use the YouTube API to check the correct order of the videos, then rename all the videos on your computer by adding a number to the start of each video, in order. This way when sorting the downloaded videos by alphebetical order they will be in the correct, original YouTube playlist order. No other part of the downloaded videos titles change.

STEPS TO USE:

  1: The first step will be to get your YouTube API key. To do this log into your google account and visit https://console.cloud.google.com. Click on the Quick access button 'APIs and Services.' 
<img width="1173" alt="image" src="https://github.com/MakoCat/Offline-YouTube-Playlist-Sorter/assets/97393692/d19f614d-89fc-4c6b-b056-54c17a519e22">
*If you don't see this section (it should be very obvious) you may need to click the dropdown menu in the top left next to the 'Google Cloud' logo and create a new project.*
On the left side click the section for 'Library' and in the search bar search for 'youtube data api v3:'
<img width="1359" alt="image" src="https://github.com/MakoCat/Offline-YouTube-Playlist-Sorter/assets/97393692/ce227138-292d-4f4d-bbf5-04731ae024d7">
Double click on the resulting product and click the blue button that says 'Enable.' You should now be redirected to the APIs and Services page.
On the left side menu click the button for 'Credentials'
<img width="1434" alt="image" src="https://github.com/MakoCat/Offline-YouTube-Playlist-Sorter/assets/97393692/1ed260e7-1a61-4c7d-a308-e2f2bffde61a">
At the top center click 'Create Credentials' and choose 'API Key' from the dropdown options. Wait a couple seconds and then it will display your API Key. Copy this and save it in a notepad for now

  2: The second step will be downloading python. I won't explain this very deeply, there are guide online and it's pretty simple. Just visit Python.org/downloads. If you are using Windows you can just press windows+r and type cmd and return. When the command prompt pops up you can just type the word 'python' into the window and will prompt you to download Python.

  3: The third step is copying my Python script and modifying it to fit your playlist and downloaded folder. Visit the file on this project called 'rename.py' and copy all the text there. Paste it all into textEdit if using Mac, or Notepad if using Windows. Towards the bottom of the Python script you will see three lines called:
api_key = 'xxxxx'  # Replace with your YouTube Data API key
playlist_id = 'xxxxx'  # Replace with your YouTube playlist ID
directory = 'xxxxx' # Replace with the path to your downloaded videos directory (if using Windows, add an r in front of the path, r'xxxxx'
Replaces the x's with you info. Don't modify any other lines. The YouTube playlist ID is youtube.com/watch?v=KiEptGbnEBc&list=xxxxx&pp=iAQB. Only the 'xxxxx' is the playlist ID. At this point save your file and name it something such as 'rename.py'. By default the computer may try to save it as a txt file, you can verify it saved as a .py file by right clicking the file and choosing 'properties' if using Windows, or 'Get Info' if using Mac. For Windows it should say 'Type of file: PY file' and for Mac it should show the same as this picture. 
<img width="235" alt="image" src="https://github.com/MakoCat/Offline-YouTube-Playlist-Sorter/assets/97393692/f73f9354-469b-4e66-98d5-468afb9e6aa0">
If it doesn't say it is a .py file, double check the file name ends with .py, instead of .txt. *A note here, if you need to modify the file for any reason, since it is a simple file I recomend right-clicking the file and open with -> Notepad or TextEdit.*

  4: Almost done, if using Windows type windows+r and type cmd and enter. If using Mac, type command+space and type terminal and return. In the terminal that pops up type this command: 'pip install google-api-python-client fuzzywuzzy[speedup]' and wait a minute or two for everything to install. fuzzywuzzy is the tool that helps infere title names if your downloaded files are slightly different names then the actual YouTube playlist. Then, regardless of using Mac or Windows type 'cd /path/to/directory/containing/rename.py' An easy way to do this is type 'cd' then drag and drop the rename.py file into the terminal. The delete the 'rename.py' text and hit return. Finally type 'python3 rename.py' and the script should rename all your files. There are some basic debugging features of the script if something doesn't work it may be able to tell you why.



  *It should be noted that, at least when using a new API key, users are limited to 10,000 API request per day. But who has playlists that long.*
