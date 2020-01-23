import path from 'path'
import express from 'express'
import { renderToString } from 'react-dom/server'

import App from './client/App'
//const App = () => {}

const port = 3000
const app = express()

app.use(express.static('static'))
app.set('views', path.join(__dirname, './views'))
app.set('view engine', 'pug')

app.get('/', (req, res) => {
  const renderedComponent = renderToString(<App />)
  res.render('index', {
    renderedComponent,
  })
})

app.listen(port, () => {
  console.log(`Running on http://localhost:${port}`)
})
