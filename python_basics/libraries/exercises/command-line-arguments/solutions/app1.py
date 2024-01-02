import sys

argv = sys.argv[1:]

if "--help" in argv:
    print("This is help text.\n\n"
          "--help - outputs the help menu.\n"
          "--fast - allows you to enable fast mode."
          )
    
if "--fast" in argv:
    print("fast mode enabled.")
else:
    print("slow mode enabled.")
