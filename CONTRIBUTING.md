# Contributing to Alibaba Damo Academy Detection Toolkit (AdaDet)

Thanks for considering contributing!

(Some contents are borrowed from contributing guidelines of [AdaSeq](https://github.com/modelscope/AdaSeq))

# 1 How Can I Contribute?

## 1.1 Bug fixes and new features

**Did you find a bug?**

First, do [a quick search](https://github.com/modelscope/AdaDet/issues) to see whether your issue has already been reported.
If so, please comment on the existing issue.

Otherwise, open [a new GitHub issue](https://github.com/modelscope/AdaDet/issues).
Be sure to include a clear title and use the issue templates.
The description should include as much relevant information as possible.
The description should explain how to reproduce the erroneous behavior as well as the behavior you expect to see.
Ideally you would include a code sample or an executable test case demonstrating the expected behavior.

**Do you have a suggestion for an enhancement?**

We use GitHub issues to track enhancement requests.  Before you create an enhancement request:

* Make sure you have a clear idea of the enhancement you would like.  If you have a vague idea, consider discussing it first on a GitHub issue.

<!-- * Check the documentation to make sure your feature does not already exist. -->
* Check the code (documentation comming soon) to make sure your feature does not already exist.

* Do [a quick search](https://github.com/modelscope/AdaDet/issues) to see whether your enhancement has already been suggested.

When creating your enhancement request, please:

* Provide a clear title and description.

* Explain why the enhancement would be useful.  It may be helpful to highlight the feature in other libraries.

* Include code examples to demonstrate how the enhancement would be used.


<!-- ## 1.2 Contributor License Agreement ("CLA") -->


# 2 Making a pull request

When you're ready to contribute code to address an open issue, please follow these guidelines to help us be able to review your pull request (PR) quickly.

## 2.1 Initial setup (only do this once)

If you haven't already done so, please fork this repository on GitHub.

Then clone your fork locally with

    git clone https://github.com/USERNAME/adadet.git

or

    git clone git@github.com:USERNAME/adadet.git

Please replace `USERNAME` with your username. Both uppercased `/AdaDet.git` and lowercased `/adadet.git` are fine.

Finally, you'll need to create a Python 3 virtual environment suitable for working on `AdaDet`. The [`conda`](https://docs.conda.io/en/latest/miniconda.html) is the most common choices. Also, more environment setup details can be found in [install tutorial](./docs/install_EN.md).

Once your virtual environment is activated, you can code now! But please remember keep your fork up-to-date, see following sections.


## 2.2 Ensure your fork is up-to-date

Keeping your fork up-to-date is easy, just click the `Sync fork` and then `Update branch` on the github webpage of your fork (`https://github.com/USERNAME/AdaDet`).

Finally pull these changes to your local clone.


## 2.3 Create a new branch to work on your fix or enhancement

Commiting directly to the main branch of your fork is not recommended. It will be easier to keep your fork clean if you work on a seperate branch for each contribution you intend to make.

If your contribution involves additions to any public part of the API, we require that you write docstrings for each function, method, class, or module that you add.
See the [Comments and Docstrings of Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) section below for details on the syntax.


## 2.4 Test your changes

Our continuous integration (CI) are now running on internal platforms.
But you can run most of these tests locally, which is something you should do *before* opening a PR to help speed up the review process and make it easier for us.

We strive to reach high test coverage, so most contributions should include additions to [the unit tests](https://github.com/modelscope/adadet/tree/main/test).

For example, if you've fixed a bug in `adadet/deploy/smoke_det_deploy.py`, you can run the tests specific to that module with

    PYTHONPATH=. python tests/deploy/test_smoke_det_deplpy.py

You can also run all tests with

    PYTHONPATH=. python tests/run.py

to check multiple changes.

We use pre-commit hooks to ensure the code lints.
There are pre-commit hooks configured in the repository which you can install.
After installation, they will automatically run each time you commit.
An abbreviated guide is given below; for more information, refer to [the offical pre-commit documentation](https://pre-commit.com/).

Install `pre-commit` by running

    pip install pre-commit
    pre-commit install

And then just commit your changes, If there was a failure, you will get feedback, for example

    trim trailing whitespace.................................................Passed
    check yaml...............................................................Passed
    fix end of files.........................................................Passed
    fix requirements.txt.....................................................Passed
    fix double quoted strings................................................Failed
    - hook id: double-quote-string-fixer
    - exit code: 1
    - files were modified by this hook

    Fixing strings in setup.py

    check for merge conflicts................................................Passed
    fix python encoding pragma...............................................Passed
    mixed line ending........................................................Passed
    isort....................................................................Passed
    black....................................................................Failed
    - hook id: black
    - files were modified by this hook

    reformatted setup.py

    All done! ✨ 🍰 ✨
    1 file reformatted, 86 files left unchanged.

    flake8...................................................................Passed

Certain hooks modify your files to comply. To include these modifications, you will need to add them (i.e. git add ...) and commit again.

If all is well, you should see something like:

    trim trailing whitespace.................................................Passed
    check yaml...............................................................Passed
    fix end of files.........................................................Passed
    fix requirements.txt.....................................................Passed
    fix double quoted strings................................................Passed
    check for merge conflicts................................................Passed
    fix python encoding pragma...............................................Passed
    mixed line ending........................................................Passed
    isort....................................................................Passed
    black....................................................................Passed
    flake8...................................................................Passed

You can also manually run pre-commit

    # check several specific files
    pre-commit run --files a.py b.py c.yaml

    # check all files
    pre-commit run --all-files

<!-- And finally, please update the [CHANGELOG](https://github.com/modelscope/adadet/blob/main/CHANGELOG.md) with notes on your contribution in the "Unreleased" section at the top. -->


## 2.5 Open a pull request

After all of the above checks have passed, you can now open [a new GitHub pull request](https://github.com/modelscope/adadet/pulls).
Make sure you have a clear description of the problem and the solution, and include a link to relevant issues.

We look forward to reviewing your PR!
