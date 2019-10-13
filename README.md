# flask-to-web
<img width="440" alt="Screen Shot 2019-10-13 at 3 45 27 PM" src="https://user-images.githubusercontent.com/6750179/66723659-8c0aa880-edd0-11e9-8352-6e3319065fb0.png">
Project to experiment with deploying a simple web app on the web using `flask`, `gunicorn` and hosted by `heroku`. Flask makes it very easy to build a REST API. Gunicorn makes it very easy to build a production scale server. Heroku makes it trivial to run a web app, on-demand on the web.

## Deploy steps
Initial steps from [Heroku Python help page](https://devcenter.heroku.com/articles/getting-started-with-python)
1. Sign up for Heroku account
2. Install Heroku client (requires GIT) by running `brew install heroku/brew/heroku`
3. login with `heroku login`
4. Create a Heroku app by `heroku create` from your repo dir.
Heroku gives it a custom name. But it adds a new git remote. For instance see

```
(flask) python-getting-started (master) $ git remote -v
heroku	https://git.heroku.com/whispering-inlet-42900.git (fetch)
heroku	https://git.heroku.com/whispering-inlet-42900.git (push)
origin	git@github.com:heroku/python-getting-started.git (fetch)
origin	git@github.com:heroku/python-getting-started.git (push)
(flask) python-getting-started (master) $ 
```
This name is seen in the URL of the app. So, if you 
want to customize the name, use `heroku apps:create <name>`

5. Now push this repo to Heroku remote using Git `git push heroku master`. This triggers 
a build process on the remote. Requirements are installed

6. See if any instances are running using `heroku ps` which prints
```cmd
(flask) python-getting-started (master) $ heroku ps
Free dyno hours quota remaining this month: 550h 0m (100%)
Free dyno usage for this app: 0h 0m (0%)
For more information on dyno sleeping and how to upgrade, see:
https://devcenter.heroku.com/articles/dyno-sleeping

=== web (Free): gunicorn gettingstarted.wsgi --log-file - (1)
web.1: up 2019/10/11 15:34:31 -0700 (~ 57s ago)

```
7. Next scale the app with 1 instance using `heroku ps:scale web=1` which returns
```cmd
Scaling dynos... done, now running web at 1:Free
``` 
8. You can open the app by `heroku open` which opens the app in the browser.
9. Your account page should show the newly created web app running on free dynos.

## Procfiles
You can declared the app. Great! Next up is `Procfile`s and how to write them. You create
Procfile without extension, with capital P and place it in the root dir of your 
repo. Procfile syntax is of the form
```procfile
<process type>: <command>
```
where, process type is name given to the command and the `command`
is the command to be executed.

## Scaling
See the number of dynos using `heroku ps` command. By default all free tier is
exhausted before using anything paid. Free tier will sleep 
after `30` min of inactivity. The next time a request comes in
there will be a short delay due to cold start. If you want 
dedicated dynos, upgrade the account to professional.

## Dependencies
Heroku relies on `requirements.txt` file for Python apps and this is 
run when the app is created. All cascading deps will be
installed.

## Local development
Going forward, you need to create a local dev replica. You can do so by creating a new
conda env, running `pip install -r requirements.txt`, once ready, run `heroku local web`
which runs the env locally, but not with containers.

You can push your changes to your remote. If you push to `heroku` remote, then 
the app gets updated and restarted

### Helpful references
1. [https://coderwall.com/p/pstm1w/deploying-a-flask-app-at-heroku](https://coderwall.com/p/pstm1w/deploying-a-flask-app-at-heroku)
2. [flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
3. [flask - uploading files](https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/)

# Log from pushing this app to Heroku
```cmd
(flask) flask-to-web (master) $ git push heroku master
Enumerating objects: 27, done.
Counting objects: 100% (27/27), done.
Delta compression using up to 12 threads
Compressing objects: 100% (23/23), done.
Writing objects: 100% (27/27), 5.93 KiB | 1.98 MiB/s, done.
Total 27 (delta 8), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing python-3.6.9
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting Flask==1.1.1 (from -r /tmp/build_6b09681a8558fbd1f34aa4d3a84e35e6/requirements.txt (line 1))
remote:          Downloading https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl (94kB)
remote:        Collecting requests==2.22.0 (from -r /tmp/build_6b09681a8558fbd1f34aa4d3a84e35e6/requirements.txt (line 2))
remote:          Downloading https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl (57kB)
remote:        Collecting six==1.12.0 (from -r /tmp/build_6b09681a8558fbd1f34aa4d3a84e35e6/requirements.txt (line 3))
remote:          Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
remote:        Collecting urllib3==1.24.2 (from -r /tmp/build_6b09681a8558fbd1f34aa4d3a84e35e6/requirements.txt (line 4))
remote:          Downloading https://files.pythonhosted.org/packages/df/1c/59cca3abf96f991f2ec3131a4ffe72ae3d9ea1f5894abe8a9c5e3c77cfee/urllib3-1.24.2-py2.py3-none-any.whl (131kB)
remote:        Collecting itsdangerous>=0.24 (from Flask==1.1.1->-r /tmp/build_6b09681a8558fbd1f34aa4d3a84e35e6/requirements.txt (line 1))
remote:          Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
remote:        Collecting click>=5.1 (from Flask==1.1.1->-r /tmp/build_6b09681a8558fbd1f34aa4d3a84e35e6/requirements.txt (line 1)
remote:          Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
remote:        Collecting Jinja2>=2.10.1 (from Flask==1.1.1->-r /tmp/build_6b09681a8558fbd1f34aa4d3a84e35e6/requirements.txt (line 1))
remote:          Downloading https://files.pythonhosted.org/packages/65/e0/eb35e762802015cab1ccee04e8a277b03f1d8e53da3ec3106882ec42558b/Jinja2-2.10.3-py2.py3-none-any.whl (125kB)
remote:        Collecting Werkzeug>=0.15 (from Flask==1.1.1->-r /tmp/build_6b09681a8558fbd1f34aa4d3a84e35e6/requirements.txt (line 1))
remote:          Downloading https://files.pythonhosted.org/packages/ce/42/3aeda98f96e85fd26180534d36570e4d18108d62ae36f87694b476b83d6f/Werkzeug-0.16.0-py2.py3-none-any.whl (327kB)
remote:        Collecting chardet<3.1.0,>=3.0.2 (from requests==2.22.0->-r /tmp/build_6b09681a8558fbd1f34aa4d3a84e35e6/requirements.txt (line 2))
remote:          Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
remote:        Collecting idna<2.9,>=2.5 (from requests==2.22.0->-r /tmp/build_6b09681a8558fbd1f34aa4d3a84e35e6/requirements.txt (line 2))
remote:          Downloading https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl (58kB)
remote:        Collecting certifi>=2017.4.17 (from requests==2.22.0->-r /tmp/build_6b09681a8558fbd1f34aa4d3a84e35e6/requirements.txt (line 2))
remote:          Downloading https://files.pythonhosted.org/packages/18/b0/8146a4f8dd402f60744fa380bc73ca47303cccf8b9190fd16a827281eac2/certifi-2019.9.11-py2.py3-none-any.whl (154kB)
remote:        Collecting MarkupSafe>=0.23 (from Jinja2>=2.10.1->Flask==1.1.1->-r /tmp/build_6b09681a8558fbd1f34aa4d3a84e35e6/requirements.txt (line 1))
remote:          Downloading https://files.pythonhosted.org/packages/b2/5f/23e0023be6bb885d00ffbefad2942bc51a620328ee910f64abe5a8d18dd1/MarkupSafe-1.1.1-cp36-cp36m-manylinux1_x86_64.whl
remote:        Installing collected packages: itsdangerous, click, MarkupSafe, Jinja2, Werkzeug, Flask, urllib3, chardet, idna, certifi, requests, six
remote:        Successfully installed Flask-1.1.1 Jinja2-2.10.3 MarkupSafe-1.1.1 Werkzeug-0.16.0 certifi-2019.9.11 chardet-3.0.4 click-7.0 idna-2.8 itsdangerous-1.1.0 requests-2.22.0 six-1.12.0 urllib3-1.24.2
remote: 
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
remote:        Done: 45.7M
remote: -----> Launching...
remote:        Released v3
remote:        https://atma-flask-to-web.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/atma-flask-to-web.git
 * [new branch]      master -> master
(flask) flask-to-web (master) $ 
```
The app runs at [https://atma-flask-to-web.herokuapp.com/](https://atma-flask-to-web.herokuapp.com/)
