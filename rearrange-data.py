import csv
import sys

filenames=sys.argv[1:-1] #provide the program with the file names for each GeneMapper output
outname = sys.argv[-1] #where do you want the output saved?
#filename="Summer2019 mp2 Genotypes Table.tsv" #example from Kylie's data

genos = {} #dictionary to store the genotypes for each individual
all_markers = [] #list of all the markers found in your data

def load_file(fn):
    """Purpose: This function opens a GeneMapper output file (exported as a tsv) and reads in the data
    Input: a string containing the file name, as supplied in standard input
    Output: Adds data to global variables genos and all_markers"""
    
    with open(fn, 'rb') as csvfile:
        data = csv.reader(csvfile, delimiter='\t') #if your data is not in tsv format, you can modify the delimiter to a comma, etc. here

        header = []
        for line in data:
            if len(header) == 0: #the first line of the file is the header
                header = line
                continue
            
            name= line[1].split('mp')[0] #sample ID
            marker=line[3] #marker name
            allele1 = line[6] #call 1
            allele2 = line[7] #call 2

            if name not in list(genos): #if this individual doesn't have genotype calls already
                genos[name]= {}
            genos[name][marker] = [allele1, allele2] #add the allele calls for this marker for this individual

            if marker not in all_markers: #if the marker hasn't already been analyzed, add it to the list of markers
                all_markers.append(marker)


for filename in filenames: #here the program loads in all the filenames you supplied
    load_file(filename) #this is calling the function "load_file" that you can see above
    
with open(outname, 'wb') as outfile: #writing all the data into a csv file
    writer = csv.writer(outfile, delimiter=',') #this is a csv file, so ',' delimited. You can change if you'd like.

    header_out = ['SampleName'] #Start the header with the column name "SampleName"
    for marker in all_markers: #for each marker, we are going to have 2 allele calls
        header_out.append(marker + '_1')
        header_out.append(marker + '_2')
    writer.writerow(header_out) #write the header
    
    for animal in list(genos): #for each individual animal
        outrow = [animal] #the first columns is the name of the individual
        for marker in all_markers: #for each marker, write the allele calls in order
            outrow += genos[animal][marker]
        writer.writerow(outrow) #write the data for this individual
        
