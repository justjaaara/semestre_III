import express from 'express'

import cors from 'cors'


const app = express()

app.use(cors())

app.get('/:page', async (req,res)=> {


    const page =  req.params
    
    const data = await fetch( `https://rickandmortyapi.com/api/character/?page=${page}`)

    const dataToJson = await data.json()

    res.json(dataToJson)
})

app.listen(3000, () => console.log('Server hearing in 3000'))
