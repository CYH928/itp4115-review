# Git

## Configure
<!-- `git <command> -help: Check the command how to use and have what options

`git --version: Check if you have which version of PC Git is installed

`git --global user.name “<name>”: Config the edit user name
`git --global user.email “<email>”: Config the edit user email -->

`git status`: Check current branch the files status

`git status --short`: Display short-form the files status
?? - Untracked files
A - Files added to stage
M - Modified files
D - Deleted files


## Repository
`git init` <project_name>: Create a new repository

`git clone` <URL>: From GitHub sync the updated repository to local (after can pull/push)
<!-- `git clone` <URL> <folder_name>: Clone GitHub repository to local add named the folder -->


## Staging
`git add <file>`: Add the snapshot to the stage

`git add -A`: Add all changed files to the stage

<!-- `git add .: Add currently all changed files to the stage -->

`git add *.<file_format (.html)>`: Add all changed format files to the stage


## Commit
`git commit`: Submit current stage to commit(e.g. GitHub)

`git commit -m “<message>”`: Submit and remark to commit

`git commit -a -m “<message>”`: include `git add + commit function

`git commit --amend -m “<message>”`: Edit the last commit message

<!-- `git log: Display the commit log
`git log --oneline: Display each commit with ID(commit hash) in one-line -->


## Branch 
`git branch`: Show local repository all branch

`git branch <branch_name>`: Create a new branch from current branch

`git branch -d <branch_name>`: Delete a branch
<!-- `git branch -a: Show local repository + remote repository all branch
`git branch -r: Show only remote repository of branch -->

`git checkout <branch_name>`: Switch to that branch (now & before Git v2.23)

`git checkout -b <branch_name>`: Switch and create new branch

`git switch <branch_name>`:Switch to that branch (after Git v2.23 or above)


## Merge
#### !!! Before a merged branch must checkout to that merge branch (master/main) first.
`git merge <merged_branch>`: Which branch merges with the current branch


<!-- ## Rebase
`git rebase <branch>: Base on which branch continue edit -->


<!-- ## Remote for GitHub
`git remote -v: Display the remote repository name

`git remote rename <current_name> <new_name>: Change the new remote name

`git remote add <repository_name (origin)> <URL>:  -->


## Pull from GitHub
<!-- `git fetch
`git fetch [origin]: From remote repository download to local repository
`git merge: From local repository merge to working directory -->

`git pull`: From the remote repository download to your local repository + working directory (fetch + merge)
Push to GitHub
`git push`: From local repository push to remote repository (e.g. GitHub)


## Reset
HEAD <- last time commit snapshot
commit_id AKA commit hash (include seven characters [a-z,0-9])

<!-- `git revert HEAD: Make a new snapshot commit, revert the last change commit data (Local repository)
`git revert HEAD --no-edit: Skip add commit message use default revert message -->

`git reset <commit_id>`: Reset to that commit
`git reset <file>`: Remove from staging back to the working directory and don't commit to the local repository (Staging -> Working directory)
<!-- `git reset --soft HEAD~1: 	Remove the local repository commit snapshot (Local repository)
`git reset HEAD~1: 		Cancel the `git commit + `git add (Local repository + Staging)
`git reset --hard HEAD~1: 	Cancel the `git commit + `git add (Local repository + Staging + Working directory) -->