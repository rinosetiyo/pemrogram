import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import SocialImage from '../assets/sosmed.jpg';

function Hero() {
    return (
        <div className="container my-4">
            <div className="position-relative">
                <img src={SocialImage} className="img-fluid rounded-4" alt="Hero Image"/>
                <div className="position-absolute top-0 start-0 w-100 h-100 bg-dark rounded-4" style={{ opacity: 0.5 }}></div>
                <div className="position-absolute bottom-0 text-white ps-3 mb-3">
                    <h1>Your Heading Here</h1>
                    <p>Your paragraph text goes here. This is an overlay text on the image.</p>
                </div>
            </div>
        </div>
    )
}

export default Hero;