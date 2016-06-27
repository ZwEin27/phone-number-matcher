# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-14 13:18:53
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-06-25 18:52:07

"""
main entrance for spark workflow

"""

"""
--input_file /user/worker/hbase-dump-2015-10-01-2015-12-01-aman/hbase
--output_dir /user/worker/hbase-dump-2015-10-01-2015-12-01-aman/extracted_phones

--output_dir /user/lteng/phone-number-extractor/data/spark_output_text_distinct


--input_file /user/worker/hbase-dump-2016-06-15/data
--output_dir /user/worker/hbase-dump-2016-06-15/extracted_phones

sample script:

spark-submit \
--conf "spark.yarn.executor.memoryOverhead=8192" \
--conf "spark.rdd.compress=true" \
--conf "spark.shuffle.compress=true" \
--driver-memory 6g \
--executor-memory 6g  --executor-cores 4  --num-executors 20 \
spark_workflow.py \
--input_file /Users/ZwEin/job_works/StudentWork_USC-ISI/projects/phone-number-matcher/tests/data/memex_data \
--output_dir /Users/ZwEin/job_works/StudentWork_USC-ISI/projects/phone-number-matcher/tests/data/spark_output

"""
import json
import sys
import os
import argparse
from pyspark import SparkContext, SparkConf, SparkFiles
from digSparkUtil.fileUtil import FileUtil
from pnmatcher import PhoneNumberMatcher

def load_jsonlines(sc, input, file_format='sequence', data_type='json', separator='\t'):
    fUtil = FileUtil(sc)
    rdd = fUtil.load_file(input, file_format=file_format, data_type=data_type, separator=separator)
    return rdd

def save_jsonlines(sc, rdd, output_dir, file_format='sequence', data_type='json', separator='\t'):
    fUtil = FileUtil(sc)
    fUtil.save_file(rdd, output_dir, file_format=file_format, data_type=data_type, separator=separator)

def extract_content(raw):
    if not raw:
        return ''
    content = []
    if isinstance(raw, basestring):
        content.append(raw)
    else:
        content = [_ for _ in raw if _ != None]
    return ' '.join(content)

def run(sc, input_file, output_dir):

    def map_load_data(data):
        key, json_obj = data
        extractions = json_obj['extractions']

        # load doc id
        if 'doc_id' in json_obj:
            doc_id = json_obj['doc_id']

        # load url
        url = ""
        if 'url' in json_obj:
            content = json_obj['url']
            if content:
                url = extract_content(content)

        # load and combine title and text content
        text_data = [] 
        title = ""
        if 'title' in extractions and 'results' in extractions['title']:
            content = extractions['title']['results']
            if content:
                title = extract_content(content)
                text_data.append(title)
        text = ""
        if 'text' in extractions and 'results' in extractions['text']:
            content = extractions['text']['results']
            if content:
                text = extract_content(content)
                text_data.append(text)
        text_data = ' '.join(text_data)

        # for test only
        # phonenumber = None
        # if 'phonenumber' in extractions and 'results' in extractions['phonenumber']:
        #     phonenumber = extract_content(extractions['phonenumber']['results'])

        # in production
        return (str(key), [url, text_data])

        # in test
        # return (key, [url, text_data, phonenumber])

    def map_extract_phone_number(data):
        # in production
        key, (url, text) = data

        # in test
        # key, (url, text, phonenumber) = data

        matcher = PhoneNumberMatcher()
        url_phone_numbers = matcher.match(url, source_type='url')
        text_phone_numbers = matcher.match(text, source_type='text')

        result_ht = {}
        result_ht["doc_id"] = key
        result_ht["url"] = url        
        result_ht["url_phone_numbers"] = url_phone_numbers
        result_ht["text_phone_numbers"] = text_phone_numbers

        # return (key, json.dumps(result_ht))
        return (key, result_ht)

    def map_extraction_frequence(data):
        key, json_obj = data
        url = json_obj['url']
        url_phone_numbers = json_obj['url_phone_numbers']
        text_phone_numbers = json_obj['text_phone_numbers']
        phone_numbers = url_phone_numbers + text_phone_numbers
        for phone_number in phone_numbers:
            # yield (str(phone_number)+'___'+url, 1)
            yield (phone_number, 1)

    rdd = load_jsonlines(sc, input_file)
    rdd = rdd.map(map_load_data).map(map_extract_phone_number)
    
    # test purpose
    # rdd = rdd.flatMap(map_extraction_frequence).distinct()
    # rdd = rdd.flatMap(map_extraction_frequence).reduceByKey(lambda v1,v2:v1+v2).sortBy(lambda a: a[1], False)

    # rdd.saveAsTextFile(output_dir)
    # save_jsonlines(sc, rdd, output_dir, file_format='text', data_type='json')
    save_jsonlines(sc, rdd, output_dir, file_format='sequence', data_type='json')

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-i','--input_file', required=True)
    arg_parser.add_argument('-o','--output_dir')#, required=True)

    args = arg_parser.parse_args()

    spark_config = SparkConf().setAppName('PhoneNumberMatcher')
    sc = SparkContext(conf=spark_config)

    run(sc, args.input_file, args.output_dir)

