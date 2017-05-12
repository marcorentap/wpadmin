# wpadmin

wpadmin is an open source tool to discover the admins of a wordpress website.

## Installation

You can download the latest zip file by clicking [here](https://github.com/marcowen20/wpadmin/archive/master.zip)

Preferably, you can download sqlmap by cloning the Git repository:
```
git clone https://github.com/marcowen20/wpadmin.git wpadmin
```
wpadmin works with Python version 2.7.x and 3.5.x and above on any platform.

### Prerequisites

The python libraries **argparse** and **requests** are used. You can use pip to install it.

```
pip install argparse requests
```

## Usage

To run the tool use: 
```
python wpadmin.py [URL] [startID] [endID]
```
Where URL is the full URL of the wordpress website without the subdomain. It should be http://domain.com not http://www.domain.com
startID and endID determines the ID range of the scan

You can Ctrl+C any time to stop the scan. The tool will output all currently collected admins.

### Example usage
```
$python wpadmin.py http://anonhq.com/ 1 5

_ _ _ ___  ____ ___  _  _ _ _  _
| | | |__] |__| |  \ |\/| | |\ | by Marc owen
|_|_| |    |  | |__/ |  | | | \| https://github.com/marcowen20

[*] Use --help' for additional information
[*] URL: http://anonhq.com/
[*]startID: 1
[*]endID: 5

[*] ^C anytime to stop scanning
[+] Current scan ID: 1  http://anonhq.com/author/wpadmin/
[+] Current scan ID: 2  http://anonhq.com/author/anonvoid/
[*] Current scan ID: 3
[+] Current scan ID: 4  http://anonhq.com/author/anonwatcher/
[*] Current scan ID: 5

[+] Found admins:
ID      : Admin URL
1       : http://anonhq.com/author/wpadmin/
2       : http://anonhq.com/author/anonvoid/
4       : http://anonhq.com/author/anonwatcher/
```
