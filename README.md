# Chunkedset

The ChunkedSet stores its elements in Chunks of size k. It behaves as a set and contains only unique values in all chunks combined.

The implementation works efficiently for any number of chunks.

ChunkedSet is implemented with 3 hash_tables. Each of which helps make it behave as a set of sets.

      Data_table -
          hash_table1 : key   :  datapoint
                        value :  (chunk, slots)
      Slot_table -
          hash_table2 : key   :  slots
                        value :  [list of chunks]
      Node_table -
          hash_table3 : key   :  chunks
                        value :  datapoints in tuple
                    

Table of contents
-------------
* [Description](#description)
* [Features](#features)
* [Requirements](#req)
* [Usage](#usage)

<a name="description"></a>
Description
-------------

<a name="features"></a>
Features
-------------
- Join : When a new chunk joins the ChunkedSet, all the duplicate values are deleted
- Leave : When a chunk leaves the ChunkedSet, all the values are migrated to the available slots in the rest of the chunks

<a name="req"></a>
Requirements
-------------
- flask

<a name="usage"></a>
Usage
-------------
- Clone the repo
```
  git clone https://github.com/anaswaratrajan/Chunkedset.git
```
- Install requirements
```
  pip install -r requirements.txt
```
- Enter directory chunkedset
```
  cd chunked set
```
- Run the app
```
  flask run
```
- Set data to chunk - POST
```
  http://127.0.0.1:5000/chunk/setdata
```
- Send join request to server - GET
```
  http://127.0.0.1:5000/chunk1/join
```
- Send leave request to server - GET
```
  http://127.0.0.1:5000/chunk1/leave
```
 Similar for other chunks ( chunk2, chunk3)


 curl --header "Content-Type: application/json" \
   --request POST \
   --data '{"chunk":1,"data":[1,2,3,4,5]}' \
   http://127.0.0.1:5000/chunk1/setdata
