# Collaborating using Git(Hub)

In a modern workflow, it is unlikely that we will be working on files entirely by ourselves. Instead, we will want to work with others on larger collaborative projects. 

We already use tools every day to collaborate with others on some virtual data files. For example, Microsoft Office and Google Docs provide ways for teams of people to simultaneously work together on documents, spreadsheets, etc.

However, I hope you can see how this might be impractical to do on code-based projects. For instance, code will only run if it is all in working order. How are you supposed to check changes you have made to the code run successfully, if I am trying to edit code elsewhere at the same time? And how does this work across teams of tens or hundreds all trying to work on different components of a project, relying on everything else staying the same?

## A centralised pull/push workflow

From what we now understand about `git` and GitHub, I want us to now imagine a scenario where a team is looking to collaborate together on a project, using only the skills we know so far.

1. One team member creates a remote repository. All team members **clone** this central repository to their local machine.

```{figure} /img/gh-1-colab.svg
:alt: three users have each cloned a copy of a central remote repository to their local machines
:class: bh-primary
:width: 850px
:align: center

```

1. One team member makes changes to files on their local machine, periodically **committing** these changes (i.e. taking a snapshot).
2. When they are finished working, this first user can **push** their changes back to the central repository.

```{figure} /img/gh-2-john-push.svg
:alt: the first user pushes to the remote repository
:class: bh-primary
:width: 850px
:align: center

```

4. But now when **another team member** (who has also been working on the project) tries to **push** their changes, Git will refuse the request because their local history has diverged from the central repository.

```{figure} /img/gh-3-mary-push.svg
:alt: a second user attempts to push their changes, but it fails
:class: bh-primary
:width: 850px
:align: center

```

5. The team member must first **pull** the most recent changes in the central repository into their local repository.

```{figure} /img/gh-4-mary-pull.svg
:alt: the second user pulls from the remote repository
:class: bh-primary
:width: 850px
:align: center

```

1. The team member then resolves any conflicts between their local version and the central repository. A **conflict** happens when both people have changed the same lines of the same file: `git` can't know which version to keep, so it marks the clashing sections in the file and asks the human to decide.

2. Once finished, the team member can then commit and push their changes to the central repo.

```{figure} /img/gh-5-mary-successful-push.svg
:alt: the second user successfully pushes to the remote repository
:class: bh-primary
:width: 850px
:align: center

```

This is a simple workflow and it might work well for small teams. However, it has multiple disadvantages:

 - If someone breaks the central repo, it breaks for everyone.
 - Potential for a lot of conflicts.
 - One solution is to all agree avoid working on the same files at the same time, but this does not scale well as teams increase in size...

## Branching workflows with Git(Hub)

To allow people to continue to work on projects simultaneously without breaking each other's workflow (or to allow one person to work on multiple sub-project in parralel without letting them interfere with one another), `git` has a functionality known as 'branching'. To examine how this works, return to the repository we set up in the previous section.

Return to your  `geogm0081-week-9` directory. Run the command `git branch`:

```bash
git branch
```
```
* main
```
This output is intended to show that you have one branch, known as **main**. The asterisk shows that we are currently in that branch.

Run the following command:

```bash
git checkout -b new-code
```
```
Switched to a new branch 'new-code'
```

This has created, and switched to, a new branch known as `new-code`. Confirm this by running `git branch` again, and noting what has changed.

:::{note}
Newer versions of `git` also provide `git switch` as an alternative to `git checkout` for moving between branches (`git switch -c new-code` creates a new branch). The two do the same job here; we use `git checkout` throughout as it works on all versions.
:::

In branches, we can continue to make changes and commits without disrupting the `main` branch. It is called a branch because we can think of the timeline as a series of branching commits:

```{figure} /img/gh-6-big-branch.svg
:alt: a timeline of commits (circles) along the main branch, with two separate branches splitting off from it at different points, each containing their own commits
:class: bh-primary
:width: 850px
:align: center

```

Eventually, these branches are merged back together. On GitHub, this is done using a **pull request**: a request for the owner of the repository to _pull_ the changes from your branch into the `main` branch.

Let's make a change within our branch. For instance, create a new file `helloworld.py` containing the following code:

```python
print("Hello, world!")
```

Now, we can add and commit our changes in the usual way:

```bash
git add .
git commit -a -m "new helloworld file"
```

Try switching back to the `main` branch by using `git checkout main` (note the lack of `-b` flag: this is because we do not need to create the `main` branch from scratch, merely switch to it). The new file should disappear: assess this either by examining your file directory, or directly from from the command line interface by running the `dir` (Windows) or `ls` (macOS) command.

Switch back to the branch by running `git checkout new-code`. Run `git branch` and examine the output ensure you are in the correct branch (an asterisk should appear next to `* new-code`). The `helloworld.py` file should have reappeared.

Now, we can `push` this to a new branch of our remote repository. Note the slightly different syntax I use here: I no longer push to `origin main`, but to a new branch `new-code`.

```bash
git push --set-upstream origin new-code
```
```
remote: 
remote: Create a pull request for 'new-code' on GitHub by visiting:
remote:      https://github.com/myusername/geogm0081-week-9/pull/new/new-code
remote: 
To https://github.com/myusername/geogm0081-week-9.git
 * [new branch]      new-code -> new-code
branch 'new-code' set up to track 'origin/new-code'.
```

<!-- ORIGINAL:
Return to the GitHub repository page. You should be able to view the new branch. You have the option to create a **pull request**: make one now. 
-->

Return to the GitHub repository page (e.g. github.com/myusername/geogm0081-week-9). You should be able to view the new branch (use the branch drop-down menu, which currently reads `main`). You should also see a yellow banner with a **Compare & pull request** button: this is the process through which we will initiate merging the branch changes back into `main`. 

Click it, leave a title and description, and click **Create pull request**. The team leader (in this case, you) now has the opportunity to **review** the pull request and discuss any changes with the team member in a forum-like format.

GitHub will automatically check whether there are any **conflicts** between the branch and the main branch. If it reports 'This branch has no conflicts with the base branch', you will be able to merge the pull request into the main branch by clicking **Merge pull request**. If there _are_ conflicts, the team leader will have the option to go through the code and pick which of the branch or main code they would like to keep (simple conflicts can be resolved in the browser; more complex ones need resolving locally).

Once you have merged the pull request, GitHub will offer a **Delete branch** button, which deletes the branch on your GitHub (remote) repository. The commits are safe: they are now part of `main`.

You can also make sure your local environment is updated, and delete the local branch:

```bash
git checkout main  # switch back to main
git pull  # update main
git branch -d new-code  # delete the branch
```
```
Deleted branch new-code (was 1c2d3e4).
```

:::{note}
Make sure you `git pull` _before_ deleting the branch. `git branch -d` will only delete a branch whose changes are already included in your current branch, and refuses otherwise - a useful safety net against accidentally deleting work.
:::

You should now be back in the main branch, with our changes made: `helloworld.py` should be present.

By using a branch workflow, large numbers of team members can all make their own changes and commits. **Pull requests** and **code reviews** allow changes to be merged back into a single source of truth: the `main` branch. Teams can work in parallel on the same files, whilst the main branch never contains broken code.

However, it is important to keep good practice:

 - If working with others, agree on a standard way of working. For instance, [my own open-source Python packages have a specific 'how to contribute' section](https://pdemtools.readthedocs.io/en/latest/appendix/community_guidelines.html#contribute-to-pdemtools), which directs people to a [standardised git workflow](https://www.asmeurer.com/git-workflow/), so no one is confused.
 - Commit often. Commits are easy to make and provide opportunities to revert or undo work: they should be made frequently as you make changes. 
 - Leave detailed log messages, so future readers can understand what has changed.
 - Use branches frequently and liberally: ensure they do not stay open for so long the codebases diverge - after a task is complete, branches should be merged back in the main development branch and then deleted.
 - Ensure you're working from the latest version. Use `git fetch` or `pull` the latest code before you start making changes: as you fall behind, it can be harder to successfully merge back into the main branch.
 - `git` repositories don't always play nicely with cloud storage systems (e.g. OneDrive, Google Drive), as cloud storage software can make their own unintended changes to file metadata. Of course, this means your data won't always be automatically backed up, which makes committing and pushing to a remote repository even more important! Even so, for your final projects/dissertations, I would recommend keeping your files within your University OneDrive files, just in case things go wrong at the last moment.

Remember that version control acts like an unlimited 'undo' - protecting the source code from yourself and others.

## Contributing to public repositories (forking)

During early development, or for working on private projects between teams, you probably want to keep your GitHub repository private. You can always add collaborators (under **Settings > Collaborators** on the repository page), which will allow them to view the online repository and `clone`/`push`/`pull` changes.

However, ultimately, open-source code should be openly available in public repositories. This can be scary to do, especially for those who don't come from a clear programming background (e.g. geosciences!). However, sharing your code doesn't just help others - it allows others to help you, as others can begin to edit and improve your codebase.


One way that public repositories protect themselves from contributions that aren't necessarily helpful (maliciously or otherwise) is to **limit public push access**. As a result, you can't just clone any old GitHub project and expect to push changes directly to it. 

Instead, users must **fork** a repository. You can think of this as a further evolution of a branch: rather than a copy of one line of history within the same repository, it is a copy of the _entire repository_, stored under your own GitHub account. You can do this by finding the GitHub repository you wish to fork, and clicking the **Fork** button which appears in the top right corner. Leave everything as is on the next page and click **Create fork**. 

When we do this, GitHub will make a copy of the project that lives in our namespace that we can push to. For instance, as well as a `github.com/other-user/coolproject`, there will be a `github.com/my-username/coolproject`. The original repository is conventionally referred to as the **upstream** repository.

You can now follow the same `clone` > `branch` > `commit` > `push` > `pull request` system as before.

1. Clone your forked remote repository into your local environment (note: _your_ username, not the original owner's).

```bash
git clone https://github.com/my-username/coolproject.git
cd coolproject
```

2. Create a new branch.

```bash
git checkout -b description-of-change
```

3. Make your changes, then `add` (if new files are introduced), `commit`, and `push` to a new branch of your fork (`origin`).

```bash
git add .
git commit -a -m "my change"
git push --set-upstream origin description-of-change
```

You can now go to your fork on GitHub, where there should be a **Compare & pull request** button. GitHub will set up a pull request from your branch into the `main` branch of the original (upstream) repository. You will be required to provide a **title** and **description**. Put some effort into these: a good description helps the owner of the original project determine what you were trying to do. Then, you can click **Create pull request**.

The code maintainer may make their own edits, or ask you to make them yourself. You can always `commit` and `push` more changes to the same branch: these will be absorbed into the existing pull request automatically.

After the pull request has been merged, you can delete your branch on your fork on GitHub. You can then either delete the fork entirely, or bring your fork's `main` branch up to date with the upstream repository: on your fork's GitHub page, click **Sync fork** > **Update branch**.

:::{important}
Your fork does _not_ update automatically when the upstream repository changes. Running `git pull` on your computer pulls from your fork (`origin`), not the upstream repository - so you need to **Sync fork** on GitHub first.
:::

Once your fork is synced, you can do the same for your local repository:

```bash
git checkout main
git pull  # update local main from your (now synced) fork
git branch -d description-of-change  # delete the old branch
```

## Key Workflow

In a collaborative workflow, the key steps are still relatively simple:

**Step 1 (Optional):** If you are contributing to a public repository, **Fork** the repository into your GitHub userspace.

**Step 2:** Clone the remote repository (or your fork of it) using the `git clone` command:

```bash
git clone https://github.com/myusername/projectname.git
```

**Step 3:** Create and switch to a new branch.

```bash
git checkout -b branch-name
```

**Step 4:** Make your changes and push them to a new branch on GitHub:

```bash
git add .  # if you have created new files
git commit -a -m "description of changes made"
git push --set-upstream origin branch-name
```

**Step 5:** Submit a pull request on GitHub when you are happy.

**Step 6:** Once merged with the `main` branch, ensure your local `main` branch reflects the new updates, and delete your branch. If you are working from a fork, click **Sync fork** on GitHub first.

```bash
git checkout main
git pull  # update main branch to include the merged changes
git branch -d branch-name  # delete the old branch
```

## Summary

<!-- ORIGINAL:
We have thougth about how
-->

We have thought about how `git` and GitHub allow teams to work on the same code without getting in each other's way. Branches let you develop changes in isolation from a working `main` branch; pull requests provide a way for those changes to be reviewed, discussed, and merged back in; and forks let anybody propose improvements to public projects without needing permission to push to them directly. 

In the exercises, you will put these skills into practice by contributing to a shared repository.
