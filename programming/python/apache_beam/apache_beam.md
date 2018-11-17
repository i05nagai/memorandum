---
title: Apache Beam
---

## Apache Beam

```
pip install apache-beam
# for GCP
pip install apache-beam[gcp]
# test
pip install apache-beam[test]
# doc
pip install apache-beam[docs]
```

## API
* bounded PCollection
    * batch
    * bounded sources (e.g. `TextIO`) do not provide timestamps
        * You can assign new timestamps to the elements of a PCollection
* unbounded PCollection
    * streaming
    * in unbounded PCollection, timestamp is added automatically
* PCollection
    * represents a collection of data, which could be bounded or unbounded in size.
* PTransform
    * represents a computation that transforms input PCollections into output PCollections.
* Pipeline
    * manages a directed acyclic graph of PTransform s and PCollection s that is ready for execution.
* PipelineRunner
    * specifies where and how the pipeline should execute.
* Read
    * read from an external source.
* Write
    * write to an external data sink.

* Flatten
    * Merge multiple `PCollection`s of the same type
* Join
    * `CoGroupByKey` transform in the Beam SDK perform a relational join between two PCollections
    * The `PCollection`s must be keyed (i.e. they must be collections of key/value pairs) and they must use the same key type.


### I/O

```
# read
lines = pipeline | beam.io.ReadFromText('gs://some/inputData.txt')
# write
output | beam.io.WriteToText('gs://some/outputData')
# transform
output_pc_collection_1 = input_pc_colelction | [Transform 1]
output_pc_collection_2 = input_pc_colelction | [Transform 2]
```

### Transform

* `ParDo`
    * analogous to Map phase of Map/Shuffle/Reduce-style algorithm
    * e.g.
        * Filtering a data set
            * filter rows or columns
        * Formatting or type-conversion each element in a dataset
        * Extracting parts of each element in a data set
            * your input PCollection contains elelents that are of a different type or format than you want
        * Performing computations on each element in a data set
            * simple computations on every elements of a PCollection and output resutls as a new PCollection
    * Applying `DoFn` for each record

```python
# The input PCollection of Strings.
words = ...

# The DoFn to perform on each element in the input PCollection.
class ComputeWordLengthFn(beam.DoFn):
  def process(self, element):
    return [len(element)]

# Apply a ParDo to the PCollection "words" to compute lengths for each word.
word_lengths = words | beam.ParDo(ComputeWordLengthFn())
```


* `DoFn`
    * [Requirement of DoFn class](https://beam.apache.org/documentation/programming-guide/#requirements-for-writing-user-code-for-beam-transforms)
    * Your function object must be serializable
        * serialized function is transmited to worker
        * Avoid loading a field with a large amount of data before serialization.
        * Individual instances of your function object cannot share data.
        * Mutating a function object after it gets applied will have no effect.
    * your function object must be thread-compatible, and be aware that the Beam SDK is not thread-safe
        * Beam SDKs are not thread safe
        * Each instance of your instance object is accessed by a single thread at a time on a worker instance, unless you explicitly create your own threads
    * your function obejct should be idempotent. Non-idempotent function is supporeted but havig side-effect
    * A given DoFn instance generally gets invoked one or more times to process some arbitrary bundle of elements
        * you can cache information across multiple calls to your processing method, but if you do so, make sure the implementation does not depend on the number of invocations

```python
word_lengths = words | beam.FlatMap(lambda word: [len(word)])
# Apply a Map with a lambda function to the PCollection words.
word_lengths = words | beam.Map(len)
```

* `GroupByKey`
    * analogous to the Shuffle phase of a Map/Shuffle/Reduce-style algorithm
* `CoGroupByKey`
    * join
* `CombineGlobally`
    * combining collections of elements or values in your data
    * `CombineGlobally().withoutDefaults()`
        * if the input is empty, this return an empty `PCollection`
    * `CombineGlobally().asSingletonView()`
        * the output is immediately converted to `PCollectionView`
* `CombineFn`
    * you need to override the following four functions
        * create_accumulator
        * add_input
            * this adds an input element to an accumulator, returing the accumlator value
        * merge_accumulators
            * merges sefveral accumulators
        * extract_output
* `Flatten`
* `Partition`
    * Divide the elements of `PCollection` according to a partitioning function

```python
class AverageFn(beam.CombineFn):
  def create_accumulator(self):
    # (sum_value, count_elem)
    return (0.0, 0)

  def add_input(self, sum_count, input):
    # return an accumator
    (sum, count) = sum_count
    return sum + input, count + 1

  def merge_accumulators(self, accumulators):
    # return merged accumulator
    sums, counts = zip(*accumulators)
    return sum(sums), sum(counts)

  def extract_output(self, sum_count):
    # extract outputs from merged accumator
    (sum, count) = sum_count
    return sum / count if count else float('NaN')
```


Create pipelines

* 1. Create a Pipeline object.
* Use a Read or Create transform to create one or more `PCollection`s for your pipeline data.
* Apply transforms to each `PCollection`.
    * Transforms can change, filter, group, analyze, or otherwise process the elements in a PCollection.
    * Each transform creates a new output PCollection, to which you can apply additional transforms until processing is complete.
* Write or otherwise output the final, transformed `PCollection`s.
* Run the pipeline.


### Coder
Python default coders corrensponding to Python types.

* int
    * VarIntCoder
* float
    * FloatCoder
* str
    * BytesCoder
* bytes
    * StrUtf8Coder
* Tuple
    * TupleCoder

Registe coders

```python
apache_beam.coders.registry.register_coder(int, BigEndianIntegerCoder)
```

### Windowing

* event time
    * determined by the timestamp on the data element itself
* processing time
    * determined by the clock on the system processing the element

* `FixedWindow(size, offset=0)`
    * [beam/window\.py at 01d8b922fbe355bc6818deebf83732ca20f79bce · apache/beam](https://github.com/apache/beam/blob/01d8b922fbe355bc6818deebf83732ca20f79bce/sdks/python/apache_beam/transforms/window.py#L319)
    * size
        * size of the window as seconds
    * offset
        * Offset of this window as seconds since Unix epoch
        * Windows start at `t=N * size + offset` where t=0 is the epoch
* `SlidingWindows(size, period, offset=0)`
    * `[N * period + offset, N * period + offset + size)`
    * size
        * Size of the window as seconds
    * period
        * Period of the windows as seconds
    * offset
        * The offset must be a value in range `[0, period)`
* `Sessions(gap_size)`
    * A session is defined as a series of consecutive events separated by a specified gap size.
    * gap_size
        * Size of the gap between windows as floating-point seconds.
* `GlobalWindows()`

### triger

## API
* [apache\_beam\.io\.gcp\.bigquery module — Apache Beam documentation](https://beam.apache.org/releases/pydoc/2.7.0/apache_beam.io.gcp.bigquery.html)
    * you need to define `GOOGLE_APPLICATION_CREDENTIALS`
* [apache\_beam\.io\.textio module — Apache Beam documentation](https://beam.apache.org/releases/pydoc/2.7.0/apache_beam.io.textio.html?highlight=readfrom#apache_beam.io.textio.ReadFromText)
    * you can read compressed text data directly
    * `file_pattern`
        * `gs://path/to/txt`
            * you need to define `GOOGLE_APPLICATION_CREDENTIALS`
    * `min_bundle_size`
    * `compression_type=auto`
    * `strip_trailling_newlines`
    * `validate`
    * `skip_header_lines`
    * `coder`
* `schema`
    * schema is required if you create table
    * schema is one of 
* `parse_table_schema_from_json(schema_string)`
    * create 


## Examples
* https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/windowed_wordcount.py
* [beam/fastavro\_it\_test\.py at 01d8b922fbe355bc6818deebf83732ca20f79bce · apache/beam](https://github.com/apache/beam/blob/01d8b922fbe355bc6818deebf83732ca20f79bce/sdks/python/apache_beam/examples/fastavro_it_test.py)
    * CoGroupByKey


## Reference
* [Apache Beam Python SDK](https://beam.apache.org/documentation/sdks/python/)
* [Beam Quickstart for Python](https://beam.apache.org/get-started/quickstart-py/)
* [Apache Beam SDK for Python — Apache Beam documentation](https://beam.apache.org/documentation/sdks/pydoc/2.6.0/)
