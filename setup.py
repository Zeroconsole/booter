
import commands


def createconfig():
    print("To make the config file could you specify some things?\n")
    inputinterface = input("which Interface will you be using? \n")
    print("Your interface is now set to be "+inputinterface + "\n")
    inputHomeIP = raw_input("What is your Home IP address(Initial startup will be ready to run)")
    print("Your Home IP will be set to " + inputHomeIP + "\n You will be able to edit this within the Config file \n")




    Interface = inputinterface
    HomeIP = inputHomeIP


#to make config file or to not make
def TMconfig():
    if(checkconfig() == True):
        print("Returned True no config file will be made. . .")

    else:
        print("Returned False config file will be generated. . .")
        createconfig()


def checkconfig():
    try:

     f = open("config.txt")
     return True

    except:
        print("Checking for config file")
        return False

#Check() checks to see if Aircrack is on the system. pretty unconventional but it gets the job done.

def checkAir():

    air = commands.getstatusoutput('aircrack-ng')
    sair = str(air)
    aircrack = "Aircrack-ng 1.2 rc4 - (C) 2006-2015 Thomas d'Otreppe"

    if( aircrack in sair):

        print("Aircrack is Installed . . .")

    else:
        print("Error can't breath")


def checkNmap():
    meme = commands.getstatusoutput('nmap')
    smeme = str(meme)
    nmapr = "Nmap 7.40 ( https://nmap.org )"

    if(nmapr in smeme):
        print("Nmap is Installed . . .")
    else:
        print("Error program is lost")


def main():
    checkAir()
    checkNmap()
    checkconfig()
    TMconfig()

main()