from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import urllib.parse as p

# Create your views here.

data = {}

# Request the home page

def home(request):
    return render(request, 'home.html',{'name':'Google page ranking by keywords'})

# Now the algorithm

def add(request):
    target_domain = request.GET['website']
    query = request.GET['keywords']
    # get the API KEY here: https://developers.google.com/custom-search/v1/overview
    API_KEY = "<Put_your_API_KEY_here>"
    # get your Search Engine ID on your CSE control panel
    SEARCH_ENGINE_ID = "<Put_your_Search_Engine_ID_here>"

    for page in range(1, 11):
        print("[*] Going for page:", page)
        start = (page - 1) * 10 + 1
        
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
        data = requests.get(url).json()
        search_items = data.get("items")
        
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





from django.shortcuts import render
from .models import *
from django.conf import settings
import requests
from requests.exceptions import RequestException
import pandas as pd
from datetime import datetime
from urllib.parse import quote_plus
# Create your views here.
SEARCH_KEY="AIzaSyARR4HswyX5E99s1HABHDjI25qRmWrwfes"
SEARCH_ID="3077dc85d6a014700"
COUNTRY="in"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT=20


def search_api(query, pages=int(RESULT_COUNT/10)):
    results = []
    for i in range(0, pages):
        start = i*10+1
        url = SEARCH_URL.format(
            key=SEARCH_KEY,
            cx=SEARCH_ID,
            query=quote_plus(query),
            start=start
        )
        response = requests.get(url)
        data = response.json()
        results += data["items"]
    res_df = pd.DataFrame.from_dict(results)
    res_df["rank"] = list(range(1, res_df.shape[0] + 1))
    res_df = res_df[["link", "rank", "snippet", "title"]]
    return res_df



def scrape_page(links):
    html = []
    for link in links:
        print(link)
        try:
            data = requests.get(link, timeout=5)
            html.append(data.text)
        except RequestException:
            html.append("")
    return html

def search(query):
    columns = ["query", "rank", "link", "title", "snippet", "html", "created"]
    storage = DBSStorage()

    stored_results = storage.query_results(query)
    if stored_results.shape[0] > 0:
        stored_results["created"] = pd.to_datetime(stored_results["created"])
        return stored_results[columns]

    print("No results in database.  Using the API.")
    results = search_api(query)
    html = scrape_page(results["link"])
    results["html"] = html
    results = results[results["html"].str.len() > 0].copy()
    results["query"] = query
    results["created"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    results = results[columns]
    results.apply(lambda x: storage.insert_row(x), axis=1)
    print(f"Inserted {results.shape[0]} records.")
    return results

from django.db.models import Q

def index(request):
    search_post=request.GET.get('search')
    if search_post:
        posts=Post.objects.filter(Q(title__icontains=search_post) | Q(content__icontains=search_post))
    else:
        posts=Post.objects.all().order_by('title')
    return render(request,'index.html',{'posts':posts})


# "app.py"



import html



styles = """
<style>
    .site {
        font-size: .8rem;
        color: green;
    }
    
    .snippet {
        font-size: .9rem;
        color: gray;
        margin-bottom: 30px;
    }
    
    .rel-button {
        cursor: pointer;
        color: blue;
    }
</style>
<script>
const relevant = function(query, link){
    fetch("/relevant", {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
           "query": query,
           "link": link
          })
        });
}
</script>
"""

search_template = styles + """
     <form action="/" method="post">
      <input type="text" name="query">
      <input type="submit" value="Search">
    </form> 
    """

result_template = """
<p class="site">{rank}: {link} <span class="rel-button" onclick='relevant("{query}", "{link}");'>Relevant</span></p>
<a href="{link}">{title}</a>
<p class="snippet">{snippet}</p>
"""

def show_search_form():
    return search_template


def show_search(request):
    query=request.GET.get('q')
    data=DBSStorage.objects.filter(query=query)
    return render(request, 'search_template.html',{'data':data})



def run_search(query):
    results = search(query)
    fi = Filter(results)
    filtered = fi.filter()
    rendered = search_template
    filtered["snippet"] = filtered["snippet"].apply(lambda x: html.escape(x))
    for index, row in filtered.iterrows():
        rendered += result_template.format(**row)
    return rendered

# def search_form():
#     if request.method == 'POST':
#         query = request.form["query"]
#         return run_search(query)
#     else:
#         return show_search_form()

# def mark_relevant():
#     data = request.get_json()
#     query = data["query"]
#     link = data["link"]
#     storage = DBStorage()
#     storage.update_relevance(query, link, 10)
#     return jsonify(success=True)




