import sys
import os

args = sys.argv[1:] #? Removes python filename

data = {
    "path": "",
    "data": {}
}
try:
    data["path"] = args[0]
    data["data"]["name"] = args[1]

except IndexError:
    print("  ERR: Incorrect arguments supplied")
    print("  python htmltemplate.py <path: str> <title: str>")
    quit()


current_dir = os.getcwd()
for directory in data["path"].split("/")[:-1]:
    temp_directory = os.path.join(current_dir, directory)
    if not os.path.exists(temp_directory):
        os.mkdir(temp_directory)
    current_dir = temp_directory


html_data = ""
try:
    html_data = open("./template.html", "r").read()
except:
    print("  ERR: Cannot find template file")
    print("  Make sure template.html in in the current working directory")

with open(data["path"], "w") as f:
    to_write = html_data

    for replace_word, data in data["data"].items():
        replace_phrase = "{#@#}".replace("@", replace_word)

        to_write = to_write.replace(replace_phrase, data)

    f.write(to_write)
