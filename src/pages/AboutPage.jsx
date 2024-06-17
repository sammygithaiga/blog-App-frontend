import React from 'react';
import '../index.css'; // Import App.css for styles

function AboutPage() {
  return (
    <div className="about-page">
      <div className="container about-content">
        <h1 className="section-title">About Us</h1>
        <p>
          Welcome to our blog! We are passionate about sharing valuable insights and knowledge on various topics. Our goal is to provide informative and engaging content that inspires and educates our readers.
        </p>
        <p>
          Our team consists of dedicated writers who strive to deliver high-quality articles covering a wide range of subjects including technology, lifestyle, travel, and much more. Whether you're a seasoned enthusiast or just curious about a particular topic, we've got you covered!
        </p>
        <p>
          Feel free to explore our blog and discover a wealth of fascinating content. If you have any questions or suggestions, don't hesitate to reach out to us. Thank you for visiting!
        </p>
      </div>
    </div>
  );
}

export default AboutPage;
