const express = require('express');
const app = express();
const fs = require('fs');
const path = require('path');

app.use(express.urlencoded({extended:true})); app.use(express.json());
app.use(express.static( __dirname ));

app.get("/output", (req, res)=>{
  fs.readFile("./index.html", (err, html)=>{
    if(err){  throw err }
    res.writeHead(200, {'Content-type':'text/html'});
    res.write(html);
    res.end();
  });
});

app.get("/rawdata", (req, res)=>{
  fs.readFile( path.join("..", "output", "output.json"), (err, data)=>{
    if(err){  throw err }
    let json = JSON.parse(data);
    res.json(json);
    res.end();
  });
});
app.listen(4000)
