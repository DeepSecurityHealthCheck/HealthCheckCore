Contributing    {#contributing}
============

We welcome your contributions to Deep Security Health Check! This doc describes the process to contribute patches to DSHC (Deep Security Health Check) and the general guidelines we expect contributors to follow.

## Before You Start
We accept patches in the form of github pull requests. If you are new to
github, please read [How to create github pull requests](https://help.github.com/articles/about-pull-requests/)
first.

### Contributor License Agreements
Contributions to this project will be automatically be assumed as GNU LESSER GENERAL PUBLIC LICENSE (This project license).



# Contributing Process
Most pull requests should go to the master branch and the change will be
included in the next major/minor version release (e.g., 3.6.0 release).

For each pull request, a DSHC team member will be assigned to review the
pull request. For minor cleanups, the pull request may be merged right away
after an initial review. For larger changes, you will likely receive multiple
rounds of comments and it may take some time to complete. We will try to keep
our response time within 7-days but if you don’t get any response in a few
days, feel free to comment on the threads to get our attention. We also expect
you to respond to our comments within a reasonable amount of time. If we don’t
hear from you for 2 weeks or longer, we may close the pull request. You can
still send the pull request again once you have time to work on it.

Once a pull request is merged, we will take care of the rest and get it into
the final release.

## Coding Style
This project *aims* to follows [PEP-8 Coding Style Guides](https://www.python.org/dev/peps/pep-0008/).
Before sending out your pull request, please familiarize yourself with the
corresponding style guides and make sure the proposed code change is style
conforming.

## Code reviews
All submissions, including submissions by project members, require review. We
use Github pull requests for this purpose.

## Pull Request Guidelines
Some tips for good pull requests:
* Use our code
  [style guide](https://www.python.org/dev/peps/pep-0008/).
  When in doubt, try looking for other good style guides like [Google style guide](https://google.github.io/styleguide/pyguide.html).
* Write a descriptive commit message. What problem are you solving and what
  are the consequences? Where and what did you test? Some good tips:
  [here](http://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message)
  and [here](https://www.kernel.org/doc/html/v4.17/process/submitting-patches.html).
* If your PR consists of multiple commits which are successive improvements /
  fixes to your first commit, consider squashing them into a single commit
  (`git rebase -i`) such that your PR is a single commit on top of the current
  HEAD. This make reviewing the code so much easier, and our history more
  readable.
* Create small PRs that are narrowly focused on addressing a single concern.
  We often receive PRs that are trying to fix several things at a time, but if
  only one fix is considered acceptable, nothing gets merged and both author's
  & review's time is wasted. Create more PRs to address different concerns and
  everyone will be happy.
* For speculative changes, consider opening an issue and discussing it first.
  If you are suggesting a behavioral or API change, make sure you get explicit
  support from a DSHC team member before sending us the pull request.
* Provide a good PR description as a record of what change is being made and
  why it was made. Link to a GitHub issue if it exists.
* Don't fix code style and formatting unless you are already changing that
  line to address an issue. PRs with irrelevant changes won't be merged. If
  you do want to fix formatting or style, do that in a separate PR.
* Keep your PR up to date with upstream/master (if there are merge conflicts,
  we can't really merge your change).
* All tests need to be passing before your change can be merged. We recommend
  you run tests locally before creating your PR to catch breakages early on.
  Ultimately, the green signal will be provided by our testing infrastructure.
  The reviewer will help you if there are test failures that seem not related
  to the change you are making.


## Commit Guideline
* Consider using `ADD`, `UPD`, `FIX`, `REM` tags before the commit description
  to indicate what is the objective of the commit, ex. `ADD: Added new rocket launcher feature to the beam system after noticing that ants could exploit the Foom Generator using the Maxwell Injector.`
* Use concise descriptions that explain what is inside each commit.
* Commits may have multiple tags for each modification.
