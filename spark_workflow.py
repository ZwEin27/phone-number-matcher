"""

sample script:

spark-submit spark_workflow.py -i /Users/ZwEin/job_works/StudentWork_USC-ISI/projects/phone-number-matcher/tests/data/memex_data --output_dir /Users/ZwEin/job_works/StudentWork_USC-ISI/projects/phone-number-matcher/tests/data/spark_output



"""



import spark
import sys
import os
import argparse
from pyspark import SparkContext, SparkConf, SparkFiles

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-i','--input_file', required=True)
    arg_parser.add_argument('-o','--output_dir')#, required=True)

    args = arg_parser.parse_args()

    spark_config = SparkConf().setAppName('WEDC')
    sc = SparkContext(conf=spark_config)

    spark.run(sc, args.input_file, args.output_dir)

