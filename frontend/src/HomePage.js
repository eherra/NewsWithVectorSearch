import React, { useState } from 'react';
import './HomePage.css';
import LoadingIcon from './LoadingIcon';

const HomePage = () => {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(false);
  

  const handleSearch = (event) => {
    event.preventDefault();

  const searchTerm = event.target.querySelector('.search-input').value;
  setLoading(true)
  setTimeout(() => {
    setLoading(false);
    setNews(
      [
        { id: 1, title: 'Breaking News: Major Announcement', content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', url: 'https://www.google.com' },
        { id: 2, title: 'New Study Reveals Surprising Health Benefits of Chocolate', content: 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', url: 'https://www.google.com' },
        { id: 3, title: 'Tech Giants Unveil Cutting-Edge Gadgets at Annual Conference', content: 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.', url: 'https://www.google.com' },
        { id: 4, title: 'Sports: Exciting Match Ends in Overtime Victory', content: 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore.', url: 'https://www.google.com' },
        { id: 5, title: 'Politics: Government Approves New Policy Changes', content: 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit.', url: 'https://www.google.com' },
        { id: 6, title: 'Entertainment: Blockbuster Movie Breaks Box Office Records', content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', url: 'https://www.google.com' },
        { id: 7, title: 'Health: Tips for Staying Active and Fit at Home', content: 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', url: 'https://www.google.com' },
        { id: 8, title: 'Science: Researchers Make Breakthrough in Renewable Energy', content: 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.', url: 'https://www.google.com' },
        { id: 9, title: 'Business: Global Markets React to Economic Developments', content: 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore.', url: 'https://www.google.com' },
        { id: 10, title: 'Travel: Explore Beautiful Destinations for Your Next Vacation', content: 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit.', url: 'https://www.google.com' },
        { id: 11, title: 'Travel: Explore Beautiful Destinations for Your Next Vacation', content: 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit.', url: 'https://www.google.com' },
        
        // Add more mock news articles as needed
      ]
    )
  }, 1000);
    
  } 

  return (
    <div className="home-page">
      <div className="header">
        <span className="header-text">REALLY GOOD NEWS ONLY TODAY</span>
      </div>
      <form onSubmit={handleSearch} className="search-bar">
        <input type="text" className="search-input" />
        <input type="submit" className="search-button" value="Search" />
      </form>
      <div className="results-container">
        {news.map((article) => (
          <div className="news-article" key={article.id}>
            <h2 className="news-title">
              <a href={article.url} target="_blank" rel="noopener noreferrer">
                {article.title}
              </a>
            </h2>
            <div className="article-content">
              <p>{article.content}</p>
            </div>
          </div>
        ))}
        {loading && <LoadingIcon />}
      </div>
    </div>
  );
};

export default HomePage;
