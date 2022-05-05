# PyCSRAPI
python Flask app (api) to generate the certificate signing request

Internally, this will call up openssl shell command, generate signing request and then read csr & key.
Afterwards, deletes both .key & .csr files from physical disk, returns it back to response. 

[![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Usage : (Flask will run on 11055, change it in main .py file)

curl --request POST \
  --url http://192.168.100.163:11055/generate \
  --header 'Content-Type: application/json' \
  --data '{
	"commonname": "testing123.com",
	"country": "IN",
	"state": "GJ",
	"locality": "AMD",
	"organization": "tj org",
	"organizationunit": "IT",
	"keysize": "4096"
}'

Response :

{
	"csr": "",
	"key": "",
	"error": ""
}


To Do:
Will add one Nice GUI at /gui path. WIP.
