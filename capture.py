import re

capture1 = open('capture2.txt','r')

capture1 = capture1.read()
output = open('output1.txt','w')

[output.write("facebook" + '\n') for line in capture1.split('\n') if "facebook" in line]
#[output.write("washington" + '\n') for line in capture1.split('\n') if "washington" in line]
[output.write("mashery" + '\n') for line in capture1.split('\n') if "mashery" in line]
[output.write("mojio" + '\n') for line in capture1.split('\n') if "moj" in line]
[output.write("twilil" + '\n') for line in capture1.split('\n') if "twil" in line]
[output.write("zillow" + '\n') for line in capture1.split('\n') if "zill" in line]
[output.write("microsoft" + '\n') for line in capture1.split('\n') if "msdn" in line]
[output.write("amazon" + '\n') for line in capture1.split('\n') if "aws" or "amazon" in line]
[output.write("new relic" + '\n') for line in capture1.split('\n') if "relic" in line]
[output.write("microsoft" + '\n') for line in capture1.split('\n') if "msdn" in line]
[output.write("google" + '\n') for line in capture1.split('\n') if "google" in line]
[output.write("whitepages" + '\n') for line in capture1.split('\n') if "whitepages" in line]