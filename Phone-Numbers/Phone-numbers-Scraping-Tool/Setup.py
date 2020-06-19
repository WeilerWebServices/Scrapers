
         # Module for Acessing Regular Expressions

import re   

         # Module provides the interfaces to stream handling

import io    

         # Used for Opening && Reading of File name "randomtext.txt.txt" 

file = open("randomtext.txt.txt")

         # Content of a file that has been opened in text mode can be read using read method

Read = file.read()

         # Closing the file

file.close()

         # Method used For Replacing Country Code  the Specific String to No String

ReplacedCCode = Read.replace("+91", "")

         
        # Making of pattern for Searching the Digits (\d)

pattern = r"(\d\d\d\d\d\d\d\d\d\d)"

        # Matching Pattern used for all string present in file

ExtractPhoneNos = re.findall(pattern,ReplacedCCode)

        
        # Avoiding Duplication of Digits by Method used set() will create a set of unique letters in the string, and "".join() will join the letters.



ExtractUniqPhoneNos = "\n\n".join(set(ExtractPhoneNos))
        
        
        
         # if loop (Extract of Phone Numbers) should greater than 1 

if ExtractPhoneNos >1:

        
         # Printing of the Unique  Number Sequentially 
        
	print("Extract Numbers Are :"+"\n\n"+ExtractUniqPhoneNos)

	    
	     # Creation of New File named "yogesh_processed.txt" as file variable

with io.FileIO("yogesh_processed.txt", "w") as file:
    
        
          # Writing the data of Extract Phone numbers into new file named "yogesh_processed.txt"
    
    file.write(ExtractUniqPhoneNos)








