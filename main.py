import gdown
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

client_secrets_file = ".\\service_account\\youtube_service_account.json"
credentials = service_account.Credentials.from_service_account_file(client_secrets_file, scopes=SCOPES)
youtube = build('youtube', 'v3', credentials=credentials)


request = youtube.playlistItems().list(
    part="snippet,contentDetails",
    maxResults=50,
    playlistId="PL3R7T9stcQyyyxL4xJofSmnojvurOFnHi"
)

response = request.execute()
links=[]
for i in response['items']:
    links.append("https://drive.google.com/uc?export=download&id="+i['snippet']['description'].split("/")[5])
print(links)
count=1
for i in links:
    file_name_link="output/"+str(count)+".pdf"
    gdown.download(i, file_name_link, quiet=False)
    count=count+1
