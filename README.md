Here is a script to combine data from multiple GeneMapper outputs. It was written by Halie Rando in summer 2019 to make life a little easier for the Kukekova Lab research assistants! It was developed for the first run of plates (Kylie's project). 

If you ran the same animal for the same marker twice (i.e., if you redid analyses), you need to be careful with how you list your input files. If the same marker shows up twice for the same animal, only the second one will be written into the final output. Therefore, you probably want to list the files in order of when you ran each plate so that you don't swap good data for bad. If you want to change how this works, let me know and we can talk about what would be useful.

What you put in: GeneMapper outputs in .tsv format

What you get out: A single CSV file (which can be opened in Excel) containing the allele calls at each marker for each individual

This should work for both python2 and python3. The lab computers have python2 but your computer might have python3. Let me know if you have any problems.

##GETTING STARTED
1. Export your data from GeneMapper as a 'tsv' file (tsv stands for Tab-Separated Values). It is recommended that you save everything in a single folder. Take a note of exactly what that folder is named and where it is located -- you'll need this information later. NOTE to Emmarie: I don't remember exactly how this works. You might need to export it, open it in Excel, and then save it as a TSV. You can also save it as a CSV and just modify the line of code that opens it (line 32) to use delimiter=','
2. Download the script "rearrange-data.py" from this repository and save it in the same folder where you saved your data.

## MAC/LINUX USERS
To run the software, the easiest way is to:
1. Open your terminal
2. Make sure you have python installed by typing `python` to check. You can also look in the finder to see if you can find anything named python -- you might need to type python2 or python3
3. [Copy the path name corresponding to the folder where you saved your data.](https://www.switchingtomac.com/tutorials/osx/5-ways-to-reveal-the-path-of-a-file-on-macos/)
4. In your terminal, type `pwd`. This means "print working directory," and it tells you what folder your computer is currently looking at. If the folder is not the one where you have your GeneMapper data and script, you need to use the command `cd` to move to that folder. This is called the path. [This link](https://www.switchingtomac.com/tutorials/osx/5-ways-to-reveal-the-path-of-a-file-on-macos/) or [this link](https://macpaw.com/how-to/use-terminal-on-mac) might help you figure out how to do this.
5. Once the response you get to `pwd` matches the location of the folder where you have your files saved, you can run the script. In the terminal type: `python rearrange-data.py genemapperoutput1 genemapperoutput2 mydata.csv` where genemapperoutput1 is the name of the first output file you want to analyze, same for genemapperoutput2, and then mydata.csv is the name of where you want your new table saved. You can provide as many input files as you want, but the last name given is the output file.

## WINDOWS USERS
1. The simplest way to get Python will be to follow step three [here](https://software.rc.fas.harvard.edu/training/scraping/install/).
2. You need to make an input file that lists your input files, one name per line. The last line should be what you want the output file to be named. The file should be named "filenames.txt" and be in the same folder as the script.
3. Open IDLE, open the script, and then press the F5 key to run it. 

