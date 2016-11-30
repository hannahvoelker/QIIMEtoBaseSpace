# QIIMEtoBaseSpace
Inputs a QIIME microbiome data file. Outputs it into a file similar to that used in BaseSpace by Illumina. 

This program was written for the BioSeq[http://ase.tufts.edu/chemistry/walt/sepa/index.html] program at Tufts University.

## The inputs
** The file input must be a CSV! ** 
A QIIME file looks like this:
|#	Constructed	from	biom	file|			
|#OTUID|	EGMFfastqjoin.join.fastq |	EGMSfastqjoin.join.fastq | EGTCfastqjoin.join.fastq	| EGTFfastqjoin.join.fastq	| EGTSfastqjoin.join.fastq	| JRHWfastqjoin.join.fastq |	JRMRfastqjoin.join.fastq|
k__Bacteria;p__Cyanobacteria;c__Chloroplast;o__Stramenopiles;f__;g__|	0.238064797 |	0.069306309 |0 |	0.00149888 |	0.007999273 |	0.011911713 |	0.004956067 |

What's different from our desired output is that our sample names are messy, we have a complete listing from Kingdom all the way down to genus, and the values for each are decimal representations of percent.

## The outputs
This file outputs a CSV, called MicrobiomeCounts, which cleans up the sample names, gives the genus (or the lowest specific classification if left blank), and multiples each value by 100 so that we have the percent out of 100, which is more effective for other data analysis scripts written for microbiome studies within this program. Since we do not have the original total counts, like we did in BaseSpace, multiplying by 100 gives the percentage value, which is what we use in the R data charts. 
