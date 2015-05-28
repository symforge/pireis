# pireis
Piri Reis (pireis) Version Logger for Git for any kind of project


Pireis written in Python, allows you to create changelog file called `CHANGELOG.md` or `version.json` file for applications from Git Repositories. If you have tags like `v1.0` Pireis automatically grab them and only show from `x` version _to_ `y` version **differences** seperately. If no tag founds, all by done via commit tags.

**Note:** This code needs clean-up before gets stable.

### Usage

    cd myapp
    $ ./pireis.py

### Options

* `-f, --format`: Output format (Can be **json** or **md**)
* `-e, --expose`: Expose committer e-mail (If True, e-mail will be included in json/md file otherwise * `NULL`)
* `-s, --signed`: Remove Signed-Off-by: from commits for better look (Strip unnecessary signed off from comments)
* `-x, --extended`: Extended output for Markdown

#### Example

    $ ./pireis.py -f json -e -s -x

**Works on both Windows and Linux.**

#### Note

This is very first release of pireis. I have to do many code cleanup and additions to the core. If you want to contribute, fork it, make changes and request a pull.
