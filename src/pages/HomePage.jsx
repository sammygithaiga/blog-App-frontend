import React from 'react';
import BlogList from '../components/BlogList';


function HomePage() {
  const featuredPosts = [
    { id: 1, title: "First Featured Post", excerpt: "This is a short description of the first featured post." },
    { id: 2, title: "Second Featured Post", excerpt: "This is a short description of the second featured post." },
  ];

  return (
    <div className="container">
      <section className="hero">
        <h1 className="hero-title">Welcome to My Blog</h1>
        <p className="hero-subtitle">Your daily dose of interesting articles</p>
        <button className="cta-button">Read the Latest Posts</button>
      </section>

      <section className="latest-posts">
        <h2 className="section-title">Latest Posts</h2>
        <BlogList />
      </section>

      <section className="featured-posts">
        <h2 className="section-title">Featured Posts</h2>
        <div className="posts-grid">
          {featuredPosts.map(post => (
            <div key={post.id} className="post-card">
              <h3 className="post-title">{post.title}</h3>
              <p className="post-excerpt">{post.excerpt}</p>
              <a href={`/post/${post.id}`} className="read-more">Read More</a>
            </div>
          ))}
        </div>
      </section>

      <section className="about">
        <h2 className="section-title">About This Blog</h2>
        <p className="about-content">This blog is all about sharing insightful articles on various topics. Stay tuned for regular updates!</p>
      </section>

      <section className="newsletter">
        <h2 className="section-title">Subscribe to Our Newsletter</h2>
        <form className="newsletter-form">
          <input type="email" placeholder="Enter your email" />
          <button type="submit">Subscribe</button>
        </form>
      </section>
    </div>
  );
}

export default HomePage;
