# yamlformatter

A simple opionated yaml formatter that keeps your comments!

`yamlfmt` is just a cli wrapper around the [ruamel.yaml](https://bitbucket.org/ruamel/yaml) python library, which happens to have the unique quality of keeping comments.

Forked from:  
https://github.com/matthewdeanmartin/yamlfmt3  
who forked from:  
https://github.com/mmlb/yamlfmt  

Thanks for your work! <3

### Usage

**Note**:
The formatting used is subject to change without notice.
Once a format seems to stick v1.0 will be tagged and the format will not change.

```sh
❯ yamlformatter -h
usage: yamlformatter [-h] [-w] [file [file ...]]

positional arguments:
  file         file to parse

optional arguments:
  -h, --help            show this help message and exit
  -w, --write           overwrite file with formatted output
  -t WIDTH, --width WIDTH
                        set custom width
  --use-yaml-1-1        force yaml output to version 1.1
  -i INDENT, --indent INDENT
                        set indent for formatted output

```

### Examples

Lets see `yamlformatter` in action:

#### Simple example from ruamel.yaml docs
```sh
# example
name:
  # details
  family: Smith   # very common
  given: Alice    # one of the siblings
EOF
# example
name:
  # details
  family: Smith   # very common
  given: Alice    # one of the siblings
```

#### Travis-CI nodejs example
```sh
language: node_js

# test on two node.js versions: 0.6 and 0.8
node_js:
  - 0.6
  - 0.8

# configure notifications (email, IRC, campfire etc)
# please update this section to your needs!
notifications:
  irc: "irc.freenode.org#travis"
EOF
language: node_js

# test on two node.js versions: 0.6 and 0.8
node_js:
- 0.6
- 0.8

# configure notifications (email, IRC, campfire etc)
# please update this section to your needs!
notifications:
  irc: irc.freenode.org#travis
```
