OUTPUT_DIR=/user/${USER}/tasks/word_count
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_demo_word_count \
  -input /data/small/gutenberg \
  -output $OUTPUT_DIR \
  -mapper mapper.py \
  -combiner combiner.py \
  -reducer reducer.py \
  -file mapper.py \
  -file combiner.py \
  -file reducer.py

hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
cat $OUTPUT_FILE
