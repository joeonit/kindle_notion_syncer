import requests
import json

database_ID = os.environ.get("database_ID")
secret_Key = os.environ.get("secret_Key")

def get_pageid_for_title(title):
    url = f"https://api.notion.com/v1/databases/{database_ID}/query"
    payload = {
        "page_size": 100,
        "filter": {
            "property": "Name",
            "rich_text": {
                "equals": title
            }
        }
    }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {secret_Key}"
    }

    response = requests.post(url, json=payload, headers=headers)

    # print(response.text)

    data = json.loads(response.text)
    if len(data['results']) == 0:
        return None
    page_id = data['results'][0]['id']
    return page_id



def get_list_of_paragraphs_for_page_with_title(title):
    page_id = get_pageid_for_title(title)
    print(page_id)


    url = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Authorization": f"Bearer {secret_Key}"
    }

    response = requests.get(url, headers=headers)

    paragraphs = []
    data = json.loads(response.text)
    for item in data['results']:
        print("ITEM")
        print(item)
        stringer = ""
        try:
            item['quote']
        except:
            continue
        for words in item['quote']['rich_text']:
            stringer += words['plain_text']
        paragraphs.append(stringer)

    return paragraphs


def append_items_to_page(title, items):
    children_array = []
    for item in items:
        children_array.append(
            #{
            #    "type": "paragraph",
            #    "paragraph": {
            #        "rich_text": [{
            #            "type": "text",
            #            "text": {
            #                "content": item,
            #                "link": None
            #            }
            #        }],
            #        "color": "default",
            #    }
            #}
            {
                "type": "quote",
                "quote": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": item,
                        },
                    }],
                    "color": "default"
                }
            }
        )

    page_id = get_pageid_for_title(title)

    url = f"https://api.notion.com/v1/blocks/{page_id}/children"

    payload = {
        "children": children_array
    }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {secret_Key}"
    }

    response = requests.patch(url, json=payload, headers=headers)

    print(response.text)



def create_page(title, author, paragraph_list):
    url = "https://api.notion.com/v1/pages"
    children_list = []
    for text in paragraph_list:
        children_list.append(
            #{
            #    "type": "paragraph",
            #    "paragraph": {
            #        "rich_text": [{
            #            "type": "text",
            #            "text": {
            #                "content": text,
            #                "link": None
            #            }
            #        }],
            #        "color": "default",
            #    }
            #}
            {
                "type": "quote",
                "quote": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content":text,
                        },
                    }],
                    "color": "default"
                }
            }
        )

    payload = {
        "children": children_list ,
        "parent": {
            "type": "database_id",
            "database_id": database_ID
        },
        "properties": {
            "Name": {
                "title": [
                    {
                        "type": "text",
                        "text": {
                                "content": title
                        }
                    }
                ]
            },
            "Author": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": author
                        }
                    },
                ]
            }
        }
    }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {secret_Key}"
    }

    response = requests.post(url, json=payload, headers=headers)

