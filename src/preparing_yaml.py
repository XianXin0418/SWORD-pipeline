#!/usr/bin/env python3

#This program convert the sample table to yaml format and add it into the config.yaml

#Usage:
#preparing_yaml.py -s sampleTable.tsv -l [PE/SE] -o [Eu/Pr] -c config.yaml

import argparse
parser = argparse.ArgumentParser(description = "This program convert the sample table to yaml format and add it into the config.yaml.")
parser.add_argument('-s', dest = 'SampleTable', metavar = 'sampleTable.tsv', help = "sample table file", required = True, type = argparse.FileType('r'))
parser.add_argument('-l', dest = 'Layout', metavar = 'layout', help = "the layout of your sequence data, PE or SE [PE/SE]", required = True, type = str, choices = ["PE", "SE"])
parser.add_argument('-o', dest = 'Organism', metavar = 'organism', help = "which kind of organisms is your research object, eukaryote or prokaryote [Eu/Pr]", required = True, type = str, choices = ["Eu", "Pr"])
parser.add_argument('-a', dest = 'AlterSplic', metavar = 'alternativeSplicing', help = "whether to do the alternative splicing analysis, only valid in Eu organisms [true/false]", required = False, type = str, default = "false", choices = ["true", "false"])
parser.add_argument('-c', dest = 'Config', metavar = 'config.yaml', help = "config file", required = True, type = argparse.FileType('a'))
args = parser.parse_args()

line_list = []
for line in args.SampleTable:
	if not line.startswith("#"):
		line = line.strip()
		line_list.append(line)

sample_name_list = []
sample_treatment_list = []
for line in line_list:
	sample_name_list.append('"' + line.split("\t")[1] + '"')
	sample_treatment_list.append('"' + line.split("\t")[0] + '"')
print("sample_name: {", end = "", file = args.Config)
print(": '',".join(sample_name_list), end = "", file = args.Config)
print(": ''", end = "", file = args.Config)
print("}", file = args.Config)	
print("sample_treatment: {", end = "", file = args.Config)
print(": '',".join(sample_treatment_list), end = "", file = args.Config)
print(": ''", end = "", file = args.Config)
print("}", file = args.Config)

if args.Layout == "SE":
	sample_list = []
	for line in line_list:
		sample_list.append('"' + line.split("\t")[1] + line.split("\t")[2] + '"')
	print('layout: "SE"', file = args.Config)
	print("sample_list: {", end = "", file = args.Config)
	print(": '',".join(sample_list), end = "", file = args.Config)
	print(": ''", end = "", file = args.Config)
	print("}", file = args.Config)
elif args.Layout == "PE":
	fw_sample_list = []
	rv_sample_list = []
	for line in line_list:
		fw_sample_list.append('"' + line.split("\t")[1] + line.split("\t")[2] + '"')
		rv_sample_list.append('"' + line.split("\t")[1] + line.split("\t")[3] + '"')		
	print('layout: "PE"', file = args.Config)
	print("fw_sample_list: {", end = "", file = args.Config)
	print(": '',".join(fw_sample_list), end = "", file = args.Config)
	print(": ''", end = "", file = args.Config)
	print("}", file = args.Config)
	print("rv_sample_list: {", end = "", file = args.Config)
	print(": '',".join(rv_sample_list), end = "", file = args.Config)
	print(": ''", end = "", file = args.Config)
	print("}", file = args.Config)

print('organism: "' + args.Organism + '"', file = args.Config)
if args.Organism == "Eu":
	print('alternativeSplicing: "' + args.AlterSplic + '"', file = args.Config)
