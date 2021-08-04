#packages contain all the files required for that module
# using camelcase package
#to install it go to command prompt and then write
#py -m pip install camelcase
# to uninstall any package
#py -m pip uninstall camelcase and then yes
import camelcase

x = camelcase.CamelCase()
a = "hi there !! this is to check whether the letters are capatlised or not"
print(x.hump(a))

#to check what all packages u have u have to write
#py -m pip list