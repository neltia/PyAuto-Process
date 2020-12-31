from notion.client import NotionClient

token = "your token"
client = NotionClient(token_v2=token)

notion_url = "your page link"
page = client.get_block(notion_url)

print("원래 제목:", page.title)
page.title = "페이지 제목이 바뀌었습니다."
