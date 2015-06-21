# HighlandLights
Home automation and light controller system

##Overall System
![System layout](overview.png?raw=true "System Layout")
<p>
Scripts:<br>
<ul>
<li>Youtube downloader</li>
<li>Playlist manager</li><ul>
<li>Read songs from twitter</li>
<li>Search if song exists on hard drive</li><ul>
<li>Download file if it doesn’t exist</li></ul>
<li>Add file to playlist</li></ul>
<li>XBMC controls (Play, Pause, etc.)</li><ul>
<li>Stop or start the file on the light controller</li></ul>
<li>Light Controller script (already done)</li>
</ul>

##Setting up dev environment
<ol>
<li>Install python</li>
<li>Install <i>pip install --upgrade google-api-python-client</i> for additional google python libraries</li>
<li>Install <i>pip install youtube-dl</i></li>
</ol>

## Scripts
#### YoutubeParser.py
Given a search query, find the most relevant youtube video 
related to that search. Returns the title, description,
id, and URL of that video. Then downloads that video as mp3
