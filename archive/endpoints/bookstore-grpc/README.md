# Google Cloud Endpoints Bookstore App in Python

[![Open in Cloud Shell][shell_img]][shell_link]

[shell_img]: http://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&page=editor&open_in_editor=endpoints/bookstore-grpc/README.md

## Installing the dependencies using virtualenv:

    virtualenv bookstore-env
    source bookstore-env/bin/activate

Install all the Python dependencies:

    pip install -r requirements.txt

Install the [gRPC libraries and tools](http://www.grpc.io/docs/quickstart/python.html#prerequisites)

## Running the Server Locally

To run the server:

    python bookstore_server.py

The `-h` command line flag shows the various settings available.

## Running the Client Locally

To run the client:

    python bookstore_client.py

As with the server, the `-h` command line flag shows the various settings
available.

## Generating a JWT token from a service account file

To run the script:

    python jwt_token_gen.py --file=account_file --audiences=audiences --issuer=issuer

The output can be used as "--auth_token" for bookstore_client.py

## Regenerating the API stubs

The bookstore gRPC API is defined by `bookstore.proto`
The API client stubs and server interfaces are generated by tools.

To make it easier to get something up and running, we've included the generated
code in the sample distribution.  To modify the sample or create your own gRPC
API definition, you'll need to update the generated code. To do this, once the
gRPC libraries and tools are installed, run:

    python -m grpc.tools.protoc \
        --include_imports \
        --include_source_info \
        --proto_path=. \
        --python_out=. \
        --grpc_python_out=. \
        --descriptor_set_out=api_descriptor.pb \
        bookstore.proto

## Running the server with gRPC <-> HTTP/JSON Transcoding

Follow the instructions for [Deploying a service using transcoding](https://cloud.google.com/endpoints/docs/transcoding#deploying_a_service_using_transcoding).