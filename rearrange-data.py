import csv
import sys

filenames=sys.argv[1:-1]
outname = sys.argv[-1]
#filename="Summer2019 mp2 Genotypes Table.tsv"

genos = {}
all_markers = []

def load_file(fn):
    with open(fn, 'rb') as csvfile:
        data = csv.reader(csvfile, delimiter='\t')

        header = []
        for line in data:
            if len(header) == 0:
                header = line
                continue
            
            name= line[1].split('mp')[0]
            marker=line[3]
            allele1 = line[6]
            allele2 = line[7]

            if name not in genos.keys():
                genos[name]= {}
            genos[name][marker] = [allele1, allele2]

            if marker not in all_markers:
                all_markers.append(marker)


for filename in filenames:
    load_file(filename)
    
with open(outname, 'wb') as outfile:
    writer = csv.writer(outfile, delimiter=',')

    header_out = ['SampleName']
    for marker in all_markers:
        header_out.append(marker + '_1')
        header_out.append(marker + '_2')
    writer.writerow(header_out)
    
    for animal in genos.keys():
        outrow = [animal]
        for marker in all_markers:
            outrow += genos[animal][marker]
        writer.writerow(outrow)
        
