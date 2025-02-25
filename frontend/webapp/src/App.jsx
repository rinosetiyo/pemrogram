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
      <div className="container my-4 text-center">
        <h1
          className="text-primary fw-bold"
          style={{ fontSize: '2rem' }}
        >
          Untitled Design & Design Photography
        </h1>
      </div>
      <Hero />
      <div className="container mt-5 mb-4">
        <h5 className="">Featured Blog Posts</h5>
      </div>
      <Card />
      <Footer />
    </div>
  )
}

export default App
