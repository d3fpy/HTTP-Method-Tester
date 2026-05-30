import requests

BASE_URL = '_URL'

#req = requests

def main():
    
    for i in range(2):
        DELETE_request = requests.delete(BASE_URL)
        GET_request = requests.get(BASE_URL)
        POST_request = requests.post(BASE_URL)
        print(DELETE_request.text,
              GET_request.text,
              POST_request.text, 
              sep='\n')

if __name__ == '__main__':
    main()