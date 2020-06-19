import re

import io

file = open("randomtext.txt.txt")

Read = file.read()

file.close()

ReplacedCCode = Read.replace("+91", "")

pattern = r"(\d\d\d\d\d\d\d\d\d\d)"

ExtractPhoneNos = re.findall(pattern,ReplacedCCode)

ExtractUniqPhoneNos = "\n\n".join(set(ExtractPhoneNos))

if ExtractPhoneNos >1:

	print("Extract Numbers Are :"+"\n\n"+ExtractUniqPhoneNos)

with io.FileIO("yogesh_processed.txt", "w") as file:

    file.write(ExtractUniqPhoneNos)








