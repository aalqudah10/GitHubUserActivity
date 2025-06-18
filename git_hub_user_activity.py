import argparse
import requests 
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help='GitHub username')
    
    args = parser.parse_args()

    #URL to the GET request
    url = f'https://api.github.com/users/{args.username}/events'
    response = requests.get(url)

    #Split output based on status code
    code = response.status_code

    #The request was valid
    if code == 200:
        for item in response.json():
            event = item['type']
            #user = item['actor']['login']
            repository = item['repo']['name']

            #Different types of activities a user can do
            if event == 'CreateEvent':
                print(f'- Created a repo called {repository}')
            elif event == 'PushEvent':
                print(f"- Pushed {len(item['payload']['commits'])} commit(s) to {repository}")
            elif event == 'DeleteEvent':
                print(f"- Deleted {item['payload']['ref']} {item['payload']['ref_type']} in {repository}")
            elif event == 'ForkEvent':
                print(f"- Forked {item['payload']['forkee']['full_name']} in {repository}")
            elif event == 'IssueCommentEvent':
                print(f"- Commented on ({item['payload']['issue']['title']}) in {repository}")
            elif event == 'IssuesEvent':
                print(f"- {item['payload']['action'].capitalize()} a new issue on ({item['payload']['issue']['title']}) in {repository}")
            elif event == 'MemberEvent':
                print(f"- {item['payload']['action'].capitalize()} ({item['payload']['member']}) to {repository}")
            elif event == 'PublicEvent':
                print(f'Made {repository} public')
            elif event == 'PullRequestEvent':
                print(f"- {item['payload']['action'].capitalize()} a pull request in {repository}")
            elif event == 'PullRequestReviewEvent':
                print(f"- Reviewed ({item['payload']['action'].capitalize()} a pull request) in {repository}")
            elif event == 'PullRequestReviewCommentEvent':
                print(f"- Commented on ({item['payload']['action'].capitalize()} a pull request) review in {repository}")
            else:
                print(f'{event} event was made in {repository}')

    #No Username Found Error
    elif code == 404:
        print(f"Username:{args.username} is Invalid")

    #Server/API Error
    elif str(code)[0] == '5':
        print(f'An error occured while fetching {args.username} events')




if __name__ == "__main__":
    main()
