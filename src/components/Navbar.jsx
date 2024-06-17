import React from 'react';
import { Link } from 'react-router-dom';
import '../index.css'; // Import App.css for styles

function Navbar() {
  return (
    <nav className="navbar">
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
        <li>
          <Link to="/add">Add Post</Link> {/* Add new link */}
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
