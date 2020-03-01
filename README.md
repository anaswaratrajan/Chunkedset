# Chunkedset

The ChunkedSet stores its elements in Chunks of size k. It behaves as a set and contains only unique values in all chunks combined. 

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
- Enter directory chunkedset
```
  cd chunked set
```
- Install requirements
```
  pip install -r requirements.txt
```
- Run the app 
```
  flask run
```
- Set data to chunk - POST 
```
  curl --header "Content-Type: application/json" \
   --request POST \
   --data '{"chunk":1,"data":[1,2,3,4,5]}' \
   http://127.0.0.1:5000/chunk1/setdata
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
