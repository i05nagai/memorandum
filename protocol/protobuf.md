---
title: protobuf
---

## protobuf

## CLI
- [Download Protocol Buffers  \|  Google Developers](https://developers.google.com/protocol-buffers/docs/downloads.html)
- [Install protobuf 3 on Ubuntu](https://gist.github.com/sofyanhadia/37787e5ed098c97919b8c593f0ec44d8)

```
protoc
```

Parse PROTO_FILES and generate output based on the options given:

```
protoc [OPTION] PROTO_FILES
```

```
protoc --python_out=. 
```

* -IPATH, --proto_path=PATH
    * Specify the directory in which to search for imports.  May be specified multiple times; directories will be searched in order.  If not given, the current working directory is used.
* --version
    * Show version info and exit.
* -h, --help
    * Show this text and exit.
* --encode=MESSAGE_TYPE       Read a text-format message of the given type from standard input and write it in binary to standard output.  The message type must be defined in PROTO_FILES or their imports.
* --decode=MESSAGE_TYPE       Read a binary message of the given type from standard input and write it in text format to standard output.  The message type must be defined in PROTO_FILES or their imports.
* --decode_raw                Read an arbitrary protocol message from standard input and write the raw tag/value pairs in text format to standard output.  No PROTO_FILES should be given when using this flag.
* --decode=MESSAGE_TYPE       Read a binary message of the given type from standard input and write it in text format to standard output.  The message type must be defined in PROTO_FILES or their imports.
* --decode_raw                Read an arbitrary protocol message from standard input and write the raw tag/value pairs in text format to standard output.  No PROTO_FILES should be given when using this flag.
* -oFILE,                     Writes a FileDescriptorSet (a protocol buffer,
* --descriptor_set_out=FILE defined in descriptor.proto) containing all of the input files to FILE.
* --include_imports           When using --descriptor_set_out, also include all dependencies of the input files in the set, so that the set is self-contained.
* --include_source_info       When using --descriptor_set_out, do not strip SourceCodeInfo from the FileDescriptorProto.  This results in vastly larger descriptors that include information about the original location of each decl in the source file as well as surrounding comments.
* --dependency_out=FILE       Write a dependency output file in the format expected by make. This writes the transitive set of input file paths to FILE
* --error_format=FORMAT       Set the format in which to print errors.  FORMAT may be 'gcc' (the default) or 'msvs' (Microsoft Visual Studio format).
* --print_free_field_numbers  Print the free field numbers of the messages defined in the given proto files. Groups share the same field number space with the parent message. Extension ranges are counted as occupied fields numbers.
* --plugin=EXECUTABLE
    * Specifies a plugin executable to use.  Normally, protoc searches the PATH for plugins, but you may specify additional executables not in the path using this flag.  Additionally, EXECUTABLE may be of the form NAME=PATH, in which case the given plugin name is mapped to the given executable even if the executable's own name differs.
* --cpp_out=OUT_DIR
    * Generate C++ header and source.
* --csharp_out=OUT_DIR
    * Generate C# source file.
* --java_out=OUT_DIR
    * Generate Java source file.
* --javanano_out=OUT_DIR
    * Generate Java Nano source file.
* --js_out=OUT_DIR
    * Generate JavaScript source.
* --objc_out=OUT_DIR
    * Generate Objective C header and source.
* --php_out=OUT_DIR
    * Generate PHP source file.
* --python_out=OUT_DIR
    * Generate Python source file.
* --ruby_out=OUT_DIR
    * Generate Ruby source file.


## proto3


```
syntax = "proto3";

message SearchRequest {
  string query = 1;
  int32 page_number = 2;
  int32 result_per_page = 3;
}
```

Import

```
// old.proto
// This is the proto that all clients are importing.
import public "new.proto";
import "project/other.proto";
```

## Value types
[Language Guide \(proto3\)  \|  Protocol Buffers  \|  Google Developers](https://developers.google.com/protocol-buffers/docs/proto3#scalar)

- double
- float
- int32
- int64
- uint32
- uint64
- sint32
- sint64
- fixed32
- fixed64
- sfixed32
- sfixed64
- bool
- string
- bytes


Enum

```
message SearchRequest {
  string query = 1;
  int32 page_number = 2;
  int32 result_per_page = 3;
  enum Corpus {
    UNIVERSAL = 0;
    WEB = 1;
    IMAGES = 2;
    LOCAL = 3;
    NEWS = 4;
    PRODUCTS = 5;
    VIDEO = 6;
  }
  Corpus corpus = 4;
}
```


## protolock
- https://github.com/nilslice/protolock


## Reference
- [Language Guide \(proto3\)  \|  Protocol Buffers  \|  Google Developers](https://developers.google.com/protocol-buffers/docs/proto3)
