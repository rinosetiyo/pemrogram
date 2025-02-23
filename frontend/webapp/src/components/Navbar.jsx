import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';

function Navbar() {
    return (
        <div className="container-fluid shadow">
            <div className="container">
                <nav className="navbar navbar-expand-lg">
                    <div className="container-fluid">
                        <a className="navbar-brand" href="#">Pemrogram</a>
                        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                            <span className="navbar-toggler-icon"></span>
                        </button>
                        <div className="collapse navbar-collapse" id="navbarSupportedContent">
                            <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
                                <li className="nav-item mx-1">
                                    <a className="nav-link active" aria-current="page" href="#">Home</a>
                                </li>
                                <li className="nav-item mx-1">
                                    <a className="nav-link" href="#">Product</a>
                                </li>
                                <li className="nav-item mx-1">
                                    <a className="nav-link" href='#'>Interview</a>
                                </li>
                                <li className="nav-item mx-1">
                                    <a href="#" className="nav-link">Resources</a>
                                </li>
                                <li className="nav-item mx-1">
                                    <a href="#" className="nav-link">About</a>
                                </li>
                            </ul>
                            <div className="d-flex">
                                <button className="btn btn-outline-primary" type="submit">Get started</button>
                            </div>
                        </div>
                    </div>
                </nav>
            </div>
        </div>

    )
}

export default Navbar;