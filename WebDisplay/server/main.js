var express = require('express');
var app = express();
const bodyParser = require("body-parser");
var server = require('http').Server(app);
var io = require('socket.io')(server);

var states = []

app.use(express.static(__dirname + "/../public"));
app.use(bodyParser.json());

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.post('/SetCounterState', function(req, res) {
  console.log(req.body)
  states = req.body
  io.sockets.emit('estadosServos', req.body);
  res.status(200).jsonp('');
});

io.on('connection', function(socket) {
  console.log('Alguien se ha conectado con Sockets');
  socket.emit('estadosServos', states);
});

server.listen(8012, function() {
  console.log("Servidor corriendo en http://localhost:8012");
});