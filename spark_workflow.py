# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-14 13:18:53
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-06-15 14:35:17

"""
main entrance for spark workflow

"""

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

