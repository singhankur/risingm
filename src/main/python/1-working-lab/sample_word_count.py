import sys

from pyspark import SparkContext, SparkConf



# This program demonstrate a simple word count example
# 1. Map function flatMap, map
# 2. Reduce function reduceByKey
# 3. Filter function
if __name__ == "__main__":

  # create Spark context with empty spark configuration
  # SparkConf() - configurations provided to spark to run this application
  conf = SparkConf().setAppName("Sample spark word count")
  # SparkContext - A context created by the spark to run the application
  sc = SparkContext(conf=conf)

  # read in text file and split each document into words
  # text file is provide as the argument when we run this program  = sys.argv[1]
  # Mapper function flatMap -> maps one to many output [Each line got split in to multiple words]
  # "king am king" -> flatMap ["king","am","king"] generates 3 output from one line
  tokenized = sc.textFile("files/spark-defaults.conf").flatMap(lambda line: line.split(" "))

  # count the occurrence of each word
  # Map function mapped each word to a tuple of count 1
  # ["king","is","king"]  map==> [("king",1) , ("is", 1), ("king",1)]
  # reduceByKey => key is the word in the tuple so same key grouped and added their value
  # [("king",1) , ("is", 1), ("king",1)]  ==> [ ("is", 1), ("king",2)]
  wordCounts = tokenized.map(lambda word: (word, 1)).reduceByKey(lambda v1,v2:v1 +v2)

  # get threshold
  # Read the second argument to set filter
  threshold = int(sys.argv[2])
  # filter out words with fewer than threshold occurrences
  filtered = wordCounts.filter(lambda pair:pair[1] >= threshold)

  list = filtered.collect()
  print repr(list)[1:-1]