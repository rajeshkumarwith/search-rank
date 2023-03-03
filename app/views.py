
from django.shortcuts import render
from .models import *
from django.conf import settings
import requests
from requests.exceptions import RequestException
import pandas as pd
from datetime import datetime
from urllib.parse import quote_plus
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
SEARCH_KEY="AIzaSyCYux7cSQyCqy9jaNi0ZBpvJfjV1sNTZRY"
SEARCH_ID="3077dc85d6a014700"
COUNTRY="in"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT=20



def add(request):
    # get the API KEY here: https://developers.google.com/custom-search/v1/overview
    API_KEY = "AIzaSyCYux7cSQyCqy9jaNi0ZBpvJfjV1sNTZRY"
    # get your Search Engine ID on your CSE control panel
    SEARCH_ENGINE_ID = "3077dc85d6a014700"
    query='python'
    for page in range(1, 11):
        print("[*] Going for page:", page)
        start = (page - 1) * 10 + 1
        
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
        data = requests.get(url).json()
        print(data,'datadatadatadatadatadata')
        print(data,'datadatadatadata')
        search_items = data.get("items")
        print(search_items,'searchsearchsearchsearch')
        
        found = False
        for i, search_item in enumerate(search_items, start=1):
            
            title = search_item.get("title")
            
            snippet = search_item.get("snippet")
            
            html_snippet = search_item.get("htmlSnippet")
            
            link = search_item.get("link")
            
            domain_name = p.urlparse(link).netloc
            if domain_name.endswith(target_domain):
                
                rank = i + start - 1
                print(f"[+] {target_domain} is found on rank #{rank} for keyword: '{query}'")
                print("[+] Title:", title)
                print("[+] Snippet:", snippet)
                print("[+] URL:", link)
                # target domain is found, exit out of the program
                found = True
                break
        if found:
            break
    # rank+1 is due to counting starts from 
    # return render(request, "rank.html",{'result':rank+1})
    # ({"found":print(rank<=10)},{"rank":rank},{"page":link},{"domain":target_domain})
    return JsonResponse({"found" : found, "rank":rank+1, "page":link, "domain":target_domain})


@api_view(['GET',])
def searchapi(query, pages=int(RESULT_COUNT/10)):
    results = []
    query='art forms of himachal pradesh'
    for i in range(0, pages):
        start = i*10+1
        url = SEARCH_URL.format(
            key=SEARCH_KEY,
            cx=SEARCH_ID,
            # query=quote_plus(query),
            query=query,
            start=start
        )
        response = requests.get(url)
        data = response.json()
        results += data["items"]
    res_df = pd.DataFrame.from_dict(results)
    res_df["rank"] = list(range(1, res_df.shape[0] + 1))
    res_df = res_df[["link", "rank", "snippet", "title"]]

    return Response({'data':res_df})


def search_api(request):
    pages=int(RESULT_COUNT/10)
    results = []
    query='python'
    for i in range(0, pages):
        start = i*10+1
        url = SEARCH_URL.format(
            key=SEARCH_KEY,
            cx=SEARCH_ID,
            # query=quote_plus(query),
            query=query,
            start=start
        )
        response = requests.get(url)
        data = response.json()
        results += data["items"]
    res_df = pd.DataFrame.from_dict(results)
    res_df["rank"] = list(range(1, res_df.shape[0] + 1))
    res_df = res_df[["link", "rank", "snippet", "title"]]
    print(res_df, 'resresrresresresresresresresresresr')
    # context={"data":res_df}
    # return render(request,'my_page.html',{'res_df':res_df.to_dict()})
    return res_df

def datasearch(request):
  query='art forms of himachal pradesh'
  df = search_api(query) #returns the dataframe
  context = {
    'df_dict': df.to_dict(),
    'df_rec': df.to_dict(orient='records')
    }
  return render(request, 'my_page.html', context)



# def connect(key):  
#     # scope = ['https://www.googleapis.com/auth/webmasters']

#     scope = ['https://www.googleapis.com/auth/analytics.readonly']
#     credentials = service_account.Credentials.from_service_account_file(key, 
#                                                                         scopes=scope)
#     print(credentials,'creadsfasd')
#     service = build(
#         'webmasters',
#         'v3',
#         credentials=credentials
#     )
#     print(service,'serviceservice')
#     return service


# def query(service, site_url, payload):
#     response = service.searchanalytics().query(siteUrl=site_url, body=payload).execute()
#     print(response,'rrrrrrrrrrrr')
#     results = []
    
#     for row in response['rows']:    
#         data = {}
        
#         for i in range(len(payload['dimensions'])):
#             data[payload['dimensions'][i]] = row['keys'][i]

#         data['clicks'] = row['clicks']
#         data['impressions'] = row['impressions']
#         data['ctr'] = round(row['ctr'] * 100, 2)
#         data['position'] = round(row['position'], 2)        
#         results.append(data)
#         print(result,'rrrrrrrrrrrrrrrrrrrrr')
    
#     return pd.DataFrame.from_dict(results)

# service = connect(key)

# payload = {
#     'startDate': "2019-01-01",
#     'endDate': "2019-12-31",
#     'dimensions': ["page","device","query"],
#     'rowLimit': 100,
#     'startRow': 0
# }

# site_url = "https://data-flair.training/"
# df = query(service, site_url, payload)
# df.head()
# print(df.head())

# @api_view(['GET',])
# def query(service, site_url, payload):
#     site_url='https://www.hptourtravel.com/'
#     payload = {
#     'startDate': "2019-01-01",
#     'endDate': "2019-12-31",
#     'dimensions': ["page","device","query"],
#     'rowLimit': 100,
#     'startRow': 0
#     }
#     response = service.searchanalytics().query(siteUrl='https://www.hptourtravel.com/', body={
#     'startDate': "2019-01-01",
#     'endDate': "2019-12-31",
#     'dimensions': ["page","device","query"],
#     'rowLimit': 100,
#     'startRow': 0
#     }).execute()
    
#     results = []
    
#     for row in response['rows']:    
#         data = {}
        
#         for i in range(len(payload['dimensions'])):
#             data[payload['dimensions'][i]] = row['keys'][i]

#         data['clicks'] = row['clicks']
#         data['impressions'] = row['impressions']
#         data['ctr'] = round(row['ctr'] * 100, 2)
#         data['position'] = round(row['position'], 2)        
#         results.append(data)
    
#     # return pd.DataFrame.from_dict(results)
#     site_url = "https://www.hptourtravel.com/'"

#     df = query(service, site_url, payload)
#     return Response({'data':df.head()})



import pandas as pd
def display_table():
    # do something to create a pandas datatable
    df = pd.DataFrame(data=[[1,2],[3,4]])
    df_html = df.to_html()  # use pandas method to auto generate html
    return render_template('page.html', table_html=df_html)
import json
def datashow(request):
  df = pd.DataFrame({
    'col1': [1,2,3,4],
    'col2': ['A','B', 'C', 'D']
  })
  context = {
        'df_dict': df.to_dict(),
        'df_rec': df.to_dict(orient='records')
        }
  return render(request,'index.html',context)




import pandas as pd

# @api_view(['GET',])
def googlesearch(request):
    data = pd.DataFrame({'Name': ['Marks'], 
                    'Jitender': ['78'],
                    'Rahul': ['77.9']})
    print(type(data))
    print(data.keys())
    context={
        'data_dict':data.to_dict(),
        'data_rec':data.to_dict(orient='record')
    }
    return render(request,'query.html',context)

