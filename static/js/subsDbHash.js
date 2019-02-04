function subsdb(file, callback){
    r = new FileReader();
    readsize = 64 * 1024;
    filesize = file.size
    startBytes = file.slice(0, readsize)
    endBytes = file.slice(filesize-readsize, filesize)
    blob = new Blob([startBytes,endBytes])
    r.onload =function(e){
        if(e.target.result != null){
            data = e.target.result
            hash = md5(data);
            callback.call(file,hash);
        }
    }
    r.readAsArrayBuffer(blob);
}