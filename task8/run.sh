OUTPUT_DIR1=/user/${USER}/tasks/81
OUTPUT_DIR=/user/${USER}/tasks/8
OUTPUT_FILE=output.out

hdfs dfs -rm -r $OUTPUT_DIR1
hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_task8_job1 \
  -D mapred.reduce.tasks=1 \
  -input /data/small/imdb/title.basics.tsv \
  -input /data/small/imdb/title.ratings.tsv \
  -output $OUTPUT_DIR1 \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py

hdfs dfs -cat ${OUTPUT_DIR1}/part-* > job1.out
cat job1.out

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_task8_job2 \
  -D mapred.reduce.tasks=1 \
  -input ${OUTPUT_DIR1}/part-00000 \
  -output $OUTPUT_DIR \
  -mapper mapper2.py \
  -reducer reducer2.py \
  -file mapper2.py \
  -file reducer2.py

hdfs dfs -cat ${OUTPUT_DIR}/part-* > $OUTPUT_FILE
cat $OUTPUT_FILE
