import requests
import json

# Change the values in these variables to ones needed for your case
HEADERS = {'Authorization': 'Bearer token'}
user_id = "offending_user_api_id"
domain = "walder.instructure.com"
subject = "Subject line of undesirable message"
url = "https://"+domain+"/api/v1/conversations?"+"as_user_id="+str(user_id)+"&scope=sent&page=1&per_page=100"
# course_id = 93 not used, maybe in a future version
messages = []


# these functions are for pagination
def get_links(url):
    r = requests.get(url, headers=HEADERS)
    return r.headers

def get_next(response_headers):
    CURRENT_LINK = 0
    NEXT_LINK = 1
    
    unparsed_links = response_headers['link']
    
    if "next" in unparsed_links:
        links = unparsed_links.split(',')
        for link in links:
            check = link.split(';')
            if "next" in check[NEXT_LINK]:
                new_url = check[CURRENT_LINK].strip('<>')
                print(new_url)
                break
        return new_url
    else:
        return url


# this finds all the IDs for the messages we'll delete and adds them to a list
while True:
    print(url)
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    links = get_links(url)
    check = get_next(links)
    i = 0
    for each in data:
        beans = data[i]['subject']
        if beans == subject:
            message_id = data[i]['id']
            print(message_id)
            messages.append(message_id)
            i += 1
        else:
            i += 1
    if check == url:
        print(check)
        print(len(messages))
        break
    else:
        url = check


# this kills the messages
j = 0
for each in messages:
    url = "https://"+domain+"/api/v1/conversations/"+str(messages[j])+"/delete_for_all"
    r = requests.delete(url, headers=headers)
    print(messages[j], r.status_code)
    j += 1

# find a good value to limit this so we don't keep pulling messages when all the unwanted messages have been deleted