import util
import sys

print("This is argv:", sys.argv)
print("Number of arguements: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))
command = sys.argv[1]

print(command)
if command == "build":
	print("Build was specified")

	util.build_pages()
	print("Import successful")
# TODO: Do something here... elif command == "new":
# elif command == "new":
#     print("New page was specified")
# # TODO: Do something here... else:
else:
    print("Please specify ’build’ or ’new’")
