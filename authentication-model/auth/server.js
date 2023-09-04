const express = require('express');
const sqlite3 = require('sqlite3');
const bodyParser = require('body-parser');
const morgan = require('morgan');
const app = express();
const port = process.env.PORT || 3000;
const cors = require('cors');


app.use(cors());

const db = new sqlite3.Database('secret_keys.db');

app.use(bodyParser.json()); 
app.use(morgan('combined')); 

// Create a new secret key for the user registering his/her taps
app.post('/secret-keys', (req, res) => {
  const { key } = req.body;

  db.run('INSERT INTO secret_keys (key_value) VALUES (?)', [key], function (err) {
    if (err) {
      console.error(err.message);
      res.status(500).json({ error: 'Internal server error' });
      return;
    }
    console.log(`Inserted key with ID ${this.lastID}`);
    res.status(201).json({ message: 'Key recorded successfully' });
  });
});

app.get('/secret-keys', (req, res) => {
  
  db.all('SELECT * FROM secret_keys', [], (err, rows) => {
    if (err) {
      console.error(err.message);
      res.status(500).json({ error: 'Internal server error' });
      return;
    }
    res.json(rows);
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
