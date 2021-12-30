# akpsi-pi-chi
Programming and other CS-based resources used by the Pi Chi Chapter of Alpha Kappa Psi Pre-Professional Business Fraternity.

## brb
Files for the maintenance of chapter resources.
* 'Bank-Template' contains a directory outline for the chapter's resume bank
* 'brb-dirs' is a bash script that reads in accompanying .txt files 'freeman.txt,' 'sla.txt,' and 'sse.txt' to automate the creation of the 'Bank-Template' directory in case it is ever lost or deleted
	* Requires 'Season-Year' to be passed as a command line argument, e.g. Fall-2021
	* See file's comments to view file specifications for the script to run properly
	* `$ bash brb-dirs Season-Year` to run
* 'space-to-hyphen.py' is a Python script that converts the spaces within a file to hyphens
	* Requires command line argument of filename; this file is overwritten upon running of the script
* '\*.txt' files should contain the department names as specified on the Tulane University website, which can be found [here](https://catalog.tulane.edu/schools-departments-colleges/)

## orgs
Files for the creation of an alphabetized list of Brother involvements in student orgs or other commitments.
* 'alphabetize.py' is a Python script that takes in a .txt file as a command line argument, sorts its lines alphabetically, and places the sorted order of lines into a new file, 'sorted.txt'
	* Sorting algorithm is a modified Quicksort

## qr
Files for the autonomous generation of QR codes used for rush lanyards.
* 'qr.py' is a Python script that reads in specific .txt files and generates QR codes based on their data
	* `$ python3 qr.py` to run
* Requires .txt files to be properly formatted
	* Lines of each file should correspond to same observation
* Note: should be updated with Pandas/NumPy in future to avoid .txt files altogether
* Warning: **DO NOT PUSH .txt FILES TO REPO WITH PERSONAL INFORMATION**
