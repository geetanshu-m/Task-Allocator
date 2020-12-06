const express = require('express');

const app = express();
const cors = require('cors');

const http = require('http').createServer(app);
const io = require('socket.io')(http, {
  cors: {
    origin: '*',
  },
});

const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors());
const tasks = [];

io.on('connection', (socket) => {
  console.log('a user connected');
  socket.on('disconnect', () => {
    console.log('user disconnected');
  });
});

app.post('/addTask', (req, res) => {
  // tasks.push(task)
//   console.log('request data', req.body);
  tasks.push(req.body);
  io.emit('message', req.body);
  res.send('Task Added');
});

app.get('/getTask', (req, res) => {
  res.send(tasks);
});

// console.log(io);
http.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
