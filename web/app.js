import path from 'path'
import express from 'express'

const port = 3000
const app = express()

app.use(express.static('static'))
app.set('views', path.join(__dirname, './views'))
app.set('view engine', 'pug')

app.get('/', (req, res) => {
  res.render('index', {
    title: 'Hey',
    message: 'I love it when a plan comes together!',
  })
})

app.listen(port, () => {
  console.log('Running!')
})
