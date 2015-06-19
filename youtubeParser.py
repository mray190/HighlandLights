# Given a search query, find the most relevant youtube video
#    related to that search. Returns the title, description,
#    id, and URL of that video

# Youtube developer documentation:
# https://developers.google.com/youtube/v3/getting-started
# https://developers.google.com/youtube/v3/docs/search/list

from apiclient.discovery import build
from apiclient.errors import HttpError

DEVELOPER_KEY = "AIzaSyDi_wkk3TXvoNp8J-wDvfaGJgsHvxbKmkI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

	search_response = youtube.search().list(
		q=query,
		order="relevance",
		safeSearch="none",
		type="video",
		part="id,snippet",
		maxResults=1
	).execute()

	search_result = search_response.get("items",[])
	if len(search_result)>0:
		title = search_result[0]["snippet"]["title"]
		description = search_result[0]["snippet"]["description"]
		id = search_result[0]["id"]["videoId"]
		url = "https://www.youtube.com/watch?v=" + id
		print "Title: " + title
		print "Description: " + description
		print "ID: " + id
		print "URL: " + url

if __name__ == "__main__":
	try:
		search_terms = "leeroy jenkins"
		youtube_search(search_terms.decode("utf-8").replace(" ","+"))
	except HttpError, e:
		print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)