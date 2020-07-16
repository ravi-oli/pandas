### Connect to VM via SSH keys
Reference: https://medium.com/@souvikhaldar/how-to-add-the-public-ssh-key-to-a-gcp-virtual-machine-ef5703e8e596

```bash
# generate key
ssh-keygen

# provide key name / path, pandas in my case
# 2 keys get created, pandas and pandas.pub

# Add public key to VM console
cat pandas.pub

# Login to instance
ssh -i pandas username@ip-address-of-instance
```


### Configure virtual environment
Reference: https://www.tensorflow.org/install/pip (Check section 2 for example on how to create a virtual environment. Options for both Ubuntu, Mac are present)

```bash
# Activate environment
source ./venv_pandas/bin/activate

# Install flask
pip install flask

# List of installed packages
pip freeze

# Output to requirements file
pip freeze > requirements.txt
```

### Basic Flask API
Reference: Github repository, https://github.com/ravi-oli/pandas
File: app.py

```bash
# Start flask server
python3 app.py

# Access APIs
# Visit: http://127.0.0.1:8001/apiname?paramname1=paramvalue1&paramname2=paramvalue2
```

### Git commands
Refer attached slides

### Upload files to remote server using ```scp```

If you do want to use git and upload files directly

```bash

scp -i pandas workspaces/pandas/app.py username@ip-address-of-instance:~

# you will see app.py in home folder of instance

# create virtual environment as you'd do in the local machine

# install flask as deployed on local machine in the activated virtual environment

# start server on port 80
sudo ./venv_pandas/bin/python3.6 app.py

# Visit: http://public-ip-address/apiname?paramname1=paramvalue1&paramname2=paramvalue2
```

