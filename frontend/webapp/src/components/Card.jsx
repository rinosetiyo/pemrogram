import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import sosmedImage from '../assets/sosmed.jpg';
import 'bootstrap/dist/js/bootstrap.bundle.min';

function Card() {
    return (
        <div className="container">
            <div className="row">
                <div className="col-md-4">
                    <div className="card">
                        <img src={sosmedImage} alt="card image" className="card-img-top" />
                        <div className="card-body">
                            <h5 className="card-title">
                                Ini adalah sebuah karya seni
                            </h5>
                            <p className="card-text text-muted">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Inventore vitae ducimus labore culpa voluptas, repudiandae quaerat at delectus ipsam nisi?</p>
                            <div className="d-flex align-items-center">
                                <img src={sosmedImage} alt="circle image" className="rounded-circle me-2" style={{ width: '40px', height: '40px' }} />
                                <p className="fw-semibold mb-0">Rino setiyo | 26 sep 2024</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Card;