# @Author: ZwEin
# @Date:   2016-06-14 13:18:59
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-06-16 16:06:23

# test
# --input_file /user/lteng/phone-number-extractor/data/memex_data
# --output_dir /user/lteng/phone-number-extractor/data/spark_output

/usr/lib/spark/bin/spark-submit \
--master yarn-client \
--conf "spark.yarn.executor.memoryOverhead=8192" \
--conf "spark.shuffle.memoryFraction=0.5" \
--executor-memory 10g  --executor-cores 2  --num-executors 5 \
--py-files python_main.zip,python_lib.zip \
spark_workflow.py \
$@