import React, { useState } from "react";
import "./HomePage.css";
import LoadingIcon from "./LoadingIcon";

const HomePage = () => {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (event) => {
    event.preventDefault();
    const searchTerm = event.target.querySelector(".search-input").value;
    setLoading(true);

    await fetch("/api/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ searchInput: searchTerm }),
    })
      .then((res) => res.json())
      .then((d) => {
        const dataJson = JSON.parse(d);
        setNews(dataJson.data.Get.Article);
      });
    setLoading(false);
  };

  console.log(news)

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
              <p>{article.text}</p>
            </div>
            <div className="article-content">
              <p>Relevancy score: {article._additional.score}</p>
            </div>
          </div>
        ))}
        {loading && <LoadingIcon />}
      </div>
    </div>
  );
};

export default HomePage;
