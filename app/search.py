from google.oauth2 import service_account
from googleapiclient.discovery import build
import requests
import json
import pandas as pd
pd.set_option('max_colwidth', 150)
from rest_framework import *
from rest_framework.decorators import api_view
key = {
    "type": "service_account",
    "project_id": "x-pulsar-376705",
    "private_key_id": "d3f35a642e9e0aa07f00dbea401c9b22ff80e479",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDDn/+LlDXvP7sK\nOonmcqfW3pF3aT/FESav1+JQao3flEQAlupz2MKnzXIeiK+RPQPCr9lgKIlcIR3z\nsEP66pGRbTuCpfZ78VUjigPt2gIFewGh/W2KsJBLMpXKpOLD1AFLMujWFFSfu93V\nL+SD5ckvjC/t/pGWXeooUSxRBuksrwNsjaY1CW31w8b0uADTTEKqaGbMWgD+q2EB\n1RiqcfQGLjRXH4TJzWA3s+ZkcdFhQBuFnFoXgBayosTV9Fq+l1nJxJj95aaJIi+b\na48inDiw9pIHPEPQg6vhURkSku/2C+5pE6N2GoAA22I3wH60YkezD5k3DIhpHdKP\nJPWRWKwvAgMBAAECggEAGsyGY4awRNBEPUh7r7gxSfw/jU470DFjTV+Tv1R5jxFu\np24FPE2LjRVV9tzewFTNeRRCASxMdPSMd9/D0FHmEzgVmPZHZ/9NnIrBswnUkQ+i\nz6A6K2+4tLR/VL1120Hl03lr8Dfkx+UipJvlADSwdPUNc9sV8rV26IMGQStjMh2i\nDQJflI3uUGYo92jYdKGEWHmJkA9rT2ZwW28imBlmnkV9S9/k6i+ug0WcGmNAk3cG\nsANqUTAf5lXREo/L2uO/L8mepEY8DCWYjoO0NIY+qZB1tyqGDtF0rgU+O0jeQBKP\njHN4euQRrIxhvy/aaKZp8Lm022BwTk9YTLfU0eDOgQKBgQD2wPpI1QiCh77w/iK9\n59sTF9M8mBqAj70+a8FPJKp+MNQOWFwuiBFra1nSPkBKWoMkRoXQdTjjCUuHjQLM\nu4UUp2hzJqYHnbapjhVJj3AQyikXZ1uupESgAG2vUDLl6Xg6hEFTzFHxlb0KCyAG\nii1p9xniHpjP+0y5N+A9f67CjwKBgQDK9I9MhnRgjnRYHTJSN9xfBTZ/MA6W4Q0N\nJbBi1iHUZUnZxDfSv0siZMj1o533wDSbWB7atf9QrP+pK/LMJz0Ym8AMlI61uFU0\nnNAQTdAxQnjemxSAJe4UnmVCZQumkKGg3+NWCkJ3ebdXyZSBRml8hojNlz76ckZj\niGxPUPnMYQKBgHhaBXlSlrT7urDWc2GG3b6BR2FtmreL5DS23/FXI+UqsbNRe5yi\nd0SadpPqEvdxEDe4Qfo7woRR+0nhCDWNXMqHIJXRivd6ACbRCyb21CUMRWCJ5BjZ\nPDOCIf15M2oaJq775NUXefxIGYz1gihOavodML2uSMBghLpuO2wjg7yXAoGBAK/W\nKsEWTIXLZilhQlPRafA5R/nx3PIDkZcubB91fmHST6WIRwUkDyiBQUrwstAPioR8\nWF8NB2MSP36GQRl3dYt4hW9g1jPCvK+UnP9DK3lCKg5TNfPA6QCcKwbXHLz22dHT\np9bHlMaGgb5hO3S1WHc26BeXTk0V7L4XWB9v/LyBAoGAeMS+hrvdjMa7n2iTUJTm\nqW/7Dc1pa0TStucYMHnZdqYamZu/wDCz0b8LEo6aHsc0ZsN5sD8m4myTQNIRsiad\nxEjppIjr9584JbGSipceHIFWvY+LKVeGT/OZ1mlXkGfDDd6YUrFFbQL+z5mqiCDa\n25FY5bkDAgxTGB287W2r1hU=\n-----END PRIVATE KEY-----\n",
    "client_email": "indexing-project-tutorial@x-pulsar-376705.iam.gserviceaccount.com",
    "client_id": "111536783541950548658",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/indexing-project-tutorial%40x-pulsar-376705.iam.gserviceaccount.com"
  }

# @api_view(['GET',])
def connect(key):  
    # scope = ['https://www.googleapis.com/auth/webmasters']
    scope = ['https://www.googleapis.com/auth/analytics.readonly']
    credentials = service_account.Credentials.from_service_account_file(key, 
                                                                        scopes=scope)
    print(credentials,'creadsfasd')
    service = build(
        'webmasters',
        'v3',
        credentials=credentials
    )
    print(service,'serviceservice')
    return Response({'data':service})

# @api_view(['GET',])
# def connect(request):
#         key = {
#         "type": "service_account",
#         "project_id": "x-pulsar-376705",
#         "private_key_id": "d3f35a642e9e0aa07f00dbea401c9b22ff80e479",
#         "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDDn/+LlDXvP7sK\nOonmcqfW3pF3aT/FESav1+JQao3flEQAlupz2MKnzXIeiK+RPQPCr9lgKIlcIR3z\nsEP66pGRbTuCpfZ78VUjigPt2gIFewGh/W2KsJBLMpXKpOLD1AFLMujWFFSfu93V\nL+SD5ckvjC/t/pGWXeooUSxRBuksrwNsjaY1CW31w8b0uADTTEKqaGbMWgD+q2EB\n1RiqcfQGLjRXH4TJzWA3s+ZkcdFhQBuFnFoXgBayosTV9Fq+l1nJxJj95aaJIi+b\na48inDiw9pIHPEPQg6vhURkSku/2C+5pE6N2GoAA22I3wH60YkezD5k3DIhpHdKP\nJPWRWKwvAgMBAAECggEAGsyGY4awRNBEPUh7r7gxSfw/jU470DFjTV+Tv1R5jxFu\np24FPE2LjRVV9tzewFTNeRRCASxMdPSMd9/D0FHmEzgVmPZHZ/9NnIrBswnUkQ+i\nz6A6K2+4tLR/VL1120Hl03lr8Dfkx+UipJvlADSwdPUNc9sV8rV26IMGQStjMh2i\nDQJflI3uUGYo92jYdKGEWHmJkA9rT2ZwW28imBlmnkV9S9/k6i+ug0WcGmNAk3cG\nsANqUTAf5lXREo/L2uO/L8mepEY8DCWYjoO0NIY+qZB1tyqGDtF0rgU+O0jeQBKP\njHN4euQRrIxhvy/aaKZp8Lm022BwTk9YTLfU0eDOgQKBgQD2wPpI1QiCh77w/iK9\n59sTF9M8mBqAj70+a8FPJKp+MNQOWFwuiBFra1nSPkBKWoMkRoXQdTjjCUuHjQLM\nu4UUp2hzJqYHnbapjhVJj3AQyikXZ1uupESgAG2vUDLl6Xg6hEFTzFHxlb0KCyAG\nii1p9xniHpjP+0y5N+A9f67CjwKBgQDK9I9MhnRgjnRYHTJSN9xfBTZ/MA6W4Q0N\nJbBi1iHUZUnZxDfSv0siZMj1o533wDSbWB7atf9QrP+pK/LMJz0Ym8AMlI61uFU0\nnNAQTdAxQnjemxSAJe4UnmVCZQumkKGg3+NWCkJ3ebdXyZSBRml8hojNlz76ckZj\niGxPUPnMYQKBgHhaBXlSlrT7urDWc2GG3b6BR2FtmreL5DS23/FXI+UqsbNRe5yi\nd0SadpPqEvdxEDe4Qfo7woRR+0nhCDWNXMqHIJXRivd6ACbRCyb21CUMRWCJ5BjZ\nPDOCIf15M2oaJq775NUXefxIGYz1gihOavodML2uSMBghLpuO2wjg7yXAoGBAK/W\nKsEWTIXLZilhQlPRafA5R/nx3PIDkZcubB91fmHST6WIRwUkDyiBQUrwstAPioR8\nWF8NB2MSP36GQRl3dYt4hW9g1jPCvK+UnP9DK3lCKg5TNfPA6QCcKwbXHLz22dHT\np9bHlMaGgb5hO3S1WHc26BeXTk0V7L4XWB9v/LyBAoGAeMS+hrvdjMa7n2iTUJTm\nqW/7Dc1pa0TStucYMHnZdqYamZu/wDCz0b8LEo6aHsc0ZsN5sD8m4myTQNIRsiad\nxEjppIjr9584JbGSipceHIFWvY+LKVeGT/OZ1mlXkGfDDd6YUrFFbQL+z5mqiCDa\n25FY5bkDAgxTGB287W2r1hU=\n-----END PRIVATE KEY-----\n",
#         "client_email": "indexing-project-tutorial@x-pulsar-376705.iam.gserviceaccount.com",
#         "client_id": "111536783541950548658",
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://oauth2.googleapis.com/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/indexing-project-tutorial%40x-pulsar-376705.iam.gserviceaccount.com"
#         }
#         scope = ['https://www.googleapis.com/auth/analytics.readonly']
#         credentials=service_account.Credentials.from_service_account_file(key,scopes=scope)
#         service = build(
#         'webmasters',
#         'v3',
#         credentials=credentials)
#         return Response({'data':service})

@api_view(['GET',])
def query(request):
    payload = {'startDate': "2019-01-01",'endDate': "2019-12-31",'dimensions': ["page","device","query"],'rowLimit': 100,'startRow': 0}
    site_url = "https://data-flair.training/"
    response = service.searchanalytics().query(siteUrl=site_url, body=payload).execute()
    print(response,'rrrrrrrrrrrr')
    results = []
    for row in response['rows']:    
        data = {}
        for i in range(len(payload['dimensions'])):
            data[payload['dimensions'][i]] = row['keys'][i]

        data['clicks'] = row['clicks']
        data['impressions'] = row['impressions']
        data['ctr'] = round(row['ctr'] * 100, 2)
        data['position'] = round(row['position'], 2)        
        results.append(data)
        print(result,'rrrrrrrrrrrrrrrrrrrrr')
    service = connect(key)
    df = query(service, site_url, payload)
    return Response({'data':df.head()})

def querydata(request):
    payload = {'startDate': "2019-01-01",'endDate': "2019-12-31",'dimensions': ["page","device","query"],'rowLimit': 100,'startRow': 0}
    site_url="https://data-flair.training/"
    response=service.searchanalytics().query(siteUrl=site_url, body=payload).execute()
    results=[]
    for row in response['rows']:
        data={}
        for i in range(len(payload['dimensions'])):
            data[payload['dimensions'][i]]=rows['keys'][i]
        data['clicks']=row['clicks']
        data['imperessions']=row['impressions']
        data['ctr']=round(row['ctr'] * 100,2)
        data['position']=round(row['position'], 2)
        results.append(data)
    service=connect(key)
    df=query(service,site_url,payload)
    return render(request,'query.html',{'df':df})

def dataquery(request):
    payload = {'startDate': "2019-01-01",'endDate': "2019-12-31",'dimensions': ["page","device","query"],'rowLimit': 100,'startRow': 0}
    site_url="https://data-flair.training/"
    service=connect(key)  
    df=query(service,site_url,payload)  
    data=querydata(df)
    context={
        'df_dict':data.to_dict(),
        'df_rec':data.to_dict(orient='records')
    }
    return render(request,'query.html',context)


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
