import os
import subprocess
import uuid
import shutil
import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def generatecsrfn(country, state, location, org, orgunit, commonname, keysize):
    #res1 = os.system("openssl req -new -newkey rsa:2048 -nodes -out jayv123_com.csr -keyout jayv123_com.key -subj ""/C=IN/ST=Gujarat/L=Ahmedabad/O=Ttest org/OU=IT/CN=jayv123.com""")
    #print(res1)

    #print(orgunit)
    dirname=str(uuid.uuid4())
    algo_size = "rsa:"+ str(keysize)
    #f_prm = "/C="+country+"/ST="+state+"/L="+location+"/O="+org+"/OU="+orgunit+"/CN=" + commonname
    
    f_prm_2 = "/C="+country+"/ST="+state+"/L="+location+"/O="+org+"/CN=" + commonname
    
    #print(f_prm_2)
    
    if (orgunit):
        f_prm_2 = f_prm_2 + "/OU="+ str(orgunit)
    
    #print(f_prm_2)
    subprocess.run(["mkdir",dirname])
    #res2 = subprocess.run(["pwd"])
    #strdir = res2 + "/" + dirname
    res2 = os.getcwd()
    strdir = os.path.join(res2, dirname)
    os.chdir(strdir)
    
    
    result_final = subprocess.run(["openssl","req","-new", "-newkey", algo_size,"-nodes","-out", "mycsr.csr", "-keyout" ,"mykey.key", "-subj",f_prm_2], capture_output=True, text=True)
    #print("stdout:", result_final.stdout)
    #print("stderr:", result_final.stderr)
    test_csr_path = os.path.join(strdir, "mycsr.csr")
    test_key_path = os.path.join(strdir, "mykey.key")
    
    test_csr = open(test_csr_path,"r")
    test_key = open(test_key_path,"r")
    
    data_csr = test_csr.read()
    data_key = test_key.read()
    
    test_csr.close()
    test_key.close()
    
    #print(data_csr)
    #print(data_key)
    
    f_result = { "csr" : data_csr, "key" : data_key }
    
    #print(json.dumps(f_result))
    
    path_parent = os.path.dirname(os.getcwd())

    os.chdir(path_parent)
    
    shutil.rmtree(strdir, ignore_errors=True)
    return data_csr, data_key
    
    
    


@app.route('/', methods=['GET'])
@cross_origin()
def welcome():    
    return """<p>

<HTML>
<TITLE>CSR API Generator</TITLE>
<head>
<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>
</head>
<BODY>
<p>
CSR Generator API is working...</p>
<br/>
<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/tjhackzy" data-size="large" aria-label="Follow @tjhackzy on GitHub">Follow @tjhackzy</a>

<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/tjhackzy/PyCSRAPI/fork" data-icon="octicon-repo-forked" data-size="large" aria-label="Fork tjhackzy/PyCSRAPI on GitHub">Fork</a>

<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/tjhackzy/PyCSRAPI/archive/HEAD.zip" data-icon="octicon-download" data-size="large" aria-label="Download tjhackzy/PyCSRAPI on GitHub">Download</a>

</BODY></HTML>
"""
    

@app.route('/generate', methods=['POST'])
@cross_origin()
def generatecsr():
    if (is_json(request.data) is False):
        f_result = { "csr" : "", "key" : "" , "error":"Missing Json in Request." }
        response_final = json.dumps(f_result)
        return response_final,400

    ret_obj = request.get_json()
    commonname = ret_obj.get("commonname")
    
    if(commonname is None):
        f_result = { "csr" : "", "key" : "" , "error":"Common name is a required field." }
        response_final = json.dumps(f_result)        
        return response_final,400
    
    country = ret_obj.get("country")
    if(country is None):
        f_result = { "csr" : "", "key" : "" , "error":"Country is a required field." }
        response_final = json.dumps(f_result)        
        return response_final,400
    
    state = ret_obj.get("state")
    if(state is None):
        f_result = { "csr" : "", "key" : "" , "error":"State is a required field." }
        response_final = json.dumps(f_result)        
        return response_final,400
    
    locality = ret_obj.get("locality")
    if(locality is None):
        f_result = { "csr" : "", "key" : "" , "error":"Locality is a required field." }
        response_final = json.dumps(f_result)        
        return response_final,400
    
    organization = ret_obj.get("organization")
    if(organization is None):
        f_result = { "csr" : "", "key" : "" , "error":"Organization is a required field." }
        response_final = json.dumps(f_result)        
        return response_final,400
    
    organizationunit=ret_obj.get("organizationunit")
    #print(organizationunit)
    keysize = ret_obj.get("keysize")
    final_result_json = generatecsrfn(country,state,locality,organization, organizationunit, commonname, keysize)
    f_result = { "csr" : final_result_json[0], "key" : final_result_json[1] , "error":"" }
    response_final = json.dumps(f_result)    
    return response_final
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11055)
    
 
