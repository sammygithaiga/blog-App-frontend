import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import AboutPage from './pages/AboutPage';
import BlogPost from './components/BlogPost';
import AddBlogPost from './components/AddBlogPost'; 
import './index.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/post/:id" element={<BlogPost />} />
          <Route path="/add" element={<AddBlogPost />} /> {}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
