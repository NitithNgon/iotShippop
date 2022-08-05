const express = require('express');
const cors = require('cors');
const app = express();
const http = require('http');
const server = http.createServer(app);
const io = require('socket.io')(server, {
  cors: { origin: "*" }
});
var statusPI =false;
var imagePI ={imageSide1:{},imageSide2:{}}
const port = 80

app.use(cors());

io.on('connection', (socket) => {
  console.log('user connected')

  socket.emit('sendstatus', statusPI)
  socket.on('sendstatus',(status)=>{
    console.log("set pi status =",String(status))
    statusPI=status
    io.emit('sendstatus',status)
  })
  socket.on('disconnect',()=>{
    console.log('user disconnected')
  })

  socket.emit('image',imagePI)
  socket.on("image", imageFromPi =>{
    console.log(imageFromPi)
    if(imageFromPi.imageSide1 !== undefined){
      imagePI.imageSide1=imageFromPi.imageSide1
    }
    if(imageFromPi.imageSide2 !== undefined){
      imagePI.imageSide2=imageFromPi.imageSide2
    }
    io.emit('image',imagePI)
  })
});

server.listen(port, ()=>{
  console.log('listening port 80')
});
