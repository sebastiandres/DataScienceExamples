from core import data_source
import sys
import os

def list_of_json(city):
    target_file = "last_30.json"
    path = os.path.join("data", city)
    out_file = os.path.join("data", city, target_file)
    # Create a new file with an opening "["
    os.system('echo "[\n" > {0}'.format(out_file))
    first = True
    for my_file in os.listdir(path):
        if my_file!=target_file:
            if first==True:
                first=False
            else:
                os.system('echo "," >> {0}'.format(out_file))
            my_file_path = os.path.join(path, my_file)
            command = "cat {0} >> {1}".format(my_file_path, out_file)
            os.system(command)
    os.system('echo "]\n" >> {0}'.format(out_file))
    return

def main():
    if len(sys.argv)<2:
        print("Please provide the city")
	return sys.exit(-1)
    elif len(sys.argv)>2:
        print("Please provide only the city")
	return sys.exit(-1)
    else:
	city = sys.argv[1].title()
        # Do stuff
	list_of_json(city)

if __name__=="__main__":
    main()
