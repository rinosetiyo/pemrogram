import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Card from './components/Card'
import Footer from './components/Footer'

function App() {

  return (
    <div>
      <Navbar />
      <div className="container my-4">
        <h1>Untitled Design & Design Photography</h1>
        <p className='text-muted'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque vel corporis voluptatem deserunt ratione, unde consequuntur maxime! Vel saepe blanditiis porro accusamus, esse fugiat earum obcaecati adipisci labore facere. Expedita?</p>
      </div>
      <Hero />
      <div className="container mt-5 mb-4">
        <h5>Featured Blog Posts</h5>
      </div>
      <Card />
      <Footer />
    </div>
  )
}

export default App
