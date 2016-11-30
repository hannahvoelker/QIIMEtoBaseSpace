
#!usr/bin/env python

# MakeCSVfile.py
#Author: Hannah Voelker
#Made: 10/14/16

import subprocess as sp 
import csv
import xlrd

# current data set: 
# each row is a bacteria, in the format 
# k__Bacteria;p__Proteobacteria;c__Betaproteobacteria;o__Burkholderiales;f__Comamonadaceae;g__Acidovorax
# each column is a sample name, in the format 
# EGMFfastqjoin.join.fastq
# the numbers are decmial percentages

# GOAL:
# Have the row be just the genus name
# Have the samples be just their sample name
INPUT_FILENAME = 'qiime.csv'
def main():
	inputs = readInput(INPUT_FILENAME)
	samples = inputs[0]
	genus = inputs[1]
	counts = inputs[2]
	makeCSV(samples, genus, counts)

def readInput(filename):
	# read in sample name strings, genus name strings, and counts
	with open(filename, 'r') as filer:
		filer.readline()
		ListofSamples = filer.readline().strip().split(',')[1:]
		cleanList = []
		for sample in ListofSamples:
			sample = sample.split('fastqjoin.join.fastq')
			cleanList.append(sample[0])
		listofGenus = []
		Counts = []
		for line in filer:
			currentLine = line.strip().split(',')
			listofGenus.append(currentLine[0].split(';')[-1])
			Counts.append(currentLine[1:]*100)

	return (cleanList, listofGenus, Counts)
def makeCSV(samples, genus, counts):
	print genus
	return

if __name__ == '__main__' :
	main()
