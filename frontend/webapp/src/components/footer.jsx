import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';

const Footer = () => {
    const currentYear = new Date().getFullYear();
    return (
        <footer className="bg-dark text-white text-center py-3">
            <div className="container">
                <p>&copy; {currentYear} Your Company. All rights reserved.</p>
            </div>
        </footer>
    );
};

export default Footer;