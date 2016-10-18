"change"
import adal
import requests
 
def get_token() :
        context = adal.AuthenticationContext('https://login.microsoftonline.com/TENANT.onmicrosoft.com')
        token_response = context.acquire_token_with_client_credentials(
        "https://management.azure.com/",
        "SERVICE_PRINCIPAL_NAME",
         "SERVICE_PRINCIPAL_PASSWORD")
        access_token = token_response.get('accessToken')
 
        print(access_token)
 
        return access_token
 
 
def make_ARM_request() :
        tokenHeader = 'Bearer ' + get_token()
 
        headers = {'Content-Type':'application/json','Authorization':tokenHeader}
 
        payload = {'api-version': '2015-01-01'}
 
        url="https://management.azure.com/subscriptions/SUBSCRIPTION_ID/resourcegroups"
 
        resp = requests.get(url,params=payload,headers=headers)
        if resp.status_code != 200:
                print('oops {}'.format(resp.status_code))
        print(resp.text)
 
print(make_ARM_request())
