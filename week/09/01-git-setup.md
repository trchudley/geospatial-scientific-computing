# Installing git

## Installing `git` and `gh`

Open up your anaconda/mamba shell (Windows) or terminal (macOS/linux). Activate our class environment:

```bash
conda activate gsc
```

And install two new tools: `git` and `gh`:

```bash
conda install -c conda-forge git gh
```

## Log in to GitHub

`git` is the core tool we will be using today; `gh` (the github CLI tool) is a simple add-on that allows us to link our local work to our online GitHub account. Let's first log in to our GitHub account.

```bash
gh auth login
```

You will be asked some questions - select `HTTPS`:

```
What is your preferred protocol for Git operations?
> HTTPS
  SSH
```

You can confirm the login has been successful using the `status` query:

```bash
gh auth status
```

After this has been succesfully installed, run the next command to authenticate our git environment:

```bash
gh auth setup-git
```

You are also welcome to edit your local username and email to match your GitHub account: this helps GitHub recognise that the local edits you make match your account.

```bash
git config --global user.name "myusername"
git config --global user.email "myemail@example.com"
```

## Check `git` is working

Next text.