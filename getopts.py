import getopt, sys

def main():
    try:
	opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
	print opts, args
    except getopt.GetoptError as err:
	print str(err)
	usage()
	sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
	if o == '-v':
	    verbose = True
	elif o in ("-h", "--help"):
	    usage()
	    sys.exit()
	elif o in ("-o", "--output"):
	    output = a
	else:
	    assert False, "unhandled option"

if __name__ == "__main__":
    main()
