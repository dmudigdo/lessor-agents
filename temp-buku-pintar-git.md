# Didi's Git for Dummies

## Intro

Firstly, be in the right directory.

    cd Documents/Repositories
    
Here's how to get a repo from bitbucket, then go into the directory.

    git clone https://dmudigdo@bitbucket.org/dmudigdo/dmudigdo.bitbucket.org.git
    cd dmudigdo.bitbucket.org/
    
`git status` is your friend, use it to figure out how things are going.

    git status
    
Once you have added new files, you need to add them to the 'staging area'.

    git add JVC*
    
Once new files are in the staging area, you can try and commit them (locally).

    git commit -m 'Starting GalliChroum Git commits'
    
Ooops, if you forget to identify yourself, do so.

    git config --global user.email "didi@didi.com.au"
    git config --global user.name "ddgallichroum"
    
OK let's try committing again.

    git commit -m 'Starting GalliChroum Git committs'
    
And here's the good bit: `push` the local changes to BitBucket (or wherever `origin` happens to be)

    git push origin master
    
And Bingo, Bob's your Uncle, local changes are now reflected on the remote BitBucket repo. Now let's change something up in the remote repo. Locally, to `pull` it in we use this command.

    git pull --all

That's all for now.

## 'Reverting'

Reverting can mean [different things](http://stackoverflow.com/questions/4114095/how-to-revert-git-repository-to-a-previous-commit). But this is the one we usually mean:

    git reset --hard 6fd72e1452af3a83080de2bdd89b229c15bda1ac

To do this, first type:

    git log
    
To view all the commits. Then find the serial number for the one you want to revert to. After that, type the git reset command above, with the relevant serial number.

## Branching

Two steps:

    git branch future-plans

...Makes the branch.

    git checkout future-plans

...Jumps onto it.

Once you've made your edits and are satisfied that everything works, do an `add` and `commit` as before (just because it was branched, doesn't mean it was staged. Must stage and then commit).

Then go back to master branch:

    git checkout master

Then merge:

    git merge future-plans

Then delete the working branch:

    git branch -d future-plans

Finally, push all the changes back to GitHub (or BitBucket):

    git push origin master

Thank you for flying git airlines.

## Starting a Local Project then Push

Make the working directory, then go to it

    mkdir blah
    cd blah

And have fun with it, move files in there, check that everything is working etc.

Now, Intialize it as a Git repo

    git init

Add everything to the 'staging area'

    git add .

Commit

    git commit -m "First commit"

So now, locally, all is good. Next, go over to GitHub, set up a new repository (same name as the folder I guess). Find the 'Quick Setup' (if you've done this before) section, and copy the HTTP address of this new GitHub repo.

Now, back to our local machine:

    git remote add origin http://the.address.you.copied.from.github
    git remote -v

And here we go... PUSH!

    git push origin master

Done.

Actually, correction, according to [this stack overflow question](http://stackoverflow.com/questions/6089294/why-do-i-need-to-do-set-upstream-all-the-time), the above should be

    git push -u origin master

As I found out, if you don't do this (i.e. add the `-u` option *the first time you push a local repo*), next time you do a `pull --all` you get the error that the above stack overflow questioner did.

## Deleting a Folder

To delete a folder (and it's contents)

    git rm -r <foldername>
