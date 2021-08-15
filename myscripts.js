var csv=document.getElementById('myfile').files[0];
var formData=new FormData();
formData.append("uploadCsv",csv);
var request = new XMLHttpRequest();

 //here you can set the request header to set the content type, this can be avoided.
 //The browser sets the setRequestHeader and other headers by default based on the formData that is being passed in the request.
 request.setRequestHeader("Content-type", "multipart/form-data"); //----(*)
 request.open("POST","/handleFile", true);
request.onreadystatechange = function (){
    if(request.readyState === XMLHttpRequest.DONE && request.status === 200) {
    console.log("yey");
    }
}

request.send(formData);
