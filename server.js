// jshint esversion:6

const express = require("express");
var multer = require('multer');
var csv = require('fast-csv');
const fs = require('fs');
const http = require('http');
const bodyParser = require('body-parser');
const app = express();


app.use(bodyParser.urlencoded({
  extended: true
}));
app.set('view engine', 'ejs');
var storage = multer.memoryStorage();
const upload = multer({
  dest: 'tmp/csv/'
});

app.get("/", function(req, res) {
  res.sendFile(__dirname + "/index.html");
});
app.post("/", upload.single('avatar'), function(req, res, next) {
  var orderDate;
  var region;
  var city;
  var category;
  var product;
  var quantity;
  var unitPrice;
  var totalPrice;
  var testDetails = [];
  var bookTitles = []
  const fileRows = [];
  csv.parseFile(req.file.path)
    .on("data", function(data) {
      fileRows.push(data); // push each row
    })
    .on("end", function() {
      console.log(fileRows);
      console.log(typeof(fileRows));
      console.log(fileRows[1]);
      fileRows.shift();
      console.log(fileRows);
      // display result page
      res.render('data.ejs', {
        fileRows: fileRows
      })
      fs.unlinkSync(req.file.path); // remove temp file
      //process "fileRows" and respond
    })




  // res.sendFile(__dirname + "/index.html");
});

app.listen(3000, function() {
  console.log("Server started on port 3000");
});
