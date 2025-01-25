import { useState } from 'react'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import Card from './components/Card'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <Navbar />
      <div className='container my-5'>
      <Card/>
        <h1 className='text-center'>Hello, world!</h1>
        <p className='text-center'>You clicked {count} times</p>
        <div className='d-flex justify-content-center'>
          <button onClick={() => setCount(count + 1)}>Click me</button>
        </div>
      </div>
      <Footer/>
    </div>
  )
}

export default App
