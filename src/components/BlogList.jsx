import React from 'react';
import { Link } from 'react-router-dom';


function BlogList() {

  const posts = [
    { id: 1, title: "First Post" },
    { id: 2, title: "Second Post" },
  ];

  return (
    <div>
      <h1 className="title">Blog Posts</h1>
      <ul className="content">
        {posts.map(post => (
          <li key={post.id}>
            <Link to={`/post/${post.id}`} className="post-title">
              {post.title}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BlogList;
