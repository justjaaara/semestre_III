import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {

  const [characters, setCharacters] = useState([])

  const [page, setPage] = useState(1)

  const [filter, setFilter] = useState('')



  useEffect(() => {

    fetch(`http://localhost:3000/${page}`)
    .then(value => value.json())
    .then(data => setCharacters(data.results))
    

  },[page])

  const handleClick = (index) => {
    
    const newArray = [...characters]
    characters[index].status = newArray[index].status === "Alive" ? "Dead" : "Alive"
    
    setCharacters(newArray)
  }

  const delete_character = (e,index) => {
    e.stopPropagation()

    const newArray = [...characters]

    newArray.splice(index, 1)

    setCharacters(newArray)
  }

  const filterData = [...characters].filter((character) => character.name.toLowerCase().includes(filter.toLowerCase()))

  const prev_page = () => {
    setPage(page == 1 ? 1 : page - 1)
    }
  const next_page = () => {
    setPage(page + 1)
    }




  return (
    <>

    <button onClick={() => next_page()} className='button right'>+</button>
    <button className='button left' onClick={() => prev_page()}>-</button>
    
    <section>

    <label>Filtro: </label>
    <input type="text" onChange={(e) => setFilter(e.target.value)} style={{marginBottom: '10px'}} />

    </section>


      {

        filterData.map((character, index) => <div key={index} onClick={() => handleClick(index)}>
          <h1>{character.name}</h1>
          <h2>{character.gender}</h2>
          <h3>{character.status}</h3>
          <img src={character.image} alt={character.name} />
          <br></br>
          <button onClick={(e) => delete_character(e,index)}>Eliminar personaje</button>
        </div>)
      }
    </>
  )
}

export default App
