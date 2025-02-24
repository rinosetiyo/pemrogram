import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import SocialImage from '../assets/sosmed.jpg';

function Hero() {
    return (
        <div className="container my-4">
            <style>{`
                @media (max-width: 576px) {
                    .hero-img {
                        height: 60vh;
                        object-fit: cover;
                    }
                }
            `}</style>
            <div className="position-relative">
                <img
                    src={SocialImage}
                    className="img-fluid hero-img rounded-4"
                    alt="Hero Image"
                />
                <div
                    className="position-absolute w-100 bg-dark py-4 rounded-4 rounded-top-0"
                    style={{ bottom: '0', opacity: 0.7 }}
                >
                    <div className="d-flex flex-column px-3">
                        {/* Categories row */}
                        <div className="d-flex my-3">
                            <span className="btn btn-outline-light rounded-5 px-2 py-1 me-2">Category 1</span>
                            <span className="btn btn-outline-light rounded-5 px-2 py-1">Category 2</span>
                        </div>
                        {/* Title */}
                        <h1 className="text-white">Welcome to Our Blog</h1>
                        {/* Description */}
                        <p className="text-white">
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque vel corporis voluptatem deserunt ratione, unde consequuntur maxime!
                        </p>
                        {/* Top row: Circle image and name aligned center */}
                        <div className="d-flex align-items-center">
                            <img
                                src={SocialImage}
                                alt="Profile"
                                className="rounded-circle"
                                style={{ width: '40px', height: '40px', objectFit: 'cover' }}
                            />
                            <p className="text-white ms-3 mb-0">Your Name Here</p>
                        </div>
                        
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Hero;