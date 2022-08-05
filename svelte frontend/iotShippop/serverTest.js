import express from 'express'
import { createServer } from 'http'
import { dirname } from 'path'
import { Server } from 'socket.io'
import { fileURLToPath } from 'url'
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const port = 3000
const app = express()

const server = createServer(app)
const io = new Server(server)

app.get('/', (req, res) => {
  res.sendFile(__dirname+'\\index.html');
});

io.on('connection', (socket) => {
  console.log('user connected')
  socket.emit('eventFromServer', 'Hello, World 👋')

  socket.on('disconnected',()=>{
    console.log('user disconnected')
  })
})


server.listen(port, ()=>{
  console.log('listening port 3000 :http://localhost:3000')
})