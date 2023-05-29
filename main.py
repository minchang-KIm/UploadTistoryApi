import TistoryAPI as API
from dotenv import load_dotenv
import os, json
import requests

def postWrite(blog_name, title, content="", visibility=None, category_id=None, published=None, slogan=None, tag=None,
              acceptComment=None, password=None, output_type="json"):
    url = "https://www.tistory.com/apis/post/write?"
    data = {}
    data['access_token'] = access_token
    data['output'] = output_type
    data['blogName'] = blog_name
    data['title'] = title
    data['content'] = content
    #url += "access_token=" + access_token + "&"
    #url += "output=" + output_type + "&"
    #url += "blogName=" + blog_name + "&"
    #url += "title=" + title + "&"
    #url += "content=" + content + "&"
    if visibility is not None:
        url += "visibility=" + visibility + "&"
    if category_id is not None:
        url += "category=" + category_id + "&"
    if published is not None:
        url += "published=" + published + "&"
    if slogan is not None:
        url += "slogan=" + slogan + "&"
    if tag is not None:
        url += "tag=" + tag + "&"
    if acceptComment is not None:
        url += "acceptComment=" + acceptComment + "&"
    if password is not None:
        url += "password=" + password
    #data += "category=" + "1024642"
    res = requests.post(url, data=data).content
    return json.loads(res)








if __name__ == "__main__":
    load_dotenv()
    client_id = str(os.environ.get("client_id"))
    client_secret = str(os.environ.get("client_secret"))
    access_token = os.environ.get("access_token")
    redirect_uri = os.environ.get("redirect_uri")
    a = API.BlogInfo()
    print(a)