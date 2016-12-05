#!usr/bin/env python

# MakeCSVfile.py
# Author: Hannah Voelker
# Made: 10/14/16

import subprocess as sp 
import csv
import re

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
		cleanList.append(' ')
		for sample in ListofSamples:
			sample = sample.split('fastqjoin.join.fastq')
			cleanList.append(sample[0])
		listofGenus = []
		Counts = []
		for line in filer:
			currentLine = line.strip().split(',')
			currbacterium = currentLine[0].split(';')
			currGenus = getGenus(currbacterium)
			listofGenus.append(currGenus)
			Counts.append(currentLine[1:])
	return (cleanList, listofGenus, Counts)

def getGenus(bacteria):
	for counter in range(len(bacteria)-1, 0, -1):
		if bacteria[counter] != 'g__' and counter == len(bacteria)-1:
			name = bacteria[counter].split('g__')[-1]
			return re.sub(r'[^\w]', '', name)
		elif bacteria[counter] != 'f__' and counter == len(bacteria) - 2:
			name =  bacteria[counter].split('f__')[-1]
			return re.sub(r'[^\w]', '', name)
		elif bacteria[counter] != 'o__' and counter == len(bacteria) - 3:
			name = bacteria[counter].split('o__')[-1]
			return re.sub(r'[^\w]', '', name)
		elif bacteria[counter] != 'c__' and counter == len(bacteria) - 4:
			name = bacteria[counter].split('c__')[-1]
			return re.sub(r'[^\w]', '', name)
		elif bacteria[counter] != 'p__' and counter == len(bacteria) - 5:
			name = bacteria[counter].split('p__')[-1]
			return re.sub(r'[^\w]', '', name)

def makeCSV(samples, genus, counts):
	outputFile = open('MicrobiomeCounts.csv', 'w')
	print genus
	filewriter = csv.writer(outputFile)
	filewriter.writerow(samples)
	for i in range(len(genus)):
		rowvector = []
		rowvector.append(genus[i])
		rowcounts = counts[i]
		for elem in rowcounts:
			elem = float(elem)*100
			rowvector.append(elem)
		filewriter.writerow(rowvector)
	return

if __name__ == '__main__' :
	main()
