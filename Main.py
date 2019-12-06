import Utility


def main():
    utility: Utility.Utility = Utility.Utility()
    utility.read_list()
    utility.read_names()
    utility.write_list()
    
    #GUI
    GUI.display()


if __name__ == '__main__':
    main()
