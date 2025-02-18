# osu-stats-boxplots
A script that helps poolers determine the difficulty of their pools by displaying the performans of the players in boxplots.

To get started just download this repository by clicking the flashy "code" button to the top right of github, download ZIP, extract the files, fill in the relevant information to 'api.txt', 'map list.txt' and 'MP links.txt'. after taht simply open 'boxplots.exe'. 

You might need to give the script permission to run before it can open, but after that you should see the client open. Set in the appropriate settings for your tournament, scroll down and press "execute script".

To request the data you need to have an API key. If you have never used the osu!api before you can get one in your osu! account settings page under the OAuth section (You need apiv2. The key under the Legacy API section is not good enough). Write a random name and a random URL, for an examble: `http://localhost:XXXX/` where you replace “XXXX” with a random 4 digit number greater than 1024. Here you will get your client ID and client secret.

The map list need to be structured in three lines:
Round
comma seperated map slots
comma seperated maps

The MP links can be either the IDs or the full url.