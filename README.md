# PyCSRAPI
Python Flask app (api) to generate the certificate signing request.

Internally, this will call up openssl shell command, generate signing request and then read csr & key.
Afterwards, deletes both .key & .csr files from physical disk, returns it back to response. 

## Deploy on Heroku
[![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)



## Getting Started

Python Flask app (api) to generate the certificate signing request.

Supports AMD and ARM architectures.

### Prerequisities


In order to run this you'll need one of the following OS/docker installed:

* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

### 1 - Manual (via CLI)

```bash
$ python app_api1.py
```

(Flask will run on 11055, change it in main .py file)

```
curl --request POST \
  --url http://127.0.0.1:11055/generate \
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
```

Response :

```json
{
	"csr": "",
	"key": "",
	"error": ""
}
```

### 2 - Docker (via CLI)


```bash
$ docker run -p 11055:11055 -d tjhackz/pycsrapi
```

### 3 - Docker Compose 

```yml
version: '3.3'
services:
    pycsrapi:
        ports:
            - '11055:11055'
        restart: always
        image: tjhackz/pycsrapi
```

### Docker Hub URL : https://hub.docker.com/r/tjhackz/pycsrapi
### GitHub URL : https://github.com/tjhackzy/PyCSRAPI




To Do:
Will add one Nice GUI at /gui path. 
WIP.
