# Introduction to Git

Sharing the following [xkcd](https://xkcd.com) webcomic is practically mandatory for those introducing people to `git` and version control software:

```{figure} https://imgs.xkcd.com/comics/git.png
:alt: xkcd webcomic. One person explains to another, "This is git. It tracks collaborative work on projects through a beautiful distributed graph theory tree model." "Cool. How do we use it?" "No idea. Just memorize these shell commands and type them to sync up. If you get errors, save your work elsewhere, delete the project, and download a fresh copy."
:class: bh-primary
:width: 350px
:align: center
[https://xkcd.com/1597/](https://xkcd.com/1597/)

```

It comes uncomfortably close to the truth: it is possible to be able to 'use `git`' simply by memorising a few basic commands, and I have definitely been guilty of messing up to the extent that I simply needed to delete everything and download a new copy! Whilst I will identify the core workflows and commands in these exercises, I hope you also take the opportunity to try and _understand_ what is happening when you run commands, and why we might use them.


## Setup 

### Installing `git` and `gh`

You should have already installed `git` on your local machine following the [Week 6 Instructions](../06/index.md#github). You can check this by opening your Miniforge prompt (Windows) or terminal (macOS/Linux) and seeing if you can get a sensible response from `git --version` (which should return the version of `git` you are using). 

 - If you are on Windows and it doesn't work, check whether it will work on the standard Command Prompt (not the Miniforge prompt). If it does, you have probably forgotten to tick the _"Git from the command line and also from 3rd-party software"_ option during the install process, and will need to try again. 
 - If you are on macOS and you start getting complaints about the Xcode command line tools, you haven't installed `git` yet. You will need to wait for macOS to install it - this will take a while!

Once you are sure you have `git` installed successfully, activate our class environment and install a new package: "`gh`", the GitHub command line interface:

```bash
conda activate gsc
conda install -c conda-forge gh
```

### Authenticate to GitHub

`git` is the core tool we will be using today; `gh` (the GitHub CLI tool) is a simple add-on that we will use once to link our local work to our online GitHub account. Let's first log in to our GitHub account.

```bash
gh auth login
```

You will be asked a series of questions, which hopefully resemble those below. Use the arrow keys and {kbd}`Enter` to select the following answers:

```
? Where do you use GitHub? GitHub.com
? What is your preferred protocol for Git operations on this host? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Login with a web browser
```

You will then be given a one-time code, and a web browser will open. Log in to GitHub (if you aren't already), and enter the code to authorise `gh`.

You can confirm the login has been successful using the `status` query:

```bash
gh auth status
```

After this has been successfully installed, run the next command to authenticate our git environment:

```bash
gh auth setup-git
```

Next, tell `git` who you are. Every commit you make is labelled with a name and email address, and `git` may refuse to commit until these are set. Using the same details as your GitHub account helps GitHub recognise that the local edits you make match your account.

```bash
git config --global user.name "myusername"
git config --global user.email "myemail@example.com"
```

:::{note}
Anything you commit to a public repository will show this email address. If you would rather keep your email private, GitHub provides a "no-reply" address you can use instead: find it under **Settings** > **Emails** on GitHub (it looks like `12345678+myusername@users.noreply.github.com`).
:::

Finally, run the following command so that new repositories use `main` as the name of their primary branch (we will explain branches later). This matches GitHub's default; without it, some versions of `git` will use `master`, which will cause some of the commands below to fail.

```bash
git config --global init.defaultBranch main
```

## Single User Workflow

### Initialise a Repository

Create a new directory wherever is sensible for you. Call it `geogm0081-week-9`. 

Within the Miniforge prompt (Windows) or terminal (macOS/Linux), move to this directory.

```bash
cd geogm0081-week-9
```

Create a new markdown file called `README.md` within this directory, and edit it within a text editor to add some generic markdown text; for instance:

```
# Example Git Repository

This is an example repository created in the course of the GEOGM0081 course at Bristol, used to learn and practice `git` and GitHub.
```

Once you have done this, initialise `git` in this repository.

```bash
git init
```
```
Initialized empty Git repository in /Users/tom/msc/geogm0081/geogm0081-week-9/.git/
```

We have now set up the files such that `git` can begin tracking this directory. The software stores everything it needs in a new hidden `.git` directory (which you should never need to look at or edit directly). But no version control is happening just yet. We can confirm this by checking the `status` of our files:

```bash
git status
```
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md

nothing added to commit but untracked files present (use "git add" to track)
```

:::{note}
If the first line of the output says `On branch master` instead of `On branch main`, run `git branch -M main` to rename the branch (and see the `init.defaultBranch` setting in the setup instructions above).
:::

We need a two-step process to begin tracking changes to our file: we first define the changes we want to track using `git add`. This is known as **staging** the changes.

```bash
git add .
git status
```
```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   README.md
```

:::{note}
The `.` means "this directory", and tells `git` to stage **all new and changed files within the directory** (except those listed in a `.gitignore` file). You can also stage individual files by name, e.g. `git add README.md`.
:::

We can then use `git commit` to begin tracking our files, leaving a note to remind us what we have included in the current commit.

```bash
git commit -m "initial commit"
```
```
[main (root-commit) e829ea6] initial commit
 1 file changed, 3 insertions(+)
 create mode 100644 README.md
```

:::{note}
The `-m` flag is a message that we use to briefly describe what the changes were.
:::

Checking with `git status` shows that our files now match the most recent commit:

```bash
git status
```
```
On branch main
nothing to commit, working tree clean
```

### Modify a Repository

Let's add another file to the project. Create a new file called `roll_die.py`, containing the following code:

```python
import random

def roll(low=1, high=6):
    num = random.randint(low, high)
    return num

print(f"Your die has returned the number {roll()}")
```

(run `python roll_die.py` if you like: I'm sure you can guess what will happen.)

Also add a new line to `README.md` containing the following:

```
`roll_die.py` returns a random integer between 1 and 6
```

Now, run `git status`: we will see there are two files that have changed since the commit. `REAMDE.md` is **modified** and `roll_die.py` is **untracked**:

```bash
git status
```
```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	roll_die.py

no changes added to commit (use "git add" and/or "git commit -a")
```

We can `add` again to **stage** changes that we can commit.

```bash
git add .
git status
```
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   README.md
	new file:   roll_die.py
```

... and use `git commit` to track them.

```bash
git commit -m "added roll_die.py"
```
```
[main 4a5bbcb] added roll_die.py
 2 files changed, 9 insertions(+)
 create mode 100644 roll_die.py
```

:::{tip}
Adding the `-a` option to the git commit command makes Git automatically stage every file that is already tracked before doing the commit, letting you skip the `git add` part e.g. `git commit -a -m "some more changes"`.

You will still need to `git add .` when you have created new files.
:::

### Navigating the repository history

:::{warning}
Some of the commands in this subsection - `git log`, `git checkout` and `git restore` - are safe to try. However, **don't run the `git reset --hard` command at the end of this subsection** unless you really want to: it will permanently delete the `roll_die.py` commit, and the rest of this page assumes you still have it.
:::

At this point, run `git log`: you can inspect the history of the repository in reverse chronological order (newest first) with the author information and commit message.

```bash
git log
```
```
commit 4a5bbcb2f0d1c9e8a7b6c5d4e3f2a1b0c9d8e7f6 (HEAD -> main)
Author: myusername <myemail@example.com>
Date:   Wed Nov 18 10:12:43 2026 +0000

    added roll_die.py

commit e829ea674e5563626ce44015a71454d4aedca51b
Author: myusername <myemail@example.com>
Date:   Wed Nov 18 10:05:11 2026 +0000

    initial commit
```

If the output is longer than your screen, press {kbd}`q` to exit. For a more compact view, try `git log --oneline`.

Each commit is named using a type of checksum called a SHA-1 hash, which is a 40-character string composed of hexadecimal characters (0–9 and a–f). Your hashes will be different to the ones shown here. You will often see only the first seven characters (e.g. `e829ea6`), which `git` will also accept as a shorthand.

Using this checksum, we can go backwards to previous commits using `git checkout`:

```bash
git checkout e829ea674e5563626ce44015a71454d4aedca51b
```
```
Note: switching to 'e829ea674e5563626ce44015a71454d4aedca51b'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at e829ea6 initial commit
```

By rolling back to prior versions, you have the opportunity to save the old file somewhere else before going back to the `main` branch using `git checkout main`. 

```bash
git checkout main
```
```
Previous HEAD position was e829ea6 initial commit
Switched to branch 'main'
```

If we made changes to a file that we later decide we don’t want, we can undo them (i.e. roll them back to the most recent commit) using `git restore`.

```bash
git restore README.md
git status
```
```
On branch main
nothing to commit, working tree clean
```

If we want to reset our repository to a previous commit, we can use `git reset`. The `--hard` flag means that any commits (and uncommitted changes) made after that point are discarded.

```bash
git reset --hard e829ea674e5563626ce44015a71454d4aedca51b
```
```
HEAD is now at e829ea6 initial commit
```

:::{tip}
In practice, you probably won't be rolling back and forth too much unless things have gone wrong: if you find yourself doing so, do so very carefully (particularly when using `git reset --hard`), as it is possible to lose work!
:::

## Remote Repositories (Working with GitHub)

The real power of using `git` for sharing and collaboration comes from using a "remote repository". In this course, we will be using GitHub to host our remote repositories.

:::{note} Difference between `git` and GitHub
`git` and GitHub are often used interchangeably, but it is important to note they are not the same. `git` is a local, open-source version control system that can be used to keep track of changes locally. GitHub is an online web platform (for-profit, owned by Microsoft) that allows you to host your repositories online. Online hosting is a real strength that massively enhances your ability to perform open and reproducible science.

GitHub is, ultimately, the biggest game in town, but it’s important to note that it isn’t necessarily part of the same feel-good open-source community as the rest of the tools I’ve been recommending. There are alternatives, such as GitLab (which is itself open-source) and Codeberg (run by a non-profit), which work with exactly the same `git` commands. However, for various reasons they have much smaller communities, so you are less likely to find other people's code there.
:::

To set up a remote repository, first go to [the GitHub main page](https://github.com/) and create a new repository (click `+` in the header, and then **New repository**).

Input a name for the new repository, matching your local repository (e.g. `geogm0081-week-9`). You can set the visibility to **Private** for now. Leave everything else blank or switched off - in particular, don't add a README, `.gitignore`, or license here, as our local repository already has its own history, an if you create them on GitHub then you will have two conflicting histories. Click **Create repository**. You should be able to see the empty repository at `github.com/myusername/geogm0081-week-9`.

Back in the terminal, run the following command, substituting your username and project name as appropriate:

```bash
git remote add origin https://github.com/myusername/geogm0081-week-9.git
```

:::{note}
`origin` is simply the conventional name for the main remote repository. GitHub also shows an `SSH` version of the address (beginning `git@github.com:`): don't use this, as we set up `gh` to use `HTTPS`, and SSH addresses require additional setup.
:::

You can check whether your remote command has been successful:

```bash
git remote -v
```
```
origin	https://github.com/myusername/geogm0081-week-9.git (fetch)
origin	https://github.com/myusername/geogm0081-week-9.git (push)
```

We can then upload the commit history from local repository to the remote repository using `git push`.

```bash
git push -u origin main
```
```
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 612 bytes | 612.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/myusername/geogm0081-week-9.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

:::{note}
The first time we use this command we have to include `-u origin main` to define which branch we want to upload to (i.e. the `main` branch of our remote repository called `origin`). `-u` is short for `--set-upstream`: it tells `git` to remember this connection, so from now on you can simply run `git push` (and `git pull`) without any extra arguments.
:::

Now view your repository on the GitHub page (e.g. github.com/myusername/geogm0081-week-9). You should see the `README.md` and `roll_die.py` files.

Now, click **Add file** > **Create new file**. Create a new markdown file (called e.g. `test.md`) with some dummy text. Commit this within the browser, leaving an appropriate commit message.

We can run `git fetch` now to compare our local repository with our (changed) remote repository and download the new commits from the remote. Note that this command does not modify the files in our local repository.

```bash
git fetch
```

Now, after running `git status`, we find that our local repository is 1 commit behind the remote repository:

```bash
git status
```
```
On branch main
Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean
```

We can use `git pull` to merge the remote commits into our local repository.

```bash
git pull
```
```
Updating 4a5bbcb..b3eb2b2
Fast-forward
 test.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 test.md
```

:::{note}
The phrase “fast-forward” means that the commit in the remote repository was ahead of the commit in the local repository, so Git simply moves the pointer forward. `git pull` actually does a `git fetch` for you first, so in practice you can skip running `git fetch` separately.
:::

Now when we run `git status`, the second line tells us that our repository is up to date with `origin/main`, the remote repository.

```bash
git status
```
```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## Retrieving a remote repository (cloning)

If you find yourself wanting to retrieve a remote repository, rather than setting one up, the process is slightly different.

On the repository's GitHub page, click the green **Code** button, select the **HTTPS** tab, and copy the address. Then, in the terminal, move to the directory in which you want the repository to be created (`git clone` will create a new directory for it). Now, run `git clone` with that address. For instance, to clone the example repository from the previous page:

```bash
git clone https://github.com/trchudley/geogm0081-example-repo.git
cd geogm0081-example-repo
```

The cloned repository comes with its full history (try `git log`), and it is already connected to the GitHub repository as `origin` - so there is no need to run `git init` or `git remote add`.

When the remote repository is later updated (by you on another computer, or by someone else), you can bring your local copy up to date by running, from within the repository directory:

```bash
git pull
```

You can clone any public repository, but you will only be able to `push` changes back to it if you own it or have been given permission. We will look at how to contribute to other people's repositories on the next page.

## Key Workflow

Ultimately, there are only a few key commands you really need to remember.

**Step 1a:** If you are creating a new repository locally: initialise the `git` repo, create an empty repository on GitHub, and connect to it. The first time you push, include `-u origin main`.

```bash
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/myusername/myprojectname.git
git push -u origin main
```

**Step 1b:** If you are cloning an existing remote repository, use the `git clone` command:

```bash
git clone https://github.com/myusername/myprojectname.git
```


**Step 2:** Perform the following every time you make a distinct update to the repository:

```bash
git pull  # if the remote may have changed since you last worked on it
git add .  # if you have created new files
git commit -a -m "description of changes made"
git push
```

## Summary

This shows a minimum viable workflow for you to be able to get your code up and running on GitHub. You should now be able to, at the very least, share code you create and keep it updated. However, you might be wondering what the point of all of this is - on the next page, we will show how version control really becomes of value when you are collaborating with others on the same project.
