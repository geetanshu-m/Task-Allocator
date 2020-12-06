const express = require('express');

const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
const tasks = [];

app.post('/addTask', (req, res) => {
  // tasks.push(task)
//   console.log('request data', req.body);
  tasks.push(req.body);
  res.send('Task Added');
});

app.get('/getTask', (req, res) => {
  res.send(tasks);
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
