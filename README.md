# flask-to-web
Project to experiment with deploying a simple web app on the web.

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