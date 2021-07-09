# html_structure
This  flask app will show you html structure

To run the application without docker just download repo and run "flask run",
if you want to run with docker go to app directory in terminal and run "docker-compose up"

use postman for checking url

 - localhost/login [Get]   -  you  will get auth code for login
 - localhost/login [Post]  -  you will login you have to Post this json file{ "code": "QWDCR4", "number_phone" = "+71111111111" } 
 - localhost/structure?link=your url&tags=tags you want to count[Get]   -  you will get tags count of the website you want. 
for example( localhost/structure?link=https://www.google.az/&tags=html, body, div )
 -  localhost/check_structure[Post]  - you can check equality of your html structure with real structure you shave to post json file like this
html_structure = {
  "link": "https://freestylo.ru/", 
  "structure": {"html": 1, "head": 1, "body": 1, "p": 10, "img": 2}
  }

## Note:This app will not show full structure of website, for this i can use selenium and webdriver, i couldnt use because of lack of time
