from apiclient import discovery
from apiclient import errors
import argparse

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
# https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
# DEVELOPER_KEY = "AIzaSyDm756_WGLl1LnMD8MawzdzpsBZalcFasQ"
DEVELOPER_KEY = "AIzaSyBmgcKRgFpOKGlpvLwIXK8JSZ-mE2lKx5I"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def extract_youtube(options):
    youtube = discovery.build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY,
    )

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = (
        youtube.search()
        .list(
            q=options.q,
            order="viewCount",
            type="video",
            location=options.location,
            locationRadius=options.location_radius,
            part="id,snippet",
            maxResults=options.max_results,
        )
        .execute()
    )

    # Merge video ids

    search_videos = []
    for search_result in search_response.get("items", []):
        search_videos.append(search_result["id"]["videoId"])
    video_ids = ",".join(search_videos)

    # Call the videos.list method to retrieve location details for each video.
    video_response = (
        youtube.videos().list(id=video_ids, part="snippet, recordingDetails, statistics").execute()
    )

    # Add each result to the list, and then display the list of matching videos.
    videos = []
    for video_result in video_response.get("items", []):
        tmp = {
            "title": video_result["snippet"]["title"],
            "latitude": video_result["recordingDetails"]["location"]["latitude"],
            "longitude": video_result["recordingDetails"]["location"]["longitude"],
            "view_count": video_result["statistics"]["viewCount"],
            "like_count": video_result["statistics"]["likeCount"],
            "dislike_count": video_result["statistics"]["dislikeCount"],
            "comment_count": video_result["statistics"]["commentCount"],
            "id": video_result["id"],
            "date": video_result["snippet"]["publishedAt"],
        }
        videos.append(tmp)
    return videos
    # print("\n".join(videos))
    # print ("Videos:\n", "\n".join(videos), "\n")


def search_youtube(word, lati, longi):
    argparser = argparse.ArgumentParser(conflict_handler="resolve")
    argparser.add_argument("--q", help="Search term", default=word)
    argparser.add_argument("--location", help="Location", default=f"{lati}, {longi}")
    argparser.add_argument("--location-radius", help="Location radius", default="1000km")
    argparser.add_argument("--max-results", help="Max results", default=10)
    args = argparser.parse_args()

    try:
        return extract_youtube(args)
    except errors.HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
