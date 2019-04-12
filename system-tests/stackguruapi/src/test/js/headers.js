function (args){
    //add security here
    var header = {};
    header["txid_header"] = java.util.UUID.randomUUID().toString();
    header["Content-Type"] = "application/json"
    return header
}