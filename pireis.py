# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2015 Symforge (Gencer Genç)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from subprocess import Popen, PIPE
import json, collections, argparse, datetime, os, codecs

isWin = False

if 'nt' == os.name:
    isWin = True


html = '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'

needToBold = [
    'Fix', 'Fixed', 'Fixes', 'Bugfix',
    'Bugfixes', 'Added', 'Add', 'Rem',
    'Removed', 'Dep', 'Deprecated',
    'Feature', 'Changed', 'Chn', 'Imp',
    'Impr', 'Improved']

needToStrip = [' - ', ' * ', '*']

def createChangeLog(outputType: str = 'json', isExposeEmail: bool = False, remSignedOff = True, isExtended: bool = False):
    """
    Gets tags from git repo and apply them to changelog as json or MarkDown.
    If no tags found classic commit-based scheme used instead.
    """
    tags = {}
    commits = {}
    references = {}
    out = ""
    print("Starting...")
    if isWin:
        hasTags = Popen('git for-each-ref --sort="*authordate" --format="%(refname:short)" refs/tags', shell=True, stdout=PIPE).stdout.read().decode()
    else:
        hasTags = Popen('git for-each-ref --sort="*authordate" --format="%(refname:short)" refs/tags | grep -v "^$"#', shell=True, stdout=PIPE).stdout.read().decode()

    if hasTags.strip() == '':
        hasTags = None
    if hasTags is not None:
        hasTags = hasTags.strip().split('\n')
        print("Found: " + str(len(hasTags)) + " tag(s).")

        for i in hasTags:
            tags[len(tags)] = i
        tags = collections.OrderedDict(reversed(sorted(tags.items())))

        if len(tags) > 0:

            for key, tag in tags.items():
                if key - 1 < 0:
                    search = '"' + tag + '"'
                else:
                    search = '"' + tags[key - 1] + '".."' +  tag + '"'


                if isWin:
                    partialCommit = Popen('git log --pretty=format:" %h,;|,%H,;|,%cn,;|,%ce,;|,%cD,;|,%ct,;|,%s%n%n%-b,|;," ' + search + ' | findstr /v /C:"Merge branch"', shell=True, stdout=PIPE).stdout.read().decode()
                else:
                    partialCommit = Popen('git log --pretty=format:" %h,;|,%H,;|,%cn,;|,%ce,;|,%cD,;|,%ct,;|,%s%n%n%-b,|;," ' + search + ' | grep -v "Merge branch"', shell=True, stdout=PIPE).stdout.read().decode()
                partialCommit =  partialCommit.strip().split(',|;,')
                k = 0
                for i in partialCommit:
                    i = i.strip()
                    if not i or i.strip().strip('\n') == '':
                        continue

                    if remSignedOff is True:
                        i = i.split("Signed-off-by:")
                        i = i[0].strip().strip('\n')

                    i = i.split(',;|,')
                    if len(i) <= 3:
                        continue
                    if not isExposeEmail:
                        i[3] = None
                    else:
                        references[i[2]] = i[3]
                    if not tag in commits:
                        commits[tag] = {}
                        out += "\n####Version " + tag.strip('v') + " (" + datetime.datetime.fromtimestamp(int(i[5])).strftime('%d.%m.%Y') + ")\n"
                    if isExtended >= 3:
                        comment = "* [" + i[0] + "](../../commit/" + i[0] + ") - [[" + i[2] + "]]: " + i[6] + "\n"
                        commits[tag]["commit_h"] = i[1]
                        commits[tag]["by"] = i[2]
                        commits[tag]["date"] = i[4]
                        commits[tag]["date_unix"] = i[5]
                    elif isExtended == 2:
                        comment = "* **" + i[0] + "**: " + i[6] + "\n"
                        commits[tag]["commit_h"] = i[1]
                    else:
                        comment = "* " + i[6] + "\n"
                    commits[tag][int(k)] = {
                        'commit': i[0],
                        'email': i[3],
                        'comment': i[6]
                    }
                    for r in needToBold:
                        if r in comment:
                            comment = comment.replace(r, '**' + r + '**')
                    out += comment
                    k += 1
        else:
            print("Error on tags")
            exit(2)
    else:
        print("No Tags found. Switching to commit mode...")
        if isWin:
            partialCommit = Popen('git log --pretty=format:" %h,;|,%H,;|,%cn,;|,%ce,;|,%cD,;|,%ct,;|,%s%n%n%-b,|;,"  | findstr /v /C:"Merge branch"', shell=True, stdout=PIPE).stdout.read().decode()
        else:
            partialCommit = Popen('git log --pretty=format:" %h,;|,%H,;|,%cn,;|,%ce,;|,%cD,;|,%ct,;|,%s%n%n%-b,|;,"  | grep -v "Merge branch"', shell=True, stdout=PIPE).stdout.read().decode()

        partialCommit =  partialCommit.strip().split(',|;,')
        k = 0
        for i in partialCommit:
            i = i.strip()
            if not i or i.strip().strip('\n') == '':
                continue

            if remSignedOff is True:
                i = i.split("Signed-off-by:")
                i = i[0].strip().strip('\n')

            i = i.split(',;|,')
            if not isExposeEmail:
                i[3] = None
            else:
                references[i[2]] = i[3]

            print("COMMIT: " + i[0])
            out += "\n####" + i[0]  + " (" + datetime.datetime.fromtimestamp(int(i[5])).strftime('%d.%m.%Y') + ")\n"

            commits[i[0]] = {
                'commit': i[0],
                'email': i[3],
                'comment': i[6]
            }
            if isExtended >= 3:
                comment = "* [" + i[0] + "](../../commit/" + i[0] + ") - [[" + i[2] + "]]: " + i[6] + "\n"
                commits[i[0]]["commit_h"] = i[1]
                commits[i[0]]["by"] = i[2]
                commits[i[0]]["date"] = i[4]
                commits[i[0]]["date_unix"] = i[5]
            elif isExtended == 2:
                comment = "* **" + i[0] + "**: " + i[6] + "\n"

                commits[i[0]]["commit_h"] = i[1]
            else:
                comment = "* " + i[6] + "\n"

            for r in needToBold:
                if r in comment:
                    comment = comment.replace(r, '**' + r + '**')
            out += comment
            k += 1
    js = None
    if outputType == 'json':
        js = json.dumps(commits, indent=4, separators=(',', ': '))
    #sort_keys=True,
    else:
        out += "\n\n"
        if isExtended >= 3:
            for k, v in references.items():
                out += "[" + k + "]:mailto://" + v + "\n"

    filename = "CHANGELOG.md"
    if js is not None:
        filename = "version.json"
        out = js

    file = codecs.open(filename, "w", "utf-8")
    file.write(out)
    file.close()
    print('Done.')


"""
Start App
"""
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--format", help="Output format", type=str, default='json')
parser.add_argument("-e", "--expose", help="Expose committer e-mail", default=False, action='store_true')
parser.add_argument("-s", "--signed", help="Remove Signed-Off-by: from commits for better look", default=False, action='store_true')
parser.add_argument("-v", "--verbose", help="Extended output for Markdown", default=1, action='count')
args = parser.parse_args()
"""
Run definition
"""
# os.chdir(os.path.dirname(__file__))
# os.getcwd()

# zlib.decompress(base64.b64decode(html)).decode()

createChangeLog(args.format, args.expose, args.signed, int(args.verbose))