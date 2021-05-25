import express from 'express';

const routes = require('./routes/index');

const app = express();

app.use('/', routes);
app.use('/students', routes);
app.use('/students/:major', routes);

app.listen(1245, () => {
  console.log('Example app listening at http://localhost:1245');
});

export default app;
