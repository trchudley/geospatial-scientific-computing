# Week 9 Exercises

## Introduction

The exercises below aim to test your ability to maintain an independent repository, as well as contribute to shared repositories. Bear in mind your ultimate aim when doing this, which should be to share the code for your project.

## Exercise

### Single User Workflow

Go back to your `geogm0081-week-9` repository.

#### Push changes to the remote GitHub repository.

Add an existing Jupyter notebook you have to hand to the repository. Also add an appropriate suite of files as described in the course: e.g. `LICENSE`, `environment.yml`, `.gitignore`, etc. In your `environment.yml`, ensure that you include the necessary Python packages to run your Jupyter notebook.

`add`, `commit`, and `push` the changes to a remote repository. If you have been succesful, you will be able to see the new files and changes within your GitHub repository.

#### Create remote changes and ensure your local repository reflects them.

On the GitHub repository, make some minor edit to the `README.md` file, and commit it. Use the tools you have learned (e.g. `pull`) to update your local repository to reflect this. If you have been succesful, you will be able to see the edit in your local repository.

### Collaborative Workflow

Fork the repo [`github.com/trchudley/geogm0081-practice-repo-2026`](https://github.com/trchudley/geogm0081-practice-repo-2026).

Clone your forked repo to your local environment, and create a new branch to work in. When done, add a new directory, titled according to your first name (this will end up on a public repository, so don't include anything you don't want public!). Within this directory, add a `README.md` file. Within this file, tell me about the favourite place (park, museum, restaurent, etc...) you have discovered whilst you have been living in Bristol.

`add`, `commit`, and `push` this file back to your remote GitHub repository. Once it is your forked repository on GitHub, submit a pull request which explains the changes you have made. I will review the pull request and merge it back into the main repository. Once it has been merged, practise syncing your fork and updating your local `main` branch.


## Your Final Project

Your final project needs to be submitted in two parts. 

 - The first is the project report, which should be submitted via Blackboard as a standard document file.
 - The second is the code, which we discuss here.

### Organising your code repository

You should start thinking about how you are structure your code repository as you progress through your project. This will not only make it easier upon submission, but also help you organise and think about your own work as you go.

Your code should be organised into a sensible repository structure as described in this week's content. 

 - It should include a reasonable `README.md`, `environment.yml`, `LICENSE` file, and `.gitignore` file. 
 - Try and separate your directories as already shown - e.g. by `notebooks`, `figures`, and `data`. 
 - In principle, users should be able to set up an environment according to your `environment.yml` file and run the notebooks to reproduce your work. However, for the benefit of not including large file sizes, **do not** include `*.tif` or `*.nc` files (in fact, `*.tif` and `*.nc` should probably be in your `.gitignore`). Instead, your report and code should describe how you downloaded and produced your gridded data files, so that someone could recreate them if they wished.
 - Notebooks should have clear file and variable names. Path management should be done using relative paths (e.g. via `pathlib`) so that they do not break on someone else's PC.

Even if you ultimately don't end up submitting your code via GitHub (see below), operating via GitHub is good practice regardless - and it will give you something to share to potential employers to show you are capable with these workflows. A complete commit history helps you keep track of the changes you have made, and is useful for proving to people that you weren't just letting AI spit out all the work in one go!

### Submitting your code repository

You are welcome to submit your code in one of three ways. **Please state which method you have used within your main report.**

1. **Via Blackboard:** a `.zip` file of your repository, submitted through Blackboard (much like your project report). The zip file should be named according to your Student ID number (e.g. `0123456.zip`)
2. **Link your own GitHub repo within the main report** Include a link to a personal GitHub repo within your report. This should be **publicly accessible** so that those grading your report can see it. It is not advised to go down this route if your GitHub username is identifiable (e.g. `firstname-surname`), as this will mean that the link will not be suitably anonymous for grading.
3. **Via a shared repository:** If you are comfortable doing so you are also welcome to submit via a shared repository. Inform me of your GitHub username and I will add you as a member of the [private GitHub repository `trchudley/geogm0081-submission-2026`](https://github.com/trchudley/geogm0081-submission-2026), Fork this to your own GitHub profile, and then clone that to your local environment. Create a **new directory named according to your student number**, and deposit your code repository within it. Push this to your remote repository and submit a pull request. I will confirm I have received the pull request with the review process - although I will not merge the files until after the submission date.

### Notes

:::{warning}
If your project code is already a `git` repository (i.e. it contains a hidden `.git` directory), copy the files into the submission repository **without** the `.git` directory. Otherwise, `git` will treat it as an "embedded repository" and only record a reference to it, rather than the files themselves - and your pull request will appear to contain an empty folder.
:::
