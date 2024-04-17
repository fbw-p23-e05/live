# EC2 Environment Setup

Once you are logged into your server, we will install all of the project dependencies: We will install the following:

* Django and Python3
* pip
* gunicorn
* NGINX
* UFW (Firewall)

## Firewall Setup

#### Enable Firewall and allow OpenSSH

```shell
% sudo ufw enable
% sudo ufw allow OpenSSH
% sudo ufw allow 'Nginx Full'
```

**Check to make sure we are allowing OpenSSH**

```shell
% sudo ufw status
```

Expected output:

```shell
To                         Action      From
--                         ------      ----
Nginx Full                 ALLOW       Anywhere
OpenSSH                    ALLOW       Anywhere
Nginx Full (v6)            ALLOW       Anywhere (v6)
OpenSSH (v6)               ALLOW       Anywhere (v6)
```

## Installing Dependencies

##### Updating packages:

```shell
% sudo apt update
% sudo apt upgrade
```

##### Installing Python 3, PostgreSQL, NGINX and Gunicorn:

```shell
% sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx gunicorn curl
```

## Setting up the Project on the Remote Server

```shell
% git clone https://github.com/<YOUR GITHUB USERNAME>/<YOUR REPOSITORY>.git
% python3 -m venv env
% source env/bin/activate
% pip3 install -r requirements.txt
% python3 manage.py makemigrations
% python3 manage.py migrate
% python3 manage.py collectstatic
```

Note: Make sure to update your .env file so that your project has the correct Environment Varialbes necessary to run.

## Configuring Gunicorn

Create a gunicorn.socket file:

```shell 
% sudo nano /etc/systemd/system/gunicorn.socket
```

Configure the gunicorn.socket file with:

```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

Next configure the gunicorn.service file with:

```shell
% sudo nano /etc/systemd/system/gunicorn.service
```

Use the configurations below:

```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=djangoadmin
Group=www-data
WorkingDirectory=/home/ubuntu/<YOUR-PROJECT>
ExecStart=/home/djangoadmin/pyapps/venv/bin/gunicorn \
--access-logfile - \
--workers 3 \
--bind unix:/run/gunicorn.sock \
<YOUR-PROJECT>.wsgi:application

[Install]
WantedBy=multi-user.target
```

##### Start and enable Gunicorn:

```shell
% sudo systemctl start gunicorn.socket
% sudo systemctl enable gunicorn.socket
```

**Check the status of gunicorn with:**

```shell
% sudo systemctl status gunicorn.socket
```

## Configuring NGINX

Next, we need to configure NGINX to redirect web traffic.

Create a new NGINX config file with the following command:

```shell
% sudo nano /etc/nginx/sites-available/<YOUR-PROJECT-NAME>
```

Paste in the following configurations and replace any of the ALL CAPS sections with your own project details:

```
server {
listen 80;
server_name YOUR_INSTANCE_IP_ADDRESS;

location = /favicon.ico { access_log off; log_not_found off; }
location /static/ {
root /home/ubuntu/<YOUR-PROJECT>;
}

location /media/ {
root /home/ubuntu/<YOUR-PROJECT>;    
}

location / {
include proxy_params;
proxy_pass http://unix:/run/gunicorn.sock;
}
}
```

Once your NGINX config is set up, make sure there are no syntax errors with:
```shell
% sudo nginx -t
```

Next, create a symbolic link of your config file from sites-available to the sites-enabled directory. This step is important because NGINX will use the configuration settings located at /etc/nginx/sites-available/default by default if there is nothing in sites-enabled.

```shell
% sudo ln -s /etc/nginx/sites-available/<YOUR-PROJECT-NAME> /etc/nginx/sites-enabled
```

Restart the NGINX Web Server with:

```shell
% sudo systemctl restart nginx
```

Now if you go to your Public IP on your browser it should show the app!

## Setting up Continuous Deployment

Continuous Deployment is helpful because it saves you the time of having to ssh into your EC2 instance each time you make an update on your codebase.

In this project, we will be using a Github Action called AWS SSM Send-Command created by peterkimzz to implement auto-deployment.

### Github Actions

Github Actions is a service by Github that allows you to perform actions such as run scripts every time something happens to a repository. In our case, we will run a script to install the latest dependencies and restart our server every time a push is made to master.

For Github Actions to work, it needs a way to communicate with the EC2 Instance and vice-versa. In order to do that, we need to assign permissions via IAM roles.

#### Create SSM Role

To create an IAM Role with AmazonSSMFullAccess permissions:

* Open the IAM console at https://console.aws.amazon.com/iam/.
* In the navigation panel, select Roles, and then click Create role.
* Under Select type of trusted entity, choose AWS service.
* In the Choose a use case section, choose EC2, and then choose Next: Permissions.
* On the Attached permissions policy page, search for the AmazonSSMFullAccess policy, choose it, and then choose Next: Review.
* On the Review page, type a name in the Role name box, and then type a description.
* Choose Create role. The system returns you to the Roles page.

#### Assigning an SSM Role to EC2 Instance

Once you have the Role created:

* Go to the EC2 Instance Dashboard
* Go to the Instances link
* Highlight the Instance
* Click on Actions
* Security
* Modify IAM Role
* Select the SSM Role you had created earlier
* Hit Apply to save changes

#### Github Secrets

With our instance being able to use the SSM Agent, we will need to provide it some details so that it can access our EC2 instance.

Now that the instance is able to communicate to Github via SSM Agent, you will need to provide the repo with credentials. Github Secrets act like environment variables for repositories and store sensitive data such as AWS login information. In order for the Github Actions script to work, it needs these three secrets: AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, and INSTANCE_ID.

There is an article by AWS on how to find your AWS Access Key and Secret Access Key here. Your instance ID is shown on your instances tab under EC2.

Start by going to your Github project repo:

* Then go to your **Settings**
* On the menu on the left, look for the link for Secrets
* There, add the three Secrets with these keys:
  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`
  * `INSTANCE_ID`

Once these **Secrets** are set, we are ready to move on!

#### _Deployment script_

Next, let's create a bash script to download dependencies and restart NGINX and PM2. Inside the EC2 instance, create a deploy.sh script in the root of the directory:

```shell
% sudo nano deploy.sh
```

Fill the contents with the bash commands we ran to build the project earlier:
```shell
#!/bin/bash     
sudo git pull origin master
sudo pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
sudo systemctl restart nginx
sudo systemctl restart gunicorn
```

#### YAML File

AWS SSM Send-Command requires a .yml file to execute. At the root of the project, create these two directories:

```shell
% mkdir -p .github/workflows/
```

Create a new YAML file with:

```shell
% sudo nano .github/workflows/deploy.yml
```

Paste in the following:
```
name: Deploy using AWS SSM Send-Command 

on:
 push:
  branches: [master]

jobs:
 start:
  runs-on: ubuntu-latest 

  steps:
  - uses: actions/checkout@v2

  - name: AWS SSM Send Command
    uses: peterkimzz/aws-ssm-send-command@1.0.1
    with:
     aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID  }}
     aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY  }}
     aws-region: <YOUR EC2 REGION>
     instance-ids: ${{ secrets.INSTANCE_ID  }}
     comment: Deploy the master branch
     working-directory: /home/ubuntu/<YOUR PROJECT DIRECTORY>
     command: /bin/bash ./deploy.sh
```

The Secrets we provided to the repo earlier comes into use in this script.

There are 3 parts of the .yml file to configure:

1. The aws-region should be the same region as where you have created your EC2 instance. (If you do not know, check the top left of your EC2 console to confirm the region you are in).
2. working-directory should be the directory where you created the deploy.sh script.
3. command should be the command you would like the SSM agent to run.

Once this is complete, commit and push the workflow to your repo.

---
