# SWORD-pipeline
Snakemake Workflow of RNA-Seq Data Analysis

Requirement:
pre-installed Docker Engine
Illumina sequencing file (.fastq, .fq, .fastq.gz, or .fq.gz)
download link of reference genome and annotation file (optional)

Step 1:
fill the sampleTable.tsv file based on your samples, fill the congif.yaml file according to your requirement, and use the preparing_yaml.py script to generate the final configuration file.
usage: preparing_yaml.py [-h] -s sampleTable.tsv -l layout -o organism
                         [-a alternativeSplicing] -c config.yaml

This program convert the sample table to yaml format and add it into the config.yaml.

optional arguments:
  -h, --help            show this help message and exit
  -s sampleTable.tsv    sample table file
  -l layout             the layout of your sequence data, PE or SE [PE/SE]
  -o organism           which kind of organisms is your research object,
                        eukaryote or prokaryote [Eu/Pr]
  -a alternativeSplicing
                        whether to do the alternative splicing analysis, only
                        valid in Eu organisms [true/false]
  -c config.yaml        config file
  
  Step 2:
  pull the Docker image xianxin1994/sword:1.1 into your local computer
  usage: docker pull xianxin1994/sword:1.1
  
  Step 3:
  use different Snakmefile based on your analysis requirement to execute the one-step analysis
  usage: docker run --rm -v /ABSOLUTE/PATH/TO/SWORD/:/sword/ xianxin1994/sword:1.1 snakemake -s SNAKEFILE 
  
